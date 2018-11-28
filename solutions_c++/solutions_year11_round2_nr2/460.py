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

#define SZ 256

#define INF 1e+30

struct atom {
	double l, r;
	double c;
	atom(double l, double r, double c) : l(l), r(r), c(c) {}
};

double m[SZ];
double p[SZ];

int main() {
	int c, tc;
	scanf("%d", &tc);
	for (c = 1; c <= tc; c++) {
		int i, n;
		double d;
		scanf("%d %lf", &n, &d);
		for (i = 0; i < n; i++)
			scanf("%lf %lf", p + i, m + i);
		
		double e, f, g, h;
		vector<atom> v;
		v.push_back(atom(-INF, -INF, 0));
		for (i = 0; i < n; i++) {
			e = d * (m[i] - 1) / 2;
			atom t(p[i] - e, p[i] + e, e);
			
			f = v.back().r + d - t.l;
			if (f <= 0) {
				v.push_back(t);
				continue;
			}
			t = atom(t.l + f, t.r + f, t.c + f);
			
			for (;;) {
				f = min(f, (t.c - v.back().c) / 2);
				t = atom(v.back().l, t.r, max(v.back().c, t.c));
				v.pop_back();
				if (f <= 0) {
					v.push_back(t);
					break;
				}
				g = min(f, t.l - (v.back().r + d));
				t = atom(t.l - g, t.r - g, t.c - g);
				if (g == f) {
					v.push_back(t);
					break;
				}
				f -= g;
			}
		}
		
		double r = 0;
		for (i = 0; i < (int) v.size(); i++)
			r = max(r, v[i].c);
		printf("Case #%d: %lf\n", c, r);
	}
	
	return (0);
}
