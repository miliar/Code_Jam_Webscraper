#define _CRT_SECURE_NO_DEPRECATE
//#define _CRT_RAND_S

//#include <windows.h>
//#include <tchar.h>
//#include <atlbase.h>
//#include <winerror.h>

#include <climits>
#include <ctime>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <map>
#include <set>
#include <deque>
#include <string>
#include <bitset>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

typedef unsigned char byte;
typedef unsigned short ushort;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef long long ll;

typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

#define SZ 1024
int b[SZ], e[SZ], w[SZ];
pii d[SZ];
int main() {
	int c, C;
	scanf("%d", &C);
	for (c = 1; c <= C; c++) {
		int x, s, r, t, i, n;
		scanf("%d %d %d %d %d", &x, &s, &r, &t, &n);
		d[n] = pii(s, x);
		for (i = 0; i < n; i++) {
			scanf("%d %d %d", b + i, e + i, w + i);
			d[i] = pii(s + w[i], e[i] - b[i]);
			d[n].second -= e[i] - b[i];
		}
		sort(d, d + n + 1);
		double dt, T = 0;
		for (i = 0; i <= n; i++) {
			dt = (double) d[i].second / (d[i].first + r - s);
			if (T + dt <= t) {
				T += dt;
			}
			else {
				if (T < t) {
					double ds = (double) (t - T) * (d[i].first + r - s);
					T += (t - T);
					T += (double) (d[i].second - ds) / d[i].first;
				}
				else {
					T += (double) d[i].second / d[i].first;
				}
			}
		}
		printf("Case #%d:%.7lf\n", c, T);
	}
	return (0);
}
