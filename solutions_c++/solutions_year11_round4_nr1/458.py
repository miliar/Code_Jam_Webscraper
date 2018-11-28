#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

const int MXN = 1007;

int T;
int X, S, R, N;
double t;
int l[MXN], r[MXN], w[MXN];
int id[MXN];

inline bool cmp(int a, int b)
{
	return w[a] < w[b];
}

int main()
{
	scanf("%d", &T);
	int numCase = 0;
	while (T--) {
		scanf("%d%d%d%lf%d", &X, &S, &R, &t, &N);
		double Y = X;
		for (int i = 0; i < N; ++i) {
			scanf("%d%d%d", l + i, r + i, w + i);
			id[i] = i;
			Y -= r[i] - l[i];
		}
		sort(id, id + N, cmp);

		double ans = 0;
		if (R * t <= Y) {
			ans += t;
			ans += (Y - R * t) / S;
			t = 0;
		} else {
			double tt = Y / R;
			ans += tt;
			t -= tt;
		}
		for (int i = 0; i < N; ++i) {
			double len = r[id[i]] - l[id[i]];
			if ((R + w[id[i]]) * t <= len) {
				ans += t;
				ans += (len - (R + w[id[i]]) * t) / (S + w[id[i]]);
				t = 0;
			} else {
				double tt = len / (R + w[id[i]]);
				ans += tt;
				t -= tt;
			}
		}
		printf("Case #%d: %.7f\n", ++numCase, ans);
	}
}
