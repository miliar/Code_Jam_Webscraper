#include<cstdio>
#include<algorithm>
using namespace std;
typedef long long ll;
#define N 1000010
int P[N],L;bool A[N];
int getP(int a,ll b)
{
	ll t=1;
	for(int i=1;;i++)
	{
		t*=a;
		if(t>b/a)return i;
	}
}
int main()
{
	int _;scanf("%d",&_);
	for(int i=2;i*i<N;i++)
		if(!A[i])for(int j=i*i;j<N;j+=i)A[j]=1;
	for(int i=2;i<N;i++)
		if(!A[i])P[L++]=i;
	for(int __=1;__<=_;__++)
	{
		ll n;scanf("%lld",&n);
		ll S=1;
		for(int i=0;i<L;i++)
		{
			if(P[i]>n)break;
			int F=getP(P[i],n);
			if(F==1)break;
			S+=F-1;
		}
		printf("Case #%d: %lld\n",__,n==1?0LL:S);
	}
	return 0;
}

