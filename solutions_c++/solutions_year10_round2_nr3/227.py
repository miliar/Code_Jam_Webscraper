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
#define MIN(a,b) ((a) < (b) ? (a) : (b)
#define ABS(X) ((X) < 0 ? (-(X)) : (X))
#define S(X) ((X)*(X))

typedef pair<int,int> PII;
typedef __int64 LL;

//int dr[]={0,-1,-1,-1,0,1,1,1};
//int dc[]={-1,-1,0,1,1,1,0,-1};

#define MOD 100003

int mark[502][502];
int dp[502][502];
LL ncr[504][504];

void gen()
{
	ncr[0][0]=1;
	int limncr = 500;
	int i,j;
	for(i=0;i<=limncr;i++)
		ncr[i][0]=1;

	for(i=1;i<=limncr;i++)
		for(j=0;j<=limncr;j++)
		{
			if(j>i) ncr[i][j]=0;
			else if(j==i || j==0) ncr[i][j]=1;
			else ncr[i][j] = (ncr[i-1][j-1] + ncr[i-1][j])%MOD;
		}
}

int DP(int pos, int num)
{
	if(pos==1) return 1;

	if(mark[pos][num]) return dp[pos][num];

	mark[pos][num]=1;

	for(int i=1;i<pos;i++)
	{
		if(num-pos >= pos-i)
			dp[pos][num] = (dp[pos][num] + DP(i,pos)*ncr[num-pos-1][pos-i-1])%MOD;
	}

	return dp[pos][num];
}

int main()
{
//	freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
//	freopen("C-small-attempt1.in","r",stdin);freopen("C-small-attempt1.out","w",stdout);
//	freopen("C-small-attempt2.in","r",stdin);freopen("C-small-attempt2.out","w",stdout);
	freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);
	
	int T,ks,n,way,i;

	gen();

	scanf("%d",&T);
	for(ks=1;ks<=T;ks++)
	{
		scanf("%d",&n);

		way=0;
		for(i=1;i<n;i++)
			way=(way + DP(i,n))%MOD;

		printf("Case #%d: %d\n",ks,way);
	}

	return 0;
}
