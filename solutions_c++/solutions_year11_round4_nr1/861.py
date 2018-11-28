#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#define eps 1e-11
#define feq(x,y) (((x)-(y))<(eps))
#define fl(x,y) ((x)+(eps)<(y))
#define fle(x,y) ((x)<(y)+(eps))
typedef long long LL;
using namespace std;

template<class T> string toString(const T &x) {ostringstream sout; sout << x; return sout.str();}
int toInt(string s) {istringstream sin(s); int n; sin >> n; return n; }

int x, s, r, n;
double t;
int b[1005], e[1005], w[1005];
int id[1005];

bool cmp(const int &x, const int &y) {
	return w[x] < w[y];
}

int main() {
	int T; scanf("%d", &T);
	int cas = 0;
	while (T--) {
		scanf("%d%d%d%lf%d", &x, &s, &r, &t, &n);
		int len = 0;
		for (int i = 0; i < n; ++i) {
			id[i] = i;
			scanf("%d%d%d", &b[i], &e[i], &w[i]);
			len += e[i] - b[i];
		}
		sort(id, id + n, cmp);
		int walk = x - len;
		printf("Case #%d: ", ++cas);
		double ret = 0;
		//printf("%d\n", walk);
		if (t * r > walk) {
			ret += walk * 1. / r;
			t -= ret;
		} else {
			ret += t + (walk - t * r) * 1. / s;
			t = 0;
		}
		//printf("%.6f\n", ret);
		for (int i = 0; i < n; ++i) {
			//printf("%d %d %d\n", w[id[i]], b[id[i]], e[id[i]]);
			double dist = e[id[i]] - b[id[i]];
			//printf("dist: %.4f time: %.4f\n", dist, t);
			if (t * (r + w[id[i]]) > dist) {
				double tt = dist * 1. / (r + w[id[i]]);
				ret += tt;
				t -= tt;
			} else {
				//printf("i: %d\n", i);
				ret += t + ((dist - t * (r + w[id[i]]) * 1.) / (s + w[id[i]]));
				t = 0;
			}
		}
		printf("%.9f\n", ret);
	}
	return 0;
}
