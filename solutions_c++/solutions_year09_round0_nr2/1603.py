#include <cstdio>
#include <cstring>

int H, W;
int m[110][110];
int b[110][110];
int label[30];
int prox;
int caso;

int coord[4][2] = { {-1,0}, {0,-1}, {0,1}, {1,0} };

void read() {
	scanf("%d%d", &H, &W);
	
	for (int i = 0; i < H; i++) {
		for (int j = 0; j < W; j++) {
			scanf("%d", &m[i][j]);
		}
	}
}

void calc(int r, int c) {
	if (b[r][c] == -1) {
		int rDest, cDest;
		int rMenor = -1;
		int cMenor = -1;
		for (int i = 0; i < 4; i++) {
			rDest = r+coord[i][0];
			cDest = c+coord[i][1];
			
			if (rDest >= 0 && rDest < H && cDest >= 0 && cDest < W) {
				if (m[rDest][cDest] < m[r][c]) {
					if (rMenor == -1 || m[rDest][cDest] < m[rMenor][cMenor]) {
						rMenor = rDest;
						cMenor = cDest;
					}
				}
			}
			
			
		}
		
		if (rMenor != -1) {
			calc(rMenor,cMenor);
			b[r][c] = b[rMenor][cMenor];
		} else {
			//printf("em r %d, c %d -> %d\n", r, c, prox);
			b[r][c] = prox++;
		}
	}
}

void process() {
	memset(b, -1, sizeof(b));
	
	prox = 0;
	for (int i = 0; i < H; i++) {
		for (int j = 0; j < W; j++) {
			calc(i,j);
		}
	}
	/*
	printf("os b\n");
	for (int i = 0; i < H; i++) {
		for (int j = 0; j < W; j++) {
			printf("%d ", b[i][j]);
		}
		printf("\n");
	}
	printf("\n");
	*/
	
	printf("Case #%d:\n", caso++);
	
	memset(label, -1, sizeof(label));
	prox = 'a';
	for (int i = 0; i < H; i++) {
		for (int j = 0; j < W; j++) {
			if (label[b[i][j]] == -1) {
				label[b[i][j]] = prox++;
			}
			
			if (j != 0) {
				printf(" ");
			}
			
			printf("%c", label[b[i][j]]);
		}
		printf("\n");
	}
}

int main() {
	//freopen("B-large.in", "r", stdin);
	//freopen("b.out", "w", stdout);
	
	caso = 1;
	
	int casos;
	scanf("%d", &casos);
	
	for (int i = 1; i <= casos; i++) {
		read();
		process();
	}
	
	return 0;
}
