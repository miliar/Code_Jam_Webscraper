#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

#define LIMIT 20

char mat[LIMIT][LIMIT];
int map[LIMIT][LIMIT];
int H, W;
char currcomp;

void printmat()
{
	for(int i = 0; i < H; ++i) {
		printf("%c", mat[i][0]);
		for(int j = 1; j < W; ++j) {
			printf(" %c", mat[i][j]);
		}
		printf("\n");
	}
}

void printmap()
{
	for(int i = 0; i < H+2; ++i) {
		printf("%d", map[i][0]);
		for(int j = 1; j < W+2; ++j) {
			printf(" %d", map[i][j]);
		}
		printf("\n");
	}
}

char dfs(int i, int j) {
	//if sink
	int N, W, E, S;

	if(mat[i][j] != 0) return mat[i][j];

	if(map[i+1][j+1] == 0xA0) {
		//printf("FUUUUCK!!!\n");
		return '0';
	}

	N = map[i-1+1][j+1];
	W = map[i+1][j-1+1];
	E = map[i+1][j+1+1];
	S = map[i+1+1][j+1];

	int cell = map[i+1][j+1];

	//printf("[%d, %d] -> map:%d   N:%d   W:%d   E:%d   S:%d\n", i+1, j+1, map[i+1][j+1], N, W, E, S);

	if(N >= cell && W >= cell && E >= cell && S >= cell) {
		//printf("Gotta sink! ");
		if(mat[i][j] == 0) {
			mat[i][j] = currcomp;
			//printf("labeled it:");
			currcomp++;
		}
		//printf("%c\n", mat[i][j]);
		return mat[i][j];
	}
	int l = min(N, min(W, min(E, S)));
	if(N == l) {
		mat[i][j] = dfs(i-1, j);
	} else if(W == l) {
		mat[i][j] = dfs(i, j-1);
	} else if(E == l) {
		mat[i][j] = dfs(i, j+1);
	} else if(S == l) {
		mat[i][j] = dfs(i+1, j);
	}
	return mat[i][j];
}

int main()
{
	int X;
	scanf(" %d", &X);
	for(int _42 = 1; _42 <= X; ++_42) {
		scanf(" %d %d", &H, &W);
		memset(map, 0x0F, sizeof(map));
		for(int i = 0; i < H; ++i) {
			for(int j = 0; j < W; ++j) {
				scanf(" %d", &map[i+1][j+1]);
			}
		}

		memset(mat, 0, sizeof(mat));
		currcomp = 'a';

		//printmap();

		//mat[0][0] = 'a';

		int found = 0;
		for(int i = 0; i < H; ++i) {
			for(int j = 0; j < W; ++j) {
				if(mat[i][j] == 0) {
					found++;
					mat[i][j] = dfs(i, j);
				}
			}
			/*if(i == H-1 && found) {
				i = 0;
			} else {
				break;
			}*/
		}

		printf("Case #%d:\n", _42);
		printmat();
	}
	return 0;
}
