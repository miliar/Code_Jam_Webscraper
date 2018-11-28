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

int least(int p){
	int ret = 100;
	if(!(p %  4)) ret /=  4; else if(!(p % 2)) ret /= 2;
	if(!(p % 25)) ret /= 25; else if(!(p % 5)) ret /= 5;
	return ret;
}

int main(){
	int T;
	scanf("%d ", &T);
	REP1(ttt, T){
		ll N;
		int Pd, Pg;
		scanf("%lld %d %d ", &N, &Pd, &Pg);
		printf("Case #%d: %s\n", ttt, ((least(Pd) > N) || (Pd > 0 && Pg <= 0) || (Pd < 100 && Pg >= 100)) ? "Broken" : "Possible");
	}
	return 0;
}
