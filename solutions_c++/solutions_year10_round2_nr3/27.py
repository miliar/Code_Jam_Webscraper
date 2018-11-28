#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <sstream>
#include <string>
#include <set>
#include <map>
#include <cmath>
#include <deque>
#include <algorithm>
#include <complex>
using namespace std;


typedef long long LL;
typedef pair<int,int> PII;

#define pb push_back
#define mp make_pair
#define sz size()
#define ALL(a) (a).begin(),(a).end()
#define RALL(a) (a).rbegin(),(a).rend()
#define FOR(i,a,b) for(int i=(a),_b(b); i<_b; ++i)
#define RFOR(i,a,b) for(int i=(a)-1,_b(b); i>=_b; --i)
#define CLR(a,v) memset((a),(v),sizeof(a))
#define CPY(a,b) memcpy((a),(b),sizeof(a))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define ABS(a) ((a)<(0)?-(a):(a))
#define HAS(x,k) ((x).find(k)!=(x).end())
#define sqr(a) ((a)*(a))

#define PREV(x) ((x)&((x)-1))
#define NEXT(x) (((x)<<1) - PREV(x))

LL  mod=100003;
LL dp[512][512];
LL _C[512][512];
LL C(int a, int b)
{
	if (a<0) return 0;
	if (b<0) return 0;
	if (b>a) return 0;
	if (b<0) return 0;
	if (_C[a][b]!=-1) return _C[a][b];
	if (a==0 && b==0) return 1;
	return _C[a][b]=(C(a-1,b-1)+C(a-1,b))%mod;
}

LL rec(int n, int k)
{
	if (k==1) return 1;
	LL &r=dp[n][k];
	if (r!=-1) return r;
	
	r=0;
	FOR(i,1,k)
	{
		r+=C(n-k-1, k-i-1)*rec(k,i);
		r%=mod;
	}
	return r;
}


int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	CLR(_C,-1);
	CLR(dp,-1);
	int t; scanf("%d",&t);
	int tc=0;
	while(t--)
	{
		++tc;
		int n;
		scanf("%d",&n);
		LL sum=0;
		FOR(i,2,n+1) sum=(sum+rec(n,i-1))%mod;
		printf("Case #%d: %d\n",tc,(int)sum);
	}


	
	
	return 0;
}