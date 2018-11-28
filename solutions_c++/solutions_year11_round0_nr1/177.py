#include <cstring>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cmath>

int curtime, freetime[2], pos[2];

void move(int x, int y, int target) {
	if (abs(target - pos[x]) > freetime[x]) {
		if (target > pos[x]) pos[x] += freetime[x];
		else pos[x] -= freetime[x];
		int d = abs(target - pos[x]);
		curtime += d;
		freetime[y] += d;
	}
	pos[x] = target;
	++curtime;
	++freetime[y];
	freetime[x] = 0;
}

int main() {
	FILE *fin = fopen("in.txt", "r");
	FILE *fout = fopen("out.txt", "w");
	int t, n;
	fscanf(fin, "%d", &t);
	for (int i = 1; i <= t; ++i) {
		fprintf(fout, "Case #%d: ", i);
		curtime = 0;
		freetime[0] = 0;
		freetime[1] = 0;
		pos[0] = 1;
		pos[1] = 1;
		fscanf(fin, "%d", &n);
		for (int j = 0; j < n; ++j) {
			char name[2];
			int target;
			fscanf(fin, "%s %d", name, &target);
			if (name[0] == 'O') move(0, 1, target);
			else move(1, 0, target);
		}
		fprintf(fout, "%d\n", curtime);
	}
	fclose(fout);
	fclose(fin);
	return 0;
}
