#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <numeric>
#include <cmath>
using namespace std;

typedef vector <int > VI;
typedef vector < VI > VVI;
typedef long long LL;
typedef vector < LL > VLL;
typedef vector < double > VD;
typedef vector < string > VS;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef istringstream ISS;

#define REP(i,n) for (int i(0),_n(n); i < _n; ++i)
#define FOR(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define FORD(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define FOREACH(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define ALL(x) (x).begin(),(x).end()
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair((a),(b))
#define ST first
#define ND second
#define SIZE(x) (int)x.size()
#define debug if(1)printf

#define MAXN 100001

LL x[MAXN];
LL y[MAXN];
int n, A, B, C, D, xx0, yy0, M;

int main() {
	int ncaso;
	scanf(" %d", &ncaso);
	FOR(icaso, 1, ncaso) {
		printf("Case #%d: ", icaso);
		scanf(" %d %d %d %d %d %d %d %d", &n, &A, &B, &C, &D, &xx0, &yy0, &M);
		x[0]=xx0; y[0]=yy0;
		FOR (i, 1, n-1) {
			x[i]=((LL)A*x[i-1]+B)%M;
			y[i]=((LL)C*y[i-1]+D)%M;
		}
		int res=0;
		FOR(i, 0, n-1) {
			FOR (j, i+1, n-1) {
				FOR (k, j+1, n-1) {
					LL xt=x[i]+x[j]+x[k];
					LL yt=y[i]+y[j]+y[k];
					if (xt%3==0 && yt%3==0) res++;
				}
			}
		}
		printf("%d\n", res);			
		
	}

	return 0;
}
