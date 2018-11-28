#include <cstdio>

int mapa[200][200];
int conjunto[40000];
char letra[40000];

int H,W;

int findset(int a) {
	if (a != conjunto[a]) {
		conjunto[a] = findset(conjunto[a]);
	}
	return conjunto[a];
}

void unir(int a, int b) {
	//printf("unir %d %d\n", a, b);
	conjunto[findset(a)] = findset(b);
}

void process() {
	scanf("%d%d", &H, &W);
	for (int i = 0 ; i < H ; i++) {
		for (int j = 0 ; j < W ; j++) {
			scanf("%d", &mapa[i][j]);
			conjunto[i*W+j] = i*W+j;
			letra[i*W+j] = '?';
		}
	}
	
	int op; // North, West, East, South
	int altitude; 
	for (int i = 0 ; i < H ; i++) {
		for (int j = 0 ; j < W ; j++) {
			op = -1;
			if (i > 0) {
				if (mapa[i-1][j] < mapa[i][j]) {
					if (op == -1 || altitude > mapa[i-1][j]) {
						op = 0;
						altitude = mapa[i-1][j];
					}
				}
			}
			if (j > 0) {
				if (mapa[i][j-1] < mapa[i][j]) {
					if (op == -1 || altitude > mapa[i][j-1]) {
						op = 1;
						altitude = mapa[i][j-1];
					}
				}
			}
			
			if (j < W-1) {
				if (mapa[i][j+1] < mapa[i][j]) {
					if (op == -1 || altitude > mapa[i][j+1]) {
						op = 2;
						altitude = mapa[i][j+1];
					}
				}
			}
			if (i < H-1) {
				if (mapa[i+1][j] < mapa[i][j]) {
					if (op == -1 || altitude > mapa[i+1][j]) {
						op = 3;
						altitude = mapa[i+1][j];
					}
				}
			}
			
			//printf("op(%d,%d) = %d\n",i,j,op);
			
			if (op == 0) {
				unir(i*W+j, (i-1)*W+(j));
			} else if (op == 1) {
				unir(i*W+j, (i)*W+(j-1));
			} else if (op == 2) {
				unir(i*W+j, (i)*W+(j+1));
			} else if (op == 3) {
				unir(i*W+j, (i+1)*W+(j));
			}
			
		}
	}
	
	char proxLetra = 'a';
	int pos;
	for (int i = 0 ; i < H ; i++) {
		for (int j = 0 ; j < W ; j++) {
			pos = findset(i*W+j);
			if (letra[pos] == '?') {
				letra[pos] = proxLetra++;
			}
			if (j) {
				printf(" ");
			}
			printf("%c", letra[pos]);
		}
		printf("\n");
	}
	
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	int T;
	scanf("%d", &T);
	
	for (int i = 1 ; i <= T ; i++) {
		printf("Case #%d:\n", i);
		process();
	}
	
	return 0;
}
