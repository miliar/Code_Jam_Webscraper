#include <stdio.h>
#include <algorithm>
using namespace std;
int gcd(int a, int b)
{
	if(b==0)
		return a;
	else
		return gcd(b, a%b);
}
int main()
{
	int t[4];
	int C,N;
	int i,j,k;
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d",&C);
	for (i=1;i<=C;i++)
	{
		scanf("%d",&N);
		for (j=0;j<N;j++)
		{
			scanf("%d",&t[j]);
		}
		sort(t,t+N);
		int g;
		g=t[1]-t[0];
		for (j=0;j<N;j++)
		{
			for (k=j+1;k<N;k++)
			{
				g=gcd(g, t[k]-t[j]);
			}
		}
		int r;
		if (t[0]%g==0)
		{
			r=0;
		}
		else
		{
			r=g-t[0]%g;
		}
		printf("Case #%d: %d\n",i,r);
	}
}