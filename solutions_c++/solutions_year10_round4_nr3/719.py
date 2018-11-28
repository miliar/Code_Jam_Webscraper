
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

#define MAX 128

int m[MAX][MAX][2];

int main(void)
{
	int i, j, k, r, a,b,c,d;
	int nc;

	scanf("%d", &nc);
	for(int ca=1;ca<=nc; ca++)
	{
		printf("Case #%d: ", ca);

		memset(m, 0, sizeof(m));
		scanf("%d", &r);
		for(k=0; k<r; k++)
		{
			scanf("%d %d %d %d", &a, &b, &c, &d);
			
			for(i=a; i<=c; i++)
			{
				for(j=b; j<=d; j++)
				{
					m[i][j][0] = 1;
				}
			}
		}

		int cnt;
		for(k=1; ; k++)
		{
			cnt = 0;
			int x = !(k%2);

			for(i=1; i<MAX; i++)
			{
				for(j=1; j<MAX; j++)
				{
					if(!m[i-1][j][x] && !m[i][j-1][x])
						m[i][j][k%2] = 0;
					else if(m[i-1][j][x] && m[i][j-1][x])
						m[i][j][k%2] = 1;
					else
						m[i][j][k%2] = m[i][j][x];

					cnt += m[i][j][k%2];
				}
			}

			if(cnt == 0) break;
		}

		printf("%d\n", k);
	}

	return 0;
}
