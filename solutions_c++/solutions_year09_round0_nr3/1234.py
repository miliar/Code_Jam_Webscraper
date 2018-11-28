#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <map>
#include <queue>
#include <sstream>
#include <numeric>
#include <functional>
#include <set>
#include <cmath>
#include <stack>
using namespace std;

#pragma comment(linker,"/stack:16000000")

#define ALL(v) v.begin(),v.end()
#define SZ(v) v.size()
#define mset(A,x) memset((A),(x),sizeof(A))
#define FOR(i,start,N) for(int i=start;i<N;++i)
#define FORSZ(i,start,v) FOR(i,start,SZ(v))
#define REPSZ(i,v) FORSZ(i,0,v)
#define FORE(i,start,N) FOR(i,start,N+1)
#define make_unique(v) v.resize(unique(ALL(v))-v.begin())
#define debug(x) cout<<#x<<" = "<<x<<endl;
#define adebug(A,N) FOR(i,0,N) cout<<#A<<"["<<i<<"] = "<<A[i]<<endl;
#define vdebug(v) REPSZ(i,v) cout<<#v<<"["<<i<<"] = "<<v[i]<<endl;
#define selfx(x,f,a) x = f(x,a)


typedef pair<int,int> pii;
typedef long long i64;
typedef vector<int> VI; typedef vector< vector<int> > VVI;
typedef vector<string> VS;

const int inf = 1<<25;
const double eps = 1e-9;

const int mod = 10000;

#define MAXN 1000

#define MAXM 30

int main()
{
//freopen ("input.txt","r",stdin);
//freopen ("in.txt","r",stdin);
freopen ("output.txt","w",stdout);

	int tt;
	cin>>tt;
	scanf("\n");

	char s[MAXN];
	int dp[MAXN][MAXM];
	string pat = "welcome to code jam";

	

	int m = pat.size();
	

	for(int cas = 1;cas<=tt;++cas)
	{
		gets(s);
		int ans = 0;
		mset(dp,0);
		FOR(i,0,MAXN)
			dp[i][0] = 1;

		int n = strlen(s);

		FORE(i,1,n)
			FORE(j,1,m)
		{
			dp[i][j] = dp[i-1][j];
			if(s[i-1]==pat[j-1])
			{
				dp[i][j] +=dp[i-1][j-1];
				dp[i][j]%=mod;
			}
		}
		
		printf("Case #%d: %04d\n",cas,dp[n][m]);
	}

	return 0;
}

