#include <stdio.h>

int W, H;
int height[128][128];
char nextBasin;
char basin[128][128];

const int dx[4] = {0, -1, 1, 0};
const int dy[4] = {-1, 0, 0, 1};

char getb(int y, int x) {
	if (basin[y][x]!=-1)
		return basin[y][x];
	int dir = -1;
	for (int i=0; i<4; i++)
		if ((unsigned int)(y+dy[i])<(unsigned int)H && (unsigned int)(x+dx[i])<(unsigned int)W)
			if (height[y+dy[i]][x+dx[i]]<height[y][x])
				if (dir==-1 || height[y+dy[i]][x+dx[i]]<height[y+dy[dir]][x+dx[dir]])
					dir = i;
	if (dir==-1)
		return basin[y][x] = nextBasin++;
	return basin[y][x] = getb(y+dy[dir], x+dx[dir]);
}

int main() {
	FILE *fi = fopen("b.in", "r");
	FILE *fo = fopen("b.out", "w");
	int T;
	fscanf(fi, "%d", &T);
	for (int t=0; t<T; t++) {
		fscanf(fi, "%d%d", &H, &W);
		for (int y=0; y<H; y++) {
			for (int x=0; x<W; x++) {
				fscanf(fi, "%d", height[y]+x);
				basin[y][x] = -1;
			}
		}
		nextBasin = 'a';
		fprintf(fo, "Case #%d:\n", t+1);
		for (int y=0; y<H; y++) {
			for (int x=0; x<W; x++) {
				fputc(getb(y, x), fo);
				fputc(' ', fo);
			}
			fputc('\n', fo);
		}
	}
	fclose(fo);
	fclose(fi);
	return 0;
}
