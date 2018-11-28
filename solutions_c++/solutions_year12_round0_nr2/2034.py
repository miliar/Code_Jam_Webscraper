#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <iostream>
#include <sstream>
#include <memory>
#include <complex>
using namespace std;

static const double EPS = 1e-5;
typedef long long ll;

#define FOR(i,a,b)	for(int i=(a);i<(int)(b);++i)
#define FORe(i,a,b)	for(int i=(a);i<=(int)(b);++i)
#define REP(i,b)	FOR(i,0,b)
#define REP1(i,b)	FORe(i,1,b)
#define ALL(c)		(c).begin(),(c).end()
#define LET(v,x)	typeof(x) v = x
#define FROMTO(it,b,e)	for(LET(it,(b));it!=(e);++it)
#define FOREACH(it,c)	FROMTO(it,(c).begin(),(c).end())

ll gcd(ll a, ll b){
	if (a && b) for(ll x; b; b = x){
		x = a % b;
		a = b;
	}
	return a;
}
ll gcd(ll a[], int n){
	return n > 0 ? accumulate(a + 1, a + n, a[0], (ll(*)(ll,ll))gcd) : 0LL;
}

ll lcm(ll a, ll b){
	return (a && b) ? a / gcd(a, b) * b : 0LL;
}
ll lcm(ll a[], int n){
	return n > 0 ? accumulate(a + 1, a + n, a[0], (ll(*)(ll,ll))lcm) : 0LL;
}

#define SCAN(p,f)	scanf("%" #f " ",p)
#define GET(t,x,f)	t x;SCAN(&x,f)
#define GETi(x)		GET(int,x,d)
#define GETl(x)		GET(ll,x,lld)
#define GETc(x)		GET(char,x,c)
#define GETf(x)		GET(float,x,f)
#define GETd(x)		GET(double,x,lf)

#define NEVER_SURPRIZE__OVER_P				0
#define NEVER_SURPRIZE__UNDER_P				1
#define SURPRIZE_ABLE__OVER_P_ALWAYS		2
#define SURPRIZE_ABLE__OVER_P_IF_SURPRIZE	3
#define SURPRIZE_ABLE__UNDER_P_ALWAYS		4

int main(){
	GETi(TTT);
	REP1(ttt, TTT){
		GETi(N);
		GETi(S);
		GETi(P);
		int stats[5] = {0};
		REP(i, N){
			GETi(t);
			bool r = 2 <= t && t <= 28;
			bool n = P <= t / 3 + (t % 3 > 0);
			bool s = P <= t / 3 + (t % 3 > 1) + 1;
			stats[
				r ? n ? SURPRIZE_ABLE__OVER_P_ALWAYS
				      : s ? SURPRIZE_ABLE__OVER_P_IF_SURPRIZE
				          : SURPRIZE_ABLE__UNDER_P_ALWAYS
				  : n ? NEVER_SURPRIZE__OVER_P
				      : NEVER_SURPRIZE__UNDER_P
			]++;
		}
		printf("Case #%d: %d\n", ttt,
			stats[NEVER_SURPRIZE__OVER_P] + 
			stats[SURPRIZE_ABLE__OVER_P_ALWAYS] + 
			min(S, stats[SURPRIZE_ABLE__OVER_P_IF_SURPRIZE])
		);
	}
	return 0;
}
