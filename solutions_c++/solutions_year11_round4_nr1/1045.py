#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

const int maxn = 1010;
double x, s, r, t, w[maxn], b[maxn], e[maxn], rest;
int n, idx[maxn];

bool cmp(int a, int b) {
	return w[a] < w[b];
}

int main() {
	int tt = 0, tc;
	cin >> tc;
	for (tt = 1; tt <= tc; tt++) {
		cin >> x >> s >> r >> t >> n;
		rest = x;
		for (int i = 0; i < n; i++) {
			scanf("%lf%lf%lf", b + i, e + i, w + i);
			rest -= e[i] - b[i];
			idx[i] = i;
		}
		sort(idx, idx + n, cmp);
		//cout << rest << endl;
		double rt = t;
		double tot = 0;
		
		if (rest / r > rt) {
			tot += rt + (rest - rt * r) / s;
			rt = 0;
		} else {
			//cout << rest << " " <<  r << endl;
			tot += rest / r;			
			rt -= rest / r;
		}
		
		for (int i = 0; i < n; i++) {
			// printf("%d\n", i);
			if (rt == 0)
				tot += (e[idx[i]] - b[idx[i]]) / (s + w[idx[i]]);
			else {
				double rr = (e[idx[i]] - b[idx[i]]) / (r + w[idx[i]]);
				if (rr <= rt) {
					rt -= rr;
					tot += rr;
				} else {
					tot += rt + (double)(e[idx[i]] - b[idx[i]] - rt * (r + w[idx[i]])) / (double)(s + w[idx[i]]);
					rt = 0;
				}
			}
		}
		printf("Case #%d: %.9lf\n", tt, tot);
	}
}
