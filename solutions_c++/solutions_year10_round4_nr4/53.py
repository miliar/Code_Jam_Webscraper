#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <set>

using namespace std;
#define dprintf debug && printf
const enum {SIMPLE, FOR, WHILE} mode = FOR;
bool debug = false;

void init() {
}

typedef pair<long double, long double> pdd;

long double sqr(long double x) { return x * x; }
long double dist(pdd a, pdd b) { return sqrt(sqr(a.first - b.first) + sqr(a.second - b.second)); }

bool solve(int P) {
	printf("Case #%d:", P+1);

	vector<pdd> poles;
	vector<pdd> buckets;
	int n, m;

	if(scanf("%d%d", &n, &m) != 2)
		assert(!"Failed to read nm");

	for(int i = 0; i < n; ++i) {
		int x, y;
		if(scanf("%d%d", &x, &y) != 2) assert(!"Failed to read pole");
		poles.push_back(pdd(x,y));
	}

	for(int i = 0; i < m; ++i) {
		int x, y;
		if(scanf("%d%d", &x, &y) != 2) assert(!"Failed to read bucket");
		buckets.push_back(pdd(x,y));
	}

	const long double d = dist(poles[0], poles[1]);

	for(int i = 0; i < m; ++i) {
		long double r1 = dist(poles[0], buckets[i]);
		long double r2 = dist(poles[1], buckets[i]);

		long double cur_area = sqr(r1) * acos((sqr(d) + sqr(r1) - sqr(r2)) / (2 * d * r1)) +
			               sqr(r2) * acos((sqr(d) + sqr(r2) - sqr(r1)) / (2 * d * r2)) -
								.5 * sqrt((r1+r2-d) * (r1+r2+d) * (r1+d-r2) * (r2+d-r1));
		printf(" %Lf", cur_area);
	}
	printf("\n");
	return true;

}

int main() {
  init();
  int n = mode == SIMPLE ? 1 : 1<<30;
  if (mode == FOR) scanf("%d", &n);
  for (int i = 0; i < n && solve(i); ++i);
  return 0;
}
