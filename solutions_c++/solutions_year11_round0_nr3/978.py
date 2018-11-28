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
		int check = 0;
		int sum = 0;
		int min = 1000001;
		REP(n, N){
			int C;
			scanf("%d ", &C);
			check ^= C;
			sum += C;
			min = std::min(min, C);
		}
		if(check || N <= 1) printf("Case #%d: NO\n", i + 1);
		else printf("Case #%d: %d\n", i + 1, sum - min);
	}
	return 0;
}
