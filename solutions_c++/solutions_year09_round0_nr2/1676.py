#include <stdio.h>
#include <string.h>

char doflow(int basin[][100], char sink[][100], int i, int j, int h, int w, char let) {
	int myalt = basin[i][j];
	char c;
	int alt = myalt;
	int xdir=0, ydir=0;
	c = sink[i][j];
	if (c != ' ')
		return c;
	if (i < h-1 && basin[i+1][j] <= alt) {
		alt = basin[i+1][j];
		xdir = 0; ydir = 1;
	}
	if (j < w-1 && basin[i][j+1] <= alt) {
		alt = basin[i][j+1];
		xdir=1; ydir = 0;
	}
	if (j > 0 && basin[i][j-1] <= alt) {
		alt = basin[i][j-1];
		xdir=-1; ydir = 0;
	}
	if (i > 0 && basin[i-1][j] <= alt) {
		alt = basin[i-1][j];
		xdir=0; ydir = -1;
	}
	if (alt == myalt) {
		sink[i][j] = let;
		return let;
	}
	c= doflow(basin, sink, i+ydir, j+xdir, h, w, let);	
	sink[i][j] = c;
	return c;
}

void flow(int basin[][100], int h, int w) {
	char sink[100][100];
	memset(sink, ' ', sizeof(sink));
	int i, j;
	char let = 'a';
	for (i=0; i < h; ++i)
		for(j=0; j < w; ++j)
			if (sink[i][j]==' ') {
				if (let ==doflow(basin, sink, i, j, h, w, let))
					++let;
			}

	for (i=0; i < h; ++i) {
		for(j=0; j < w; ++j) {
			printf ("%c", sink[i][j]);
			if (j < w-1)
				printf(" ");
		}
		printf("\n");
	}	
}

int main() {
	int t;
	int basin[100][100];
	scanf("%d\n", &t);
	for (int i = 0; i < t; ++i) {
		int h, w;
		memset(basin, 0, sizeof(basin));
		scanf("%d %d\n", &h, &w);
		for (int j = 0; j < h; ++j) {
			for (int k = 0; k < w; ++k)
				scanf("%d", &basin[j][k]);
			scanf("\n");
		}
		printf ("Case #%d:\n", i+1);
		flow(basin, h, w);
	}
}
