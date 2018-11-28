#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>
#include <cctype>
#include <assert.h>

using namespace std;
typedef long long ll;

const double PI=acos(-1.0);
const double eps=1e-11;

#define dump(x) cerr<<#x<<" = "<<(x)<<endl;
#define foreach(c,itr) for (__typeof( (c).begin() ) itr=(c).begin();itr!=(c).end() ;itr++ )


int countbit(int n) {return (n==0)?0:1+countbit(n&(n-1));}
int lowbit(int n) {return n&(n^(n-1));}
string toString(ll v) { ostringstream sout;sout<<v;return sout.str();}
string toString(int v) { ostringstream sout;sout<<v;return sout.str();}
int Rand16(){return rand();}
int Rand32(){return rand()*rand();}
double DRand(){return (double)rand()/RAND_MAX;}
int RandRange(int f,int r){return f+(int)(DRand()*(r-f)+0.5);}







const int MOD =100003;
const int MAX = 50+5;

int T,cas;
int n;
int dp[MAX][MAX];
int C[MAX][MAX];

int solve(int v,int at)
{
	if (dp[v][at]!=-1) return dp[v][at];
	int &ret=dp[v][at];
	if (at==1)
		return ret=1;
	ret=0;
	int pat;
	for (pat=1;pat<at;pat++)
		if (at-pat<=v-at)
			ret=(ret+solve(at,pat)*C[v-at-1][at-pat-1])%MOD;
	//printf("dp[%d][%d]=%d\n",v,at,ret);
	return ret;
}

int main()
{
	int i,j;

	freopen("C-small-attempt0.in","r",stdin);
	freopen("out","w",stdout);

	for (i=0;i<MAX;i++)
		for (j=0;j<=i;j++)
			if (j==0 || j==i)
				C[i][j]=1;
			else
				C[i][j]=(C[i-1][j]+C[i-1][j-1])%MOD;
	memset(dp,-1,sizeof(dp));
	cas=0;
	scanf("%d",&T);
	while (T--)
	{
		cas++;
		scanf("%d",&n);		
		int ans=0;
		for (i=1;i<=n;i++)
			ans=(ans+solve(n,i))%MOD;
		printf("Case #%d: %d\n",cas,ans);
	}
	return 0;
}
