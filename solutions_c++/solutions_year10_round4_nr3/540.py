#include <stdio.h>
#include <cstring>

#define MAX 128

int m[MAX][MAX];

int main()
{
	int t, n;
	int cas;
	int x1, y1, x2, y2;

	scanf("%d", &t);

	for (cas=1; cas<=t; cas++)
	{
		printf("Case #%d: ", cas);
		memset(m, 0, sizeof(m));
		scanf("%d", &n);
//		printf("n=%d\n",n);
		int i;
		int x, y;
		for (i=0; i<n; i++)
		{
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);

//			printf("%d %d %d %d\n", x1, y1, x2, y2);
			for (x = x1 ; x <= x2; x++)
			{
				for (y=y1 ; y <= y2; y++)
				{
//					printf("%d %d\n", x1, y1);
					m[x][y] = 1;
				}
			}
		}

		int j, v =0;
		for (i=0; i<MAX; i++)
		{
			for (j=0; j<MAX; j++)
			{
				v += m[i][j];
			}
		}
		int resp = 0;
		while (v)
		{
			resp++;
/*						printf("\n");

			for (i=0; i<10; i++)
			{
				for (j=0; j<10; j++)
				{
					printf("%d", m[i][j]);
				}
				printf("\n");
			}
							printf("\n");

*/
			for (i=MAX-1; i>0; i--)
			{
				for (j=MAX-1; j>0; j--)
				{
					if (m[i-1][j] && m[i][j-1])
					{
						if (!m[i][j])
						{
							m[i][j] = 1;
							v++;
						}
					}
					if (!m[i-1][j] && !m[i][j-1] && m[i][j])
					{
						m[i][j] = 0;
						v--;
					}
				}
			}
		}
		printf("%d\n", resp);
	}

}
