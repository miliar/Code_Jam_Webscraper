#include <cstdio>
#include <cmath>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <utility>
#include <stack>
#include <queue>
#include <map>

#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define pi 2*acos(0.0)
#define eps 1e-9
#define PII pair<int,int> 
#define PDD pair<double,double>
#define LL long long
#define INF 1000000000

using namespace std;

int T,N,S,P,x;
int tot[111];
int dp[111][111];

int solve(int surp, int now)
{
	if(surp<0) return -INF;
	if(now==N && !surp) return 0;
	if(now==N && surp) return -INF;
	if(dp[surp][now]!=-1) return dp[surp][now];
	
	int &ret = dp[surp][now] = 0;
	for(int a = 0;a<=10;a++)
		for(int b = 0;b<=10;b++)
			for(int c = 0;c<=10;c++)
			{
				int maxDiff = max(max(abs(a-b),abs(b-c)),abs(a-c));
				if(maxDiff>2) continue;
				if(a+b+c!=tot[now]) continue;
				
				int skor = 0;
				if(a>=P || b>=P || c>=P) skor = 1;
				if(maxDiff==2) ret=max(ret,skor+solve(surp-1,now+1));	
					else ret=max(ret,skor+solve(surp,now+1));
			}
	return ret;
}

int main()
{
	scanf("%d",&T);
	for(int i = 1;i<=T;i++)
	{
		scanf("%d %d %d",&N,&S,&P);
		for(x=0;x<N;x++) scanf("%d",&tot[x]);
		
		memset(dp,-1,sizeof(dp));
		printf("Case #%d: %d\n",i,solve(S,0));
	}
	return 0;
}

