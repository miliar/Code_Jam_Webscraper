
#include <stdio.h>

#define MAX 105

int t,w,h;
int map[MAX][MAX];
char finmap[MAX][MAX];
char cact;

//delta row, delta col
int delta[8] = {-1,0,0,-1,0,1,1,0};

//Retorna la altitud o infinito si posicion invalida
int altitud(int r, int c) {
	if (r<0 || r>=h || c<0 || c>=w) {
		return 0x3fffffff;
	}
	return map[r][c];
}

char poner(int r, int c) {
	if (finmap[r][c] != '\0') return finmap[r][c];
	int min = 0x3fffffff;
	int fr, fc;
	for (int i=0; i<4; i++) {
		int nr = r+delta[2*i], nc = c+delta[2*i+1];
		int na = altitud(nr, nc);
		if (min > na) {
			min = na;
			fr=nr; fc=nc;
		}
	}
	if (min >= map[r][c]) {
		//sink node
		char car = cact;
		cact++;
		finmap[r][c] = car;
		return car;
	} else {
		finmap[r][c] = poner(fr, fc);
		return finmap[r][c];
	}
}

void solve() {
	cact='a';
	for (int i=0; i<h; i++) {
		for (int j=0; j<w; j++) {
			finmap[i][j] = '\0';
		}
	}
	for (int i=0; i<h; i++) {
		for (int j=0; j<w; j++) {
			poner(i,j);
		}
	}
}

int main(int argc, char **argv) {
	scanf("%i", &t);
	for (int caso=0; caso<t; caso++) {
		scanf("%i %i", &h, &w);
		for (int i=0; i<h; i++) {
			for (int j=0; j<w; j++) {
				scanf("%i", &map[i][j]);
			}
		}
		solve();
		printf("Case #%i:\n", caso+1);
		for (int i=0; i<h; i++) {
			for (int j=0; j<w; j++) {
				printf("%c ", finmap[i][j]);
			}
			printf("\n");
		}
	}
}