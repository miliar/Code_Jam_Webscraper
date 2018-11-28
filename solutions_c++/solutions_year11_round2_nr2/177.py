#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

#define inf 1e20
#define maxn 1000006

const double eps	=	1e-3;

int a[maxn],n,D;

inline bool check(double len)
{
	double last=-inf;
	for (int i=0;i<n;++i)
	{
		double l=a[i]-len,r=a[i]+len;
		if (r+eps<last+D) return false;
		double x=max(l,last+D);
		last=x;
	}
	return true;
}

int main()
{
	freopen("B_large.in","r",stdin);
	freopen("B_large2.out","w",stdout);
	
	int T,test=1;
	for (scanf("%d",&T);test<=T;++test)
	{
		int C;
		scanf("%d%d",&C,&D);
		n=0;
		while (C--)
		{
			int P,V;
			scanf("%d%d",&P,&V);
			for (int i=0;i<V;++i)
				a[n++]=P;
		}
		sort(a,a+n);
		double l=0,r=inf;
		while (l+eps<r)
		{
			double mid=(l+r)/2;
			if (check(mid)) r=mid;
			else l=mid;
		}
		
		printf("Case #%d: %.2f000000\n",test,r);
	}
	
	return 0;
}
