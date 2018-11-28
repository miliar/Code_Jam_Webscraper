#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;
int v[150];
int x[150];
double nt[150];
double tt[150];
int main()
{
	freopen("g2.in","r",stdin);
	freopen("g2.out","w",stdout);
	int c;
	scanf("%d",&c);
	int i,j;
	int n,k,b,t;
	int cnt;
	int ob;
	int ans;
	double divide;
	for (i = 1;i <= c;i++)
	{
		cnt = 0;
		ob = 0;
		ans = 0;
		scanf("%d%d%d%d",&n,&k,&b,&t);
		for (j = 1;j <= n;j++)
		{
			scanf("%d",&x[j]);
			x[j] = b-x[j];
		}
		for (j = 1;j <= n;j++)
			scanf("%d",&v[j]);
		for (j = 1;j <= n;j++)
		{
			nt[j] = double(x[j])/double(v[j]);
			tt[j] = nt[j];
		}
		sort(&nt[1],&nt[n+1]);
		divide = nt[k];
		if (divide > double(t))
		{
			printf("Case #%d: IMPOSSIBLE\n",i);
			continue;
		}
		if (double(t) > divide)
			divide = double(t);
		
		for (j = n;cnt < k&&j >= 1;j--)
		{
			if (tt[j] > divide)
			{
				ob ++;
			}
			else
			{
				cnt ++;
				ans += ob;
			}
		}
		printf("Case #%d: %d\n",i,ans);
				
	}
	
}