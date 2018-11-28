#include<stdio.h>
#include<string.h>

int csN, csK, R, C, map[128][128];
char B[128][128], dir[128][128], dr[4] = {-1, 0, 0, 1}, dc[4] = {0, -1, 1, 0};

void fill(int r, int c, char ch)
{
	if(B[r][c] != 0) return;
	B[r][c] = ch;
	if(dir[r][c] != -1)
	{
		int x = dir[r][c];
		fill(r+dr[x], c+dc[x], ch);
	}
	for(int i = 0; i < 4; ++i)
		if(dir[r+dr[i]][c+dc[i]] == (i^3))
			fill(r+dr[i], c+dc[i], ch);
}

int main()
{
	int i, j, k, m;
	char c;
	scanf("%d", &csN);
	for(csK = 1; csK <= csN; ++csK)
	{
		scanf("%d %d", &R, &C);
		memset(map, 63, sizeof(map));
		for(i = 1; i <= R; ++i)
			for(j = 1; j <= C; ++j)
				scanf("%d", &map[i][j]);
		printf("Case #%d:\n", csK);
		memset(dir, -1, sizeof(dir));
		for(i = 1; i <= R; ++i) {
			for(j = 1; j <= C; ++j)
			{
				for(m = k = 0; k < 4; ++k)
					if(map[i+dr[m]][j+dc[m]] > map[i+dr[k]][j+dc[k]])
						m = k;
				if(map[i+dr[m]][j+dc[m]] < map[i][j])
					dir[i][j] = m;
				else dir[i][j] = -1;
		//		fprintf(stderr, "%3d", dir[i][j]);
			}
		//	fprintf(stderr, "\n");
		}
		memset(B, 0, sizeof(B));
		for(c = 'a', i = 1; i <= R; ++i)
			for(j = 1; j <= C; ++j)
				if(B[i][j] == 0)
					fill(i, j, c++);
		for(i = 1; i <= R; ++i)
		{
			printf("%c", B[i][1]);
			for(j = 2; j <= C; ++j)
				printf(" %c", B[i][j]);
			printf("\n");
		}
	}
}
