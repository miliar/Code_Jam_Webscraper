#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<algorithm>
#include<queue>
#include<list>
#include<vector>
#include<string>
using namespace std;	

#define sq(a) ((a)*(a))
#define pb(a) push_back(a)
#define Min(a,b) (((a)<(b))?(a):(b))
#define Max(a,b) (((a)>(b))?(a):(b))
#define eps 1e-9
#define inf 1<<29
#define pye 2.*acos(0.)
#define SZ(v) ((int)(v).size())
#define For(i,a,b) for(i=(a);i<(b);++i)
#define Fore(i,a,b) for(i=(a);i<=(b);++i)
#define Forc(i,v) For(i,0,SZ(v))
#define Foro(i,a) For(i,0,a)
#define mod 1000000007
int n,is[1005];
long long num[1005],a[1005];

int makei(int pos)
{
	int i;
	if(is[pos])
		return is[pos];
	For(i,pos+1,n)
		if(num[i]>num[pos])
			is[pos]=(is[pos]+makei(i))%mod;
	is[pos]=(is[pos]+1)%mod;
	return is[pos];
}

int main()
{
	freopen("out12.txt","w",stdout);
	int i,m,t,cs,ans;
	long long x,y,z;
	scanf("%d",&t);
	Foro(cs,t)
	{
		scanf("%d%d%lld%lld%lld",&n,&m,&x,&y,&z);
		Foro(i,m)
			scanf("%lld",&a[i]);
		Foro(i,n)
		{
			num[i]=a[i%m],is[i]=0;
			a[i%m]=(x * a[i%m] + y* (i + 1))%z;
		}
		Foro(i,n)
			is[i]=makei(i);
		ans=0;
		Foro(i,n)
			ans=(ans+is[i])%mod;
		printf("Case #%d: %d\n",cs+1,ans);
	}
	return 0;
}