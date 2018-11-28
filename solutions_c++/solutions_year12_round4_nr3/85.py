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

const int MAX = 1000000000;

const int N = 2001;

int t, n;
int h[N + 1], line[N];
VI looking[N];

int main() {
	scanf("%d", &t);
	REP(xx, t) {
		printf("Case #%d: ", xx + 1);
		scanf("%d", &n);
		REP(i, n) looking[i].clear();
		REP(i, n) h[i] = -1;
		h[n - 1] = h[n] = MAX;

		VI cmax;
		cmax.PB(n - 1);
		bool good = 1;

		REP(i, n - 1) {
			scanf("%d", &line[i]);
			line[i]--;
			DEB("%d -> %d\n", i, line[i]);
			if(i == cmax.back()) cmax.pop_back();
			if(line[i] > cmax.back()) {
				good = 0;
			}
			if(line[i] < cmax.back()) cmax.PB(line[i]);

			looking[line[i]].PB(i);
		}
		REP(i, n) {
			DEB("%d : ", i);
			FOREACH(it, looking[i]) DEB("%d ", *it);
			DEB("\n");
		}
		line[n - 1] = n;
		if(!good) {
			printf("Impossible\n");
			continue;
		}
		FORD(i, n - 1, 0) FOREACH(it, looking[i]) {
			LL x = *it, y, x_a = i, x_b = line[i], y_a = h[i], y_b = h[line[i]];
			y = ((y_b - y_a) * (x - x_a)) / (x_b - x_a) + y_a - 1;
			h[*it] = y;
			line[i] = *it;
			DEB("%d -> h[%d] = %d\n", i, *it, h[*it]);
		}
		REP(i, n) printf("%d ", h[i]);
		printf("\n");

	}
	return 0;
}

