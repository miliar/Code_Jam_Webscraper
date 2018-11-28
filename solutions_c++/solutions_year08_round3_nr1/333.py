#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<algorithm>
#include<queue>
#include<map>
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

bool comp(int a,int b)
{
	return a>b;
}

int main()
{
	freopen("out.txt","w",stdout);
	int i,t,cs,p,k,n,freq[1005],now;
	long long ans;
	scanf("%d",&t);
	Foro(cs,t)
	{
		scanf("%d%d%d",&p,&k,&n);
		Foro(i,n)
			scanf("%d",&freq[i]);
		sort(freq,freq+n,comp);
		if(p*k<n)
		{
			printf("Case #%d: Impossible",cs+1);
			continue;
		}
		now=1;
		ans=(long long)(freq[0]*now);
		for(i=1;i<n;i++)
		{
			if(i%k==0)
				now++;
			ans+=(long long)(freq[i]*now);
		}
		printf("Case #%d: %lld\n",cs+1,ans);
	}
	return 0;
}