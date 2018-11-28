#include <stdio.h>
#include <string.h>

int N, R, C;
char b[17][17];
int mv[8][2] = {{1,1}, {1,0}, {1,-1}, {0,1}, {0,-1}, {-1,1}, {-1,0}, {-1,-1}};

int play(int i, int j, int s)
{
	//printf("%d %d %d\n", i,j,s);
	for (int k=0;k<8;k++)
	{
		if (b[i+mv[k][0]][j+mv[k][1]] == '.')
		{
			b[i+mv[k][0]][j+mv[k][1]] = '#';
			if (play(i+mv[k][0], j+mv[k][1],(!s)) == s)
			{
				b[i+mv[k][0]][j+mv[k][1]] = '.';
				return s;
			}

			b[i+mv[k][0]][j+mv[k][1]] = '.';
		}
	}

	//printf("%d %d %d %c loses\n", i,j,s, b[i][j]);
	return (!s);
}

int main()
{
	int bst,i,j;
	scanf("%d", &N);

	for (int cs=1; cs<=N; cs++)
	{
		memset(b,'#',sizeof(b));
		scanf("%d %d", &R, &C);
		for (i=1;i<=R;i++)
		{
			scanf("%s", b[i]+1);
			int k = strlen(b[i]);
			b[i][k]='#';
		}
	
	/*	
		for (i=0;i<=R+1;i++)
		{
			for (j=0;j<=C+1;j++)
				printf("%c", b[i][j]);

			printf("\n");
		}
*/
		for (i=1;i<=R;i++)
		{
			for (j=1;j<=C;j++)
				if (b[i][j] == 'K') break;

			if (j <= C) break;
		}
		
		//printf("%d %d %c\n", i, j, b[i][j]);
		b[i][j] = '#';
		bst = play(i,j,0);

		if (!bst) printf("Case #%d: A\n", cs);
		else printf("Case #%d: B\n", cs);
	}

	return 0;
}
