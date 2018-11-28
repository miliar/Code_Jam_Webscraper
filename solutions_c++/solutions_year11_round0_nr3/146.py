#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

int t,n,xorsum,p,q;
int a[1100];
int f[2][1<<20];


int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	cin >> t;
	for (int k=1;k<=t;k++)
	{
		cin >> n;
		for (int i=1;i<=n;i++) cin >> a[i];
		xorsum = 0;
		for (int i=1;i<=n;i++) xorsum ^= a[i];
		if (xorsum!=0)
		{
			printf("Case #%d: NO\n",k);
			continue;
		}
		/*
		p = 0;
		q = 1;
		for (int i=0;i<(1<<20);i++) f[p][i] = -100000000;
		f[p][0] = 0;
		for (int i=1;i<=n;i++)
		{
			for (int j=0;j<(1<<20);j++) if (f[p][j]>=0)
				f[q][j^a[i]] = max(f[q][j^a[i]], f[p][j]+a[i]);
		}
		int ans = 0;
		for (int j=0;j<(1<<20);j++) if ()*/
		sort(a+1,a+n+1);
		int ans = 0;
		for (int i=2;i<=n;i++) ans += a[i];
		printf("Case #%d: %d\n",k,ans);
	}
	
	return 0;
}
