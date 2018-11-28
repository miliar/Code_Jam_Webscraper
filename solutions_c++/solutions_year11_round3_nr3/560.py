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
	if (!a || !b) return 0;
	while(a != b) if(a > b) a -= b; else b -= a;
	return a;
}

ll ot[10001];
int main(){
	int T;
	scanf("%d ", &T);
	REP1(ttt, T){
		int N;
		ll L, H;
		scanf("%d %lld %lld ", &N, &L, &H);
		REP(i,N) scanf("%lld ", ot + i);
		bool ok = false;
		for(ll f = L; f <= H; ++f){
			ok = true;
			REP(i,N){
				ll g = gcd(f, ot[i]);
				if(g != f && g != ot[i]){
					ok = false;
					break;
				}
			}
			if(ok){
				printf("Case #%d: %lld\n", ttt, f);
				break;
			}
		}
		if(!ok) printf("Case #%d: NO\n", ttt);
	}
	return 0;
}
