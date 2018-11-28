#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cctype>
using namespace std;

#define FOR(i,a,b) for(int i=int(a); i<int(b); ++i)
#define FORD(i,a,b) for(int i=int(a-1); i>=int(b); --i)
#define FORE(i,q) for(typeof((q).begin()) i=(q).begin(); i!=(q).end(); ++i)
typedef long long LG;

LG N, M, A;

LG angle(pair<int, int> a, pair<int, int> b, pair<int, int> c) {
        return  LG(a.first - b.first) * LG(c.second - b.second) -
                LG(c.first - b.first) * LG(a.second - b.second);
}

int main() {
	int T;
	scanf("%d", &T);
	for(int z=1; z<=T; ++z) {
		scanf("%lld%lld%lld", &N, &M, &A);
			FOR(x2,0,N+1) FOR(y2,0,M+1)
			FOR(x3,0,N+1) FOR(y3,0,M+1) {
				if(abs(angle(make_pair(0, 0),
				             make_pair(x2, y2),
				             make_pair(x3, y3))) == A) {
			printf("Case #%d: %lld %lld %lld %lld %lld %lld\n", z,
			0LL, 0LL, LG(x2), LG(y2), LG(x3), LG(y3));
					goto ende;
				}
			}
			printf("Case #%d: IMPOSSIBLE\n", z);
			ende:;
	}
	return 0;
}
