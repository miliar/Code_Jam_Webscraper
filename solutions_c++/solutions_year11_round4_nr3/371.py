#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <set>
#include <map>
#include <string>


#define M 1

//struct D{int s,e;
//	bool friend operator < (const D &p,const D &q)
//	{
//		if(p.s!=q.s) return p.s<q.s;
//		return p.e<q.e;
//	}
//};


int v[1000001],p;
__int64 prime[1000001];
int main()
{
	int i,j,t,T=0;
	__int64 n,max,min,buf;

	freopen("input.txt","r",stdin);
	freopen("output2.txt","w",stdout);

	for(i=2;i<=1000000;++i) if(!v[i])
	{
		prime[++p]=i;
		for(j=i*2;j<=1000000;j+=i) v[j]=1;
	}
	prime[++p]=99999999;

	for(scanf("%d",&t);t--;)
	{
		scanf("%I64d",&n);

		max=1;
		min=0;
		if(n==1) min=1;

		for(i=1;prime[i]*prime[i]<=n;++i)
		{
			j=1; buf=prime[i];
			while(buf*prime[i]<=n) buf*=prime[i], ++j;
			max+=j;
			min+=1;
		}
		printf("Case #%d: %I64d\n",++T,max-min);
	}
	return 0;
}
