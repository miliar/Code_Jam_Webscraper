// Adrian Kügel
#include <stdio.h>
#include <vector>
#include <set>
#include <queue>
#include <math.h>
#include <stdlib.h>
#include <map>
#include <assert.h>
#include <limits.h>
#include <complex>
#include <algorithm>
#include <ctype.h>
#include <string>
using namespace std;

typedef set<int> SI;
typedef vector<int> VI;
typedef vector<string> VS;
typedef complex<double> tComp;

double b[1000], e[1000], w[1000];
double S, R, rem;

double eval(double d, double add, bool run) {
	if (!run)
		return d / (S + add);
	// determine how far I would get within rem seconds
	double dist = rem * (R + add);
	if (dist > d) {
		rem -= d / (R + add);
		return d / (R + add);
	}
	rem = 0;
	return dist / (R + add) + (d - dist) / (S + add);
}

struct segment {
	double len, speed;
}s[3000];

bool operator<(const segment &a, const segment &b) {
	return a.speed < b.speed;
}

int main() {
	int tc, n;
	double t, X;
	scanf("%d", &tc);
	for (int scen=1; scen<=tc; ++scen) {
		printf("Case #%d: ", scen);
		scanf("%lf %lf %lf %lf %d", &X, &S, &R, &t, &n);
		double pos = 0;
		int N = 0;
		for (int i=0; i<n; ++i) {
			scanf("%lf %lf %lf", &b[i], &e[i], &w[i]);
			s[N].len = b[i] - pos;
			s[N].speed = 0;
			++N;
			s[N].len = e[i] - b[i];
			s[N].speed = w[i];
			++N;
			pos = e[i];
		}
		s[N].len = X - pos;
		s[N].speed = 0;
		++N;
		sort(s, s+N);
		double best = 1e9;
//		for (int h=0; h<=100; ++h) {
		int h = 0;
		for (int h2 = h; h2 <= 100; ++h2) {
			double pos = 0;
			rem = t;
			double c = 0;
			for (int i=0; i<N; ++i) {
				c += eval(s[i].len, s[i].speed, (s[i].speed <= h2));
			}
//			c += eval(X - pos, 0, h == 0);
			if (c < best) {
//				printf("h = %d c = %lf\n", h, c);
				best = c;
			}
		}
//		}
		printf("%.9lf\n", best);
	}
	return 0;
}
