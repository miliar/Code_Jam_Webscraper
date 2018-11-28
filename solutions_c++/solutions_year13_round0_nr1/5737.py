#include <cstdio>

int dx[] = {1,0,1,1};
int dy[] = {0,1,1,-1};

int T,t,i,j,k,d,nx,ny,dots,ts,sm;
char s[10][10];

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d\n", &T);
	for (t = 0; t < T; t++) {
		for (i = 0; i < 4; i++, scanf("\n"))
			for (j = 0; j < 4; j++) scanf("%c", &s[i][j]);
		scanf("\n");

		/*for (i = 0; i < 4; i++, printf("\n"))
			for (j = 0; j < 4; j++) printf("%c", s[i][j]);
		printf("----\n");*/

		dots = 0;
		for (i = 0; i < 4; i++)
			for (j = 0; j < 4; j++)
				dots += s[i][j] == '.';

		for (i = 0; i < 4; i++) {
			for (j = 0; j < 4; j++) {
				if (s[i][j] == '.' || s[i][j] == 'T')
					continue;
				for (d = 0; d < 4; d++) {
					sm = 0; ts = 0;
					for (k = 0; k < 4; k++) {
						nx = i + dx[d] * k;
						ny = j + dy[d] * k;
						if (nx > 3 || ny > 3)
							break;
						if (s[i][j] == s[nx][ny])
							sm++;
						if (s[nx][ny] == 'T')
							ts++;
					}
					if (sm == 4 || (sm == 3 && ts == 1)) {
						printf("Case #%d: %c won\n", t+1, s[i][j]);
						goto br;
					}
				}
			}
		}

		if (dots)
			printf("Case #%d: Game has not completed\n", t+1);
		else
			printf("Case #%d: Draw\n", t+1);
		br:;
	}
}