#include <iostream>
#include <cstdio>
#include <ctime>
#include <cstdlib>
#include <cctype>
#include <algorithm>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
using namespace std;
typedef vector<int> VI;
typedef long long LL;
#define FOR(x,b,e) for (int x = (b); x < (e); ++x)
#define FORD(x,b,e) for (int x = (b) x >= (e); --x)
#define REP(x,n) for (int x = 0; x < (n); ++x)
#define VAR(v,n) __typeof(n) v = (n)
#define ALL(c) c.begin(), c.end()
#define SIZE(x) (int)x.size()
#define FOREACH(i,c) for (VAR(i,c.begin()); i != c.end(); ++i)
#define PB push_back
#define ST first
#define ND second
int ab(int x) { return x >= 0 ? x : -x; }
int main() {
	int c;
	scanf("%d",&c); 
	FOR(a,1,c+1) {
		int N, M, A;
		scanf("%d%d%d",&N, &M, &A);
		int f = 0;
		printf("Case #%d: ",a);
		REP(x1,N+1) REP(x2,N+1) REP(y1,M+1) REP(y2,M+1) {
			if (f != 1 && ab((x1*y2-x2*y1)) == A)  { f = 1; printf("%d %d %d %d %d %d\n",0,0,x1,y1,x2,y2); } }
			if (f == 0) printf("IMPOSSIBLE\n");
	}
	return 0;
}
