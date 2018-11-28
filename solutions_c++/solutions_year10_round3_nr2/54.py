#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
using namespace std;

long long L,P,C;

long long calc(long long l,long long p,long long c)
{
	long long ret=0;
	while(l*c<p) l=l*c,ret++;
	return ret;
}

long long solve()
{
	long long ret=0;
	long long n=calc(L,P,C);
	while(n>0) n/=2,ret++;
	return ret;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("b.out","w",stdout);
	long long i,T;
	scanf("%lld",&T);
	for(i=1;i<=T;i++)
	{
		scanf("%lld%lld%lld",&L,&P,&C);
		printf("Case #%lld: ",i);
		printf("%lld\n",solve());
	}
	return 0;
}