#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
#include <queue>
#include <algorithm>
#include <map>
#include <stack>
#include <vector>
#include <stdlib.h>
#include <cmath>
#include <fstream>
using namespace std;
#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)
#define INF 0x7f7f7f7f
#define INFL (1LL<<60)
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;
long long num[2000000];
bool cmp(const long long &a,const long long &b)
{
	return a>b;
}
int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int T;
	scanf("%d",&T);
	
	int cas=0;
	while(T--)
	{
		long long L,t,N,C;
		long long tot=0;
		scanf("%lld%lld%lld%lld",&L,&t,&N,&C);
		for(int i=1;i<=C;i++)
		{
			scanf("%d",&num[i]);
			tot+=num[i];
		}
		for(int i=C+1;i<=N;i++)
		{
			num[i] = num[i-C];
			tot+=num[i];
		}
		long long cnt = 0;
		int chose = N+1;
		for(int i=1;i<=N;i++)
		{
			cnt+=num[i];
			if(cnt*2 >= t)
			{
				chose = i;
				break;
			}
		}
		printf("Case #%d: ",++cas);
		if(chose!=N+1)
		{
			long long ans = t;
			
			cnt -= t/2;
			num[chose]=cnt;
			int i,j;
			sort(num+chose,num+N+1,cmp);
			for(i=chose,j=0;i<=N&&j<L;i++,j++)
			{
				ans+=num[i];
			}
			for(;i<=N;i++) ans+=num[i]*2;
			printf("%lld\n",ans);
		}
		else printf("%lld\n",tot*2);
	}
    return 0;
}
