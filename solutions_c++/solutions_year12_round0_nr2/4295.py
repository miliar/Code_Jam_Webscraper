#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
//#define DEBUG
#ifdef DEBUG
	#define DEB printf
	#define FF fflush(stdout)
#else
	#define DEB(...) 
	#define FF
#endif
#define REP(x, n) for(int x = 0; x < (n); x++)
#define FOR(x, b, e) for(int x = (b); x <= (e); x++)
#define FORD(x, u, d) for(int x = (u); x >= (d); x--)
#define VAR(x, a) __typeof(a) x = (a)
#define FOREACH(x, c) for(VAR(x, (c).begin()); x != (c).end(); x++)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define INF 1000000
#define PB push_back
#define MP make_pair
#define ST first
#define ND second
using namespace std;
typedef vector<int> VI;
typedef pair<int, int> PII;
typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;

const int N = 100;

int t, n, s, p, sc, res;

int main() {
	scanf("%d", &t);
	REP(xx, t) {
		res = 0;
		scanf("%d%d%d", &n, &s, &p);
		REP(i, n) {
			scanf("%d", &sc);
			if((sc + 2) / 3 >= p) {
				res++;
			} else if(s > 0 && (sc + 4) / 3 >= p && 2 <= sc && sc <= 28) {
				s--;
				res++;
			}

		}
		printf("Case #%d: %d\n", xx + 1, res);
	}
	return 0;
}


