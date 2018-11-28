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

int arr[10000][2];
int tested[10000];
bool test(int N, int D, int pos, int crr){
	int able = arr[crr][0] * 2 - pos;
	if(able >= D) return true;
	if(tested[crr] >= 0 && pos >= tested[crr]) return false;
	tested[crr] = pos;
	FOR(i,crr+1,N){
		if(arr[i][0] > able) break;
		int sz = min(arr[i][0] - arr[crr][0], arr[i][1]);
		if(test(N, D, arr[i][0] - sz, i)) return true;
	}
	
	return false;
}

int main(){
	GETi(TTT);
	REP1(ttt, TTT){
		GETi(N);
		REP(i,N){
			GETi(d);
			GETi(L);
			arr[i][0] = d;
			arr[i][1] = L;
			tested[i] = -1;
		}
		GETi(D);
		printf("Case #%d: %s\n", ttt, test(N, D, 0, 0) ? "YES" : "NO");
	}
	return 0;
}
