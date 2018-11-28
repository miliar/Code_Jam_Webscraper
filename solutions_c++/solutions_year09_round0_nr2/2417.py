#include <stdio.h>
#include <string.h>
#include <math.h>

int t, h, w;
int area[101][101];
int drain[101][101];
int drains = 0;

int inspect(int y, int x) {
	if(x<0 || x>w || y<0 || y>h)
		return 0;

	if(drain[y][x]!=0)
		return 0;

	int min = area[y][x];
	int minx = x, miny = y;
	
	//Nord
	if(min > area[y-1][x] && y>1) {
		min = area[y-1][x];
		minx = x;
		miny = y - 1;
	}

	//West
	if(min > area[y][x-1] && x>1) {
		min = area[y][x-1];
		minx = x - 1;
		miny = y;
	}

	//East
	if(min > area[y][x+1] && x<w) {
		min = area[y][x+1];
		minx = x + 1;
		miny = y;
	}

	//South
	if(min > area[y+1][x] && y<h) {
		min = area[y+1][x];
		minx = x;
		miny = y + 1;
	}

	if(min==area[y][x]) {
		drains++;
		drain[y][x] = drains;
		return drains;
	}

	if(drain[miny][minx]!=0)
		drain[y][x] = drain[miny][minx];
	else
		drain[y][x] = inspect(miny, minx);
	return drain[y][x];
}

int main() {
	int matchWords;
	bool match;

	FILE *fin=fopen("B-large.in","r");
	FILE *fout=fopen("watersheds.out","w");

	fscanf(fin, "%d", &t);

	for(int i=0; i<t; i++) {
		drains = 0;
		fscanf(fin, "%d %d", &h, &w);
		
		for(int j=1; j<=h; j++) {
			for(int k=1; k<=w; k++) {
				fscanf(fin, "%d", &area[j][k]);
				//printf("%d ", area[j][k]);
				drain[j][k] = 0;
			}
			//printf("\n");
		}

		for(int j=1; j<=h; j++)
			for(int k=1; k<=w; k++)
				inspect(j, k);

		fprintf(fout, "Case #%d:\n", i+1);

		for(int j=1; j<=h; j++) {
			for(int k=1; k<=w; k++)
				fprintf(fout, "%c ", drain[j][k]+96);
			fprintf(fout, "\n");
		}
	}

	return 0;
}
