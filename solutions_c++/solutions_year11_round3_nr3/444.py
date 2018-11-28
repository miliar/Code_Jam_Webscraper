#include <iostream>
#include <cstdio>
using namespace std;

int a[20000],l,h,tes,n;

int ok(int x)
{
	for (int i=1;i<=n;i++)
		if (x%a[i]==0 || a[i]%x==0) continue;
		else return 0;
	return 1;
}

int solve()
{
	for (int i=l;i<=h;i++)
		if (ok(i)) return i;
	return 0;
}


int main()
{
	freopen("c.out","w",stdout);
	scanf("%d",&tes);
	for (int ttt=1;ttt<=tes;ttt++)
	{
		scanf("%d%d%d",&n,&l,&h);
		for (int i=1;i<=n;i++) scanf("%d",&a[i]);
		printf("Case #%d: ",ttt);
		int t=solve();
		if (t) printf("%d\n",t);
		else printf("NO\n");
	}
}
