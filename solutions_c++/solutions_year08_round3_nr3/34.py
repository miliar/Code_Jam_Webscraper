#include <stdio.h>
#include <assert.h>
#include <string.h>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

#define FOR(i,a,b) for (int i=(a),_b=(b); i<=_b; i++)
#define FORD(i,a,b) for (int i=(a),_b=(b); i>=_b; i--)
#define REP(i,n) for (int i=0,_n=(n); i<_n; i++)
#define FOREACH(it,arr) for (__typeof((arr).begin()) it=(arr).begin(); it!=(arr).end(); it++)
#define FOREACHD(it,arr) for (__typeof((arr).rbegin()) it=(arr).rbegin(); it!=(arr).rend(); it++)

#define MAXN 1012

long long mod = 1000000007;
long long nTC,n,m,X,Y,Z,a[MAXN],A[MAXN];
long long memo[MAXN][MAXN];

long long rec(int idx, int prev){
	if (idx==n) return prev==-1? 0 : 1;
	long long &ret = memo[idx][prev+1];
	if (ret!=-1) return ret;

	ret = rec(idx+1,prev);
	if (prev==-1 || a[prev] < a[idx])
		ret += rec(idx+1,idx);
	ret %= mod;
	return ret;
}

int main(){
	scanf("%lld",&nTC);
	FOR(TC,1,nTC){
		scanf("%lld %lld %lld %lld %lld",&n,&m,&X,&Y,&Z);
		REP(i,m) scanf("%lld",&A[i]);
		REP(i,n){
			a[i] = A[i%m];
			A[i%m] = (X * A[i%m] + Y * (i + 1)) % Z;
		}
		long long res = 0;
		memset(memo,-1,sizeof(memo));
		REP(i,n){
			long long t = rec(i+1,i);
			res += t;
			res %= mod;
		}
		printf("Case #%d: %lld\n",TC,res%mod);
	}
}
