#include <cstdio>
#include <cstring>
int T, H, W;
int mtx[100][100], cnn[100][100][4];
char fill[100][100];
void DFS(int a, int b){
	if(cnn[a][b][0] && !fill[a-1][b]) { fill[a-1][b] = fill[a][b]; DFS(a-1, b); }
	if(cnn[a][b][1] && !fill[a][b+1]) { fill[a][b+1] = fill[a][b]; DFS(a, b+1); }
	if(cnn[a][b][2] && !fill[a+1][b]) { fill[a+1][b] = fill[a][b]; DFS(a+1, b); }
	if(cnn[a][b][3] && !fill[a][b-1]) { fill[a][b-1] = fill[a][b]; DFS(a, b-1); }
}
void run(void){
	memset(fill, 0, sizeof(fill));
	memset(cnn, 0, sizeof(cnn));
	scanf("%d %d", &H, &W);
	for(int i = 0; i < H; ++i)
		for(int j = 0; j < W; ++j)
			scanf("%d", &mtx[i][j]);
	char ab = 'a';
	for(int i = 0; i < H; ++i){
		for(int j = 0; j < W; ++j){
			int dir = -1, wei = mtx[i][j];
			if(i-1>=0 && mtx[i-1][j] < wei){
				wei = mtx[i-1][j];
				dir = 0;
			}
			if(j-1>=0 && mtx[i][j-1] < wei){
				wei = mtx[i][j-1];
				dir = 3;
			}
			if(j+1<W && mtx[i][j+1] < wei){
				wei = mtx[i][j+1];
				dir = 1;
			}
			if(i+1<H && mtx[i+1][j] < wei){
				wei = mtx[i+1][j];
				dir = 2;
			}
			switch(dir){
				case 0: cnn[i][j][0] = cnn[i-1][j][2] = 1; break;
				case 1: cnn[i][j][1] = cnn[i][j+1][3] = 1; break;
				case 2: cnn[i][j][2] = cnn[i+1][j][0] = 1; break;
				case 3: cnn[i][j][3] = cnn[i][j-1][1] = 1; break;
			}
		}
	}
	for(int i = 0; i < H; ++i)
		for(int j = 0; j < W; ++j){
			if(fill[i][j] == 0){
				fill[i][j] = ab++;
				DFS(i, j);
			}
		}
}
int main(void){
	scanf("%d", &T);
	for(int i = 1; i <= T; ++i){
		printf("Case #%d:\n", i);
		run();
		for(int i = 0; i < H; ++i){
			for(int j = 0; j < W; ++j){
				if(j) putchar(' ');
				putchar(fill[i][j]);
			}
			putchar('\n');
		}
	}
	return 0;
}
