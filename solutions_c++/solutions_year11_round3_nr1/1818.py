#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <assert.h>

int main()
{
	int T, R, C, t;
	char g[50][55];

	scanf("%d", &T);
	for (t = 1; t <= T; t++) {
		scanf("%d %d", &R, &C);
		for (int i=0;i<R;i++){
			scanf("%s", g[i]);
		}

		for (int i=0;i<R-1;i++){
			for (int j=0;j<C-1;j++) {
				if (g[i][j] == '#' && g[i][j+1] == '#' && g[i+1][j] == '#' && g[i+1][j+1] == '#') {
					g[i][j] = '/';
					g[i][j+1] = '\\';
					g[i+1][j] = '\\';
					g[i+1][j+1] = '/';
				}
			}
		}

		for (int i=0;i<R;i++){
			for (int j=0;j<C;j++){
				if (g[i][j] == '#')
					goto error;
				if (g[i][j] == '.')
					continue;
			}
		}

		printf("Case #%d:\n", t);
		for (int i=0;i<R;i++){
			puts(g[i]);
		}
		continue;
error:
		printf("Case #%d:\nImpossible\n", t);
	}

	return 0;
}
