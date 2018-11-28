#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
int t,n,s;
struct N
{
	int x,y;
}a[1010];

bool cmp(N p,N q)
{
	return (p.x<q.x);
}

int main()
{
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);
	scanf("%d",&t);
	for (int tt=1;tt<=t;tt++)
	{
		scanf("%d",&n);
		for (int i=1;i<=n;i++)
		{
			scanf("%d",&a[i].x);
			a[i].y=i;
		}
		s=0;
		sort(a+1,a+n+1,cmp);
		for (int i=1;i<=n;i++)
			if (i!=a[i].y) s++;
		printf("Case #%d: %d.000000\n",tt,s);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}