#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

typedef struct {
	short x, y, z;
	short vx, vy, vz;
} firefly;

typedef struct {
	double x, y, z;
	double vx, vy, vz;
} firefly_d;

int main(int argc, char *argv[]) {
	char *in_name, *out_name;
	FILE *in_file, *out_file;
	
	if (argc != 3) {
		printf("Usage: %s <infile> <outfile>\n", argv[0]);
		return 1;
	}
	
	in_name = argv[1];
	out_name = argv[2];
	
	in_file = fopen(in_name, "r");
	out_file = fopen(out_name, "w");
	
	int T;
	firefly cases[100][500];
	firefly_d totals[100];
	
	int N[100];
	
	fscanf(in_file, "%d", &T);
	
	for (int i = 0; i < T; i++) {
		fscanf(in_file, "%d", &N[i]);
		totals[i].x = 0;
		totals[i].y = 0;
		totals[i].z = 0;
		totals[i].vx = 0;
		totals[i].vy = 0;
		totals[i].vz = 0;
		for (int j = 0; j < N[i]; j++) {
			fscanf(in_file, "%hu %hu %hu %hu %hu %hu",
				&cases[i][j].x, &cases[i][j].y, &cases[i][j].z,
				&cases[i][j].vx, &cases[i][j].vy, &cases[i][j].vz);
			totals[i].x += cases[i][j].x;
			totals[i].y += cases[i][j].y;
			totals[i].z += cases[i][j].z;
			totals[i].vx += cases[i][j].vx;
			totals[i].vy += cases[i][j].vy;
			totals[i].vz += cases[i][j].vz;
		}
	}
	
	for (int i = 0; i < T; i++) {
		firefly_d t = totals[i];
		double dmin, tmin;
		
		if (t.vx == 0 && t.vy == 0 && t.vz == 0) {
			tmin = 0;
		} else {
			tmin = -(t.x * t.vx + t.y * t.vy + t.z * t.vz) /
				(pow(t.vx, 2) + pow(t.vy, 2) + pow(t.vz, 2));
			if (tmin <= 0)
				tmin = 0;
		}
		t.x /= N[i];
		t.y /= N[i];
		t.z /= N[i];
		t.vx /= N[i];
		t.vy /= N[i];
		t.vz /= N[i];
		dmin = sqrt(pow(t.x + t.vx * tmin, 2) + pow(t.y + t.vy * tmin, 2)
			+ pow(t.z + t.vz * tmin, 2));
		fprintf(out_file, "Case #%d: %.08f %.08f\n", i + 1, dmin, tmin);
	}
	
	fclose(in_file);
	fclose(out_file);
	
	return 0;
}