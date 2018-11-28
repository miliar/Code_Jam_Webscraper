#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
const int maxp=1000000;
void PrimeGen(int p[],int &n)
{
	static bool q[maxp+1]={0};
	for(int i=2;i*i<=maxp;i++)
		if(!q[i]) for(int j=i*2;j<=maxp;j+=i) q[j]=true;
	n=0;
	for(int i=2;i<=maxp;i++) if(!q[i]) p[n++]=i;
}
int prime[maxp],pn;
int solve(long long n)
{
	if(n==1) return 0;
	int m=sqrt(n);
	int ans=1;
	//printf("n=%I64d m=%d\n",n,m);
	for(int i=0;i<pn&&prime[i]<=m;i++)
	{
		int p=(int)(log((long double)n)/log((long double)prime[i])+1e-9);
		ans+=p-1;
		//printf("%d %d\n",prime[i],p);
	}
	return ans;
}
int main()
{
	PrimeGen(prime,pn);
	int t;
	scanf("%d",&t);
	for(int cs=1;cs<=t;cs++)
	{
		long long n;
		scanf("%I64d",&n);
		printf("Case #%d: %d\n",cs,solve(n));
	}
	return 0;
}
