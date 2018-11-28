#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <tr1/unordered_map>
#include <tr1/unordered_set>
#include <vector>
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

const int INF = 1000000001;
const int N = 1000;

int t, n, w, l;

int r[N], tab[N];

bool comp(int a, int b) {
	return r[a] < r[b];
}

struct point {
	int x, y;
	point() {}
	point(int nx, int ny) : x(nx), y(ny) {}
};

point pos[N], cpos;

int main() {
	scanf("%d", &t);
	REP(xx, t) {
		scanf("%d%d%d", &n, &w, &l);
		REP(i, n) {
			scanf("%d", &r[i]);
			tab[i] = i;
		}
		sort(tab, tab + n, comp);
		cpos = point(0, 0);
		REP(i, n) {
			if(i > 1 && (cpos.x + 2 * r[tab[i]] > w)) {
				cpos = point(0, pos[tab[i - 1]].y + r[tab[i - 1]]);
			}
			if(cpos.y == 0) {
				pos[tab[i]] = point(cpos.x + r[tab[i]], 0);
			} else {
				pos[tab[i]] = point(cpos.x + r[tab[i]], cpos.y + r[tab[i]]);
			}
			if(cpos.x == 0) {
				pos[tab[i]].x -= r[tab[i]];
				cpos.x += r[tab[i]];
			} else {
				cpos.x += 2 * r[tab[i]];
			}
			DEB("cpos = (%d, %d)\n", cpos.x, cpos.y);
		}

		printf("Case #%d: ", xx + 1);
		REP(i, n) printf("%d %d ", pos[i].x, pos[i].y);
		printf("\n");
	}
	return 0;
}
