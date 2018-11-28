#pragma warning(disable:4786)
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<functional>
#include<string>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<utility>
#include<fstream>
#include<sstream>
#include<math.h>
#include<stack>
using namespace std;

#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define ABS(X) ((X) < 0 ? (-(X)) : (X))
#define S(X) ((X)*(X))

typedef pair<int,int> PII;
typedef __int64 LL;

//int dr[]={0,-1,-1,-1,0,1,1,1};
//int dc[]={-1,-1,0,1,1,1,0,-1};

#define INF 1000000000

int X;
int cost[12][1<<11];
int dp[12][1<<11][12];
int mark[12][1<<11][12];
int M[1<<11];

int DP(int level,int match,int miss)
{
	if(mark[level][match][miss]==X) return dp[level][match][miss];
	if(level==0)
	{
		if(miss > M[match]) return INF;
		return 0;
	}

	mark[level][match][miss]=X;

	int &ret = dp[level][match][miss];

	int x=DP(level-1,match*2,miss)+cost[level][match]+DP(level-1,match*2+1,miss);
	int y=DP(level-1,match*2,miss+1)+DP(level-1,match*2+1,miss+1);

	ret = MIN(x,y);

	if(ret > INF) ret = INF;

	return ret;


}

int main()
{
//	freopen("B-small-attempt0.in","r",stdin);freopen("B-small-attempt0.out","w",stdout);
//	freopen("B-small-attempt1.in","r",stdin);freopen("B-small-attempt1.out","w",stdout);
//	freopen("B-small-attempt2.in","r",stdin);freopen("B-small-attempt2.out","w",stdout);
	freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);
	
	int T,ks;
	int P,lim,temp;
	int i,j,ans;

	scanf("%d",&T);
	for(ks=1;ks<=T;ks++)
	{
		scanf("%d",&P);
		lim=(1<<P)-1;

		for(i=0;i<=lim;i++) scanf("%d",&M[i]);

		temp=(1<<P);
		for(i=1;i<=P;i++)
		{
			temp/=2;
			for(j=0;j<temp;j++)
				scanf("%d",&cost[i][j]);
		}

		X++;
		printf("Case #%d: ",ks);
		ans = DP(P,0,0);
		printf("%d\n",ans);
	}

	return 0;
}