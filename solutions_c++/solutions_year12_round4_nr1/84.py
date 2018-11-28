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

const int N = 10000;
int t, n, len;
int d[N], l[N], ran[N];
vector<int> qu;

int bsearch(int val) {
	int l = 0, r = SIZE(qu) - 1, m;
	while(l < r) {
		m = (l + r) / 2;
		if(ran[qu[m]] < val) {
			l = m + 1;
		} else {
			r = m - 1;
		}
	}
	if(l < SIZE(qu) && ran[qu[l]] < val) l++;
	return l;
}

int main() {
	scanf("%d", &t);
	REP(xx, t) {
		scanf("%d", &n);
		bool good =  0;
		qu.clear();
		REP(i, n) {
			scanf("%d%d", &d[i], &l[i]);
		}

		scanf("%d", &len);
		ran[0] = 2 * d[0];
		qu.PB(0);
		if(ran[0] >= len) {
			good = 1;
		} else FOR(i, 1, n) {
			int v = bsearch(d[i]);
			if(v == SIZE(qu)) break;
			ran[i] = min(d[i] + l[i], 2 * d[i] - d[qu[v]]);
			if(ran[i] >= len) {
				good = 1;
				break;
			}
			if(qu.empty() || ran[i] > ran[qu.back()]) qu.PB(i);
		}
		REP(i, n) DEB("%d - > %d\n",i + 1, ran[i]);
		printf("Case #%d: ", xx + 1);
		if(good) {
			printf("YES\n");
		} else {
			printf("NO\n");
		}

	}

	return 0;
}
