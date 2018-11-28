#include <string>
#include <vector>
#include <algorithm>
#include <numeric>

#include <iostream>
#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <list>

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>
using namespace std;

#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define SIZE(t) ((int)((t).size()))

typedef struct {
	long long pos;
	int v;
}node;
double ans;
bool operator < (node a, node b) {
	return a.pos < b.pos;
}
long long suck;
node hh[211];
long long C, D;

long long abs(long long a) {
	return a < 0 ? -a : a;
}
bool check(long long x) {
	long long ans = 0;
	long long now = hh[0].pos - x;
	for (int i = 0; i < C; ++i) {
		if (hh[i].pos - x >= now) {
			now = hh[i].pos - x;
		} else {
			if(abs(hh[i].pos - now) > x) {
				return false;
			}
		}
		for (int j = 0; j < hh[i].v; ++j) {
			now += D;
		}
		if (abs(now - D - hh[i].pos) > x) {
			return false;
		}
	}
	return true;
}

int main() {
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int T;
    scanf("%d", &T);
    int bb = 1;
    while (T--) {
		scanf("%lld%lld", &C, &D);
		D = D * 10;
		for (int i = 0; i < C; ++i) {
			scanf("%lld%d", &hh[i].pos, &hh[i].v);
			hh[i].pos = 10 * hh[i].pos;
		}
		sort(hh, hh + C);
		long long low = -11000000000000LL;
		long long high = 11000000000000LL;
		suck = 11000000000010LL;
		while (low <= high) {
			long long mid = (low + high) / 2;
			if (check(mid)) {
				suck = mid;
				high = mid - 1;
			} else {
				low = mid + 1;
			}
		}
		int dig = suck % 10;
		suck /= 10;
        printf("Case #%d: %lld.%d\n", bb++, suck, dig);
    }
    return 0;
}