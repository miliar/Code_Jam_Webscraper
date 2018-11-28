
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

#define MAX 1024
int v[MAX];
int cost[MAX][MAX];

int main(void)
{
	int nc;
	int i, j, p;

	scanf("%d", &nc);
	for(int ca=1;ca<=nc; ca++)
	{
		printf("Case #%d: ", ca);

		scanf("%d", &p);
		for(i=0; i<(1<<p); i++)
		{
			scanf("%d", &v[i]);
			v[i] = p-v[i];
			//printf("v[%d] = %d\n", i, v[i]);
		}

		for(i=0; i<p; i++)
		{
			for(j=0; j<(1<<(p-1-i)); j++)
			{
				scanf("%d", &cost[i][j]);
			}
		}

		int res = 0;

		for(int lv = p; lv>0; lv--)
		{
			for(int g=0; g<(1<<(p-lv)); g++)
			{
				int q = 1<<(lv);

				for(int t=g * q; t < (g+1)*q; t++)
				{
					if(v[t] > 0)
					{
						//printf("level %d, game %d, team %d - limites %d a %d - v=%d - p=%d\n", lv,g,t, g*q, (g+1)*q, v[t], p);
						res++; //custo aqui!!
						for(i=g*q; i<(g+1)*q; i++) v[i]--;

						break;
					}
				}
			}
		}

		printf("%d\n", res);
	}

	return 0;
}
