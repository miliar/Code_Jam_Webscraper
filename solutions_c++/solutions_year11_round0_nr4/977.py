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
#define REP(i,b)	FOR(i,0,b)
#define ALL(c)		(c).begin(),(c).end()
#define LET(v,x)	typeof(x) v = x
#define FOREACH(it,c)	for(LET(it,(c).begin());it!=(c).end();++it)

int main(){
	int T;
	scanf("%d ", &T);
	REP(i, T){
		int N;
		scanf("%d ", &N);
		int x = 0;
		REP(n, N){
			int C;
			scanf("%d ", &C);
			x += C != n + 1;
		}
		printf("Case #%d: %d.000000\n", i + 1, x);
	}
	return 0;
}
