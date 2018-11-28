#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

#define MAXN 2000
#define eps 1e-7

struct Seg {
	int b, e, v;
}seg[MAXN], temp[MAXN];

int walk, run;

bool cmp(Seg s1, Seg s2) {
//	double t1 = (double)(s1.e - s1.b) / (walk + s1.v);
//	double t2 = (double)(s2.e - s2.b) / (walk + s2.v);
//	return t1 > t2;
	return walk + s1.v < walk + s2.v;
}

bool cmp1(Seg s1, Seg s2) {
	return s1.b < s2.b;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int cases;
	scanf("%d", &cases);
	for(int caseT = 1; caseT <= cases; ++caseT) {
		int len, ts, n;
		scanf("%d%d%d%d%d", &len, &walk, &run, &ts, &n);
		for(int i = 0; i < n; ++i) scanf("%d%d%d", &seg[i].b, &seg[i].e, &seg[i].v);
		sort(seg, seg + n, cmp1);
		int endPoint = 0, total = 0;
		for(int i = 0; i < n; ++i) {
			if(seg[i].b != endPoint) {
				temp[total].b = endPoint;
				temp[total].e = seg[i].b;
				temp[total++].v = 0;
			}
			endPoint = seg[i].e;
		}
		if(endPoint != len) {
			temp[total].b = endPoint;
			temp[total].e = len;
			temp[total++].v = 0;
		}
		for(int i = 0; i < total; ++i) seg[n++] = temp[i];
		double t = ts, res = 0.0;
		sort(seg, seg + n, cmp);

		for(int i = 0; i < n; ++i) {
			if(t > eps) {
				double t1 = (double)(seg[i].e - seg[i].b) / (run + seg[i].v);
				if(t1 <= t) {
					res += t1;
					t -= t1;
				}
				else {
					res += t;
					res += (double)(seg[i].e - seg[i].b - t * (run + seg[i].v)) / (walk + seg[i].v);
					t = 0;
				}
			}
			else {
				res += (double)(seg[i].e - seg[i].b) / (walk + seg[i].v);
			}
		}
		printf("Case #%d: %.9f\n", caseT, res);
	}
	return 0;
}
