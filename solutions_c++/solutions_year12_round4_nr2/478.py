#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <valarray>
#include <vector>
using namespace std;

#define ALL(x) (x).begin(), (x).end()
#define MP make_pair
#define SZ(x) ((int) (x).size())
#define maxit(x,y) ((x) = max((x),(y)))
#define minit(x,y) ((x) = min((x),(y)))
typedef long long LL;
typedef complex<double> CD;

int N, W, L;
int R[1100];
int order[1100];
int maxr;

CD pos[1100];

bool ok(int n, int i)
{
	CD p = pos[order[i]];
	int rr = R[order[i]];
	for (int j = 0; j < n; ++j) {
		CD q = pos[order[j]];
		double r = R[order[j]];
		double d = abs(p-q);
		if (d < rr+r)
			return false;
	}
	return true;
}

double min_y(int n)
{
	double m = -1.0;
	for (int i = 0; i < n; ++i) {
		maxit(m, pos[order[i]].imag() + 2*maxr);
	}
	return m;
}

int main()
{
	int TC;
	scanf("%d", &TC);
	for (int tc = 1; tc <= TC; ++tc) {
		scanf("%d %d %d", &N, &W, &L);
		maxr = -1;
		for (int i = 0; i < N; ++i) {
			scanf("%d", &R[i]);
			maxit(maxr, R[i]);
			order[i] = i;
		}
RESTART:
		{
			random_shuffle(order, order+N);
			//puts("trying");
			double X = 0.0, Y = 0.0;
			for (int i = 0; i < N; ++i) {
				//printf("%lf %lf\n", X, Y);
				pos[order[i]] = CD(X, Y);
				if (ok(i,i))
					continue;
				pos[order[i]] = CD(W, Y);
				if (!ok(i,i)) {
					X = 0.0;
					//puts("hax");
					Y = min_y(i) + 0.00001;
					if (Y > L)
						goto RESTART;
					i -= 1;
					continue;
				}
				double lo = X;
				double hi = W;
				for (int j = 0; j < 100; ++j) {
					double mid = (lo+hi) / 2.0;
					pos[order[i]] = CD(mid, Y);
					if (ok(i,i))
						hi = mid;
					else
						lo = mid;
				}
				pos[order[i]] = CD(hi + 0.00001, Y);
				X = hi + 0.00001;
			}
			printf("Case #%d:", tc);
			for (int i = 0; i < N; ++i) {
				printf(" %0.6lf %0.6lf", pos[i].real(), pos[i].imag());
			}
			puts("");
			fflush(stdout);
		}
	}
	return 0;
}
