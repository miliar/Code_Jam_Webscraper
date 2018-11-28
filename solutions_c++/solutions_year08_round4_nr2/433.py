#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <map>
#include <set>
#include <cctype>
#include <iostream>
#include <cassert>
#include <numeric>

using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;

#define ALL(a) (a).begin(),(a).end()
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define CLR(v,a) memset(v,a,sizeof(v))
#define PB push_back
#define MP make_pair
#define FI first
#define SE second

int n, m, A;

int area(int a, int b, int c, int d) {
	return abs(a*d-b*c);
}

int main()
{
	int t; scanf("%d", &t);
	REP(tC,t) {
		scanf("%d %d %d", &n,&m,&A);

		FOR(x1,0,n) FOR(y2,0,m) 
			FOR(x3,0,n) FOR(y3,0,m)
				if (area(x1-x3,0-y3,0-x3,y2-y3)==A) {
					printf("Case #%d: %d %d %d %d %d %d\n", tC+1, x1, 0, 0, y2, x3, y3);
					goto koniec;
				}
		printf("Case #%d: IMPOSSIBLE\n", tC+1);
		koniec:;
	}
	return 0;
}
