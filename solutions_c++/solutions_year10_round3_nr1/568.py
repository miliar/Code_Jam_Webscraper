#include<iostream>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<vector>
using namespace std;
struct pp
{
	int s, e;
}a[1001];
int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	long long  tt, ii, n, cnt, i, j;
	scanf("%lld\n", &tt);
	for(ii=1; ii<=tt; ii++)
	{
		scanf("%lld\n", &n);
		cnt=0;
		for(i=1; i<=n; i++)
			scanf("%d %d\n", &a[i].s, &a[i].e);
		for(i=1; i<=n; i++)
			for(j=1; j<=n; j++)
			{
				if( (a[i].s>a[j].s && a[i].e<a[j].e )|| (a[i].s<a[j].s && a[i].e>a[j].e ))
					cnt++;
			}
		cout<<"Case #"<<ii<<": "<<cnt/2<<'\n';
	}
	return 0;
}