#include <cstdio>
#include <cstring>

int T, R, C;
char mat[60][60];

int main()
{
	scanf("%d", &T);
	for(int _42 = 1; _42 <= T; ++_42) {
		printf("Case #%d:\n", _42);
		memset(mat, '.', sizeof(mat));

		scanf("%d %d", &R, &C);

		for(int i = 0; i < R; ++i) {
			scanf("%s", mat[i]);
		}

		bool poss = true;
		for(int i = 0; i < R; ++i) {
			for(int j = 0; j < C; ++j) {
				if(mat[i][j] == '#') {
					if(mat[i+1][j] != '#'
					|| mat[i][j+1] != '#'
					|| mat[i+1][j+1] != '#') {
						poss = false;
						break;
					} else {
						mat[i][j] = '/';
						mat[i][j+1] = '\\';
						mat[i+1][j] = '\\';
						mat[i+1][j+1] = '/';
					}
				}
			}
			if(!poss) break;
		}

		if(!poss) {
			printf("Impossible\n");
		} else {
			for(int i = 0; i < R; ++i) {
				printf("%s\n", mat[i]);
			}
		}
	}
	return 0;
}
