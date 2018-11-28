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
#define adebug2d(a,n,m) FOR(i,0,n) { FOR(j,0,m) { cout<<a[i][j]<<" ";} cout<<endl;}
#define vdebug(v) REPSZ(i,v) cout<<#v<<"["<<i<<"] = "<<v[i]<<endl;
#define selfx(x,f,a) x = f(x,a)


typedef pair<int,int> pii;
typedef long long i64;
typedef vector<int> VI; typedef vector< vector<int> > VVI;
typedef vector<string> VS;

const int inf = 1<<25;
const double eps = 1e-9;

const int modulo = 100003;
const int MAXN = 600;
i64 aC[MAXN][MAXN];
i64 C(i64 n,i64 k)
{
	if(k<0 || k>n) return 0;
	return aC[n][k];
}

i64 memo[MAXN][MAXN];

i64 f(int n,int k)
{
	if(n<k+1)
		return 0;
	if(n == 2)
	{
		if(k == 1) return 1;
		return 0;
	}
	if(n<=2) return 0;
	if(k == 1)
		return 1;
	i64& ret = memo[n][k];
	if(ret!=-1)
		return ret;
	ret = 0;
	for(int i = 1; i < k; ++i)
	{
		ret+=f(k,i)*C(n-k-1,k-i-1);
		ret%=modulo;
	}
	return ret;
}

int main()
{
	freopen ("C-large.in","r",stdin);
	//freopen ("in.txt","r",stdin);
	freopen ("C-large.out","w",stdout);

	int tt;
	
	mset(aC,0);
	FOR(i,0,MAXN)
		aC[i][0] = 1;
	FOR(i,1,MAXN)
		FORE(j,1,i)
		aC[i][j] = (aC[i-1][j-1]+aC[i-1][j])%modulo;
	
	cin>>tt;
	for(int cas = 1;cas<=tt;++cas)
	{
		int ans = 0;
		int n;
		mset(memo,-1);
		cin>>n;
		FOR(i,1,n)
		{
			ans+=f(n,i);
			ans%=modulo;
		}
		printf("Case #%d: %d\n",cas,ans);
	}

	return 0;
}

