#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <string>
#include <map>
#include <vector>

using namespace std;
#define dprintf debug && printf
const enum {SIMPLE, FOR, WHILE} mode = FOR;
bool debug = false;

void init() {
}

struct Plant {
	int r, x, y;
};

const double eps = 1e-7;

inline double sqr(double x) {
	return x * x;
}

inline double dist(const Plant &p1, const Plant &p2) {
	return sqrt(sqr(p1.x - p2.x) + sqr(p1.y - p2.y));
}

bool solve(int P) {
	int N;
	scanf("%d", &N);

	vector<Plant> plants(N);

	for(int i = 0; i < N; ++i) {
		scanf("%d%d%d", &plants[i].x, &plants[i].y, &plants[i].r);
	}


	int m = 0;
	for(int i = 0; i < N; ++i)
		m = max(m, plants[i].r);

	double lo = m;
	double hi = 2000;

	if(N <= 2) {
		hi = lo;
	}

	while(fabs(hi - lo) > eps) {
		double mid = (hi + lo) / 2;
		bool good = false;

		for(int i = 0; i < N; ++i) {
			for(int j = i + 1; j < N; ++j) {
				if(plants[i].r + plants[j].r + dist(plants[i], plants[j]) <= 2*mid)
					good = true;
			}
		}

		if(!good) {
			lo = mid;
		} else {
			hi = mid;
		}
	}

	printf("Case #%d: %.6lf\n", P + 1, (hi + lo) / 2);
	return true;
}

int main() {
  init();
  int n = mode == SIMPLE ? 1 : 1<<30;
  if (mode == FOR) scanf("%d", &n);
  for (int i = 0; i < n && solve(i); ++i);
  return 0;
}
