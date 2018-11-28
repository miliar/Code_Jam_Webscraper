#include <stdio.h>
#include <assert.h>
#include <string.h>

bool enough (int x, int v, double time) {
    return (((double) x) < ((double) v) * time);
}

int main (void) {
    int T;
    int scanned = scanf("%d", &T);
    int g[101];
    for (int currentcase = 1; currentcase <= T; ++currentcase) {
	memset(g, 0, 101 * sizeof(int));
	int x, s, r, t, n;
	scanf("%d %d %d %d %d", &x, &s, &r, &t, &n);
	int a, b, ps;
	g[0] = x;
	for (int i = 0; i < n; ++i) {
	    scanf("%d %d %d", &a, &b, &ps);
	    g[ps] += b - a;
	    g[0] += a - b;
	}
	double T = t;
	double time = 0;
	for (ps = 0; T != 0 && ps <= 100; ++ps) {
	    if (enough(g[ps], r + ps, T)) {
		T -= ((double) g[ps]) / ((double) r + ps);
		time += ((double) g[ps]) / ((double) r + ps);
	    }
	    else {
		time += T + (((double) g[ps]) - ((double) r + ps) * T) / ((double) s + ps);
		T = 0;
	    }
	}
	for (; ps <= 100; ++ps) {
	    time += ((double) g[ps]) / ((double) ps + s);
	}
	printf("Case #%d: %.9lf\n", currentcase, time);
    }
    return 0;
}
