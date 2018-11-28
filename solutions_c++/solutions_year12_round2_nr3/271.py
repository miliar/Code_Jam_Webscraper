#include <stdio.h>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <memory.h>

using namespace std;

int i,j,k,l,m,h;
int t,T;
int n;
int a[500];
int s;
double p;
int it;
int u[5000000];

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);

	scanf("%d", &T);
	for(t=1; t<=T; t++)
	{
		memset(u, 0, sizeof(u));
		s = 0;
		scanf("%d", &n);
		for (i=0; i<n; i++)
		{
			scanf("%d", &a[i]);
		}
		k = 1<<n;

		printf("Case #%d:\n", t);
		for(i=1; i<k; i++)
		{
			s = 0;
			for (j=i, l=0; j!=0; j>>=1, l++)
			{
				if(j&1)
				{
					s+=a[l];
				}
			}
			if(u[s]!=0)
			{
				for (m=u[s], h=0; m!=0; m>>=1, h++)
				{
					if(m&1)
					{
						printf("%d ", a[h]);
					}
				}
				printf("\n");
				for (m=i, h=0; m!=0; m>>=1, h++)
				{
					if(m&1)
					{
						printf("%d ", a[h]);
					}
				}
				printf("\n");
				break;
			}
			u[s]=i;
		}
		if(i==k)
		{
			printf("Impossible\n");
		}
    }
	return 0;
}