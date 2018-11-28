#include <cstdio>
#include <cmath>
#include <algorithm>
#include <iostream>
using namespace std;
typedef long long lint;
typedef long double ldouble;

const ldouble eps = 1e-9;
const ldouble inf = 1e16;
inline bool eq(double a, double b) {
    return fabs(a - b) < eps;
}
inline bool lt(double a, double b) {
    return a < b && !eq(a, b);
}

int Pos[1 << 20];
int C, D, N;

void solve(int test) {
    printf("Case #%d: ", test);
    scanf("%d %d", &C, &D);
    N = 0;
    for(int i = 0; i < C; ++i) {
	int p, v;
	scanf("%d %d", &p, &v);
	for(int k = 0; k < v; ++k) {
	    Pos[N++] = p;
	}
    }
    ldouble lo = 0, hi = inf;
    while(hi - lo > eps) {
	ldouble d = 0.5 * (lo + hi);
	//cout << lo << " " << hi << " " << hi - lo << endl;
	ldouble pos = -inf;
	bool ok = true;
	for(int i = 0; ok && i < N; ++i) {
	    if(lt(d + Pos[i], pos + D)) {
		ok = false;
		break;
	    }
	    pos = max(pos + D, -d + Pos[i]);
	}
	if(ok) {
	    hi = d;
	}
	else {
	    lo = d;
	}
    }
    printf("%.9lf\n", (double)lo);
}


int main() {
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; ++i) {
	solve(i);
    }
    return 0;
}
