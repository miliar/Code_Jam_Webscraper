#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef pair<int, int> pii;
typedef pair<pii, int> piii;

const int h = 1010;

int TC, X, S, R, N;
double T;
piii a[h];
vector<pii> v;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &TC);
	for (int t = 0; t < TC; t++) {
		scanf("%d%d%d%lf%d", &X, &S, &R, &T, &N);
		v.clear();
		a[0] = make_pair(make_pair(0, 0), 0);
		for (int i = 1; i <= N; i++)
			scanf("%d%d%d", &a[i].first.first, &a[i].first.second, &a[i].second);
		a[N+1] = make_pair(make_pair(X, X), 0);
		for (int i = 1; i <= N+1; i++) {
			if (a[i-1].first.second < a[i].first.first)
				v.push_back(make_pair(S, a[i].first.first - a[i-1].first.second));
			if (i < N+1)
				v.push_back(make_pair(a[i].second + S, a[i].first.second - a[i].first.first));
		}
		sort(v.begin(), v.end());
		double ans = 0.;
		for (int i = 0; i < v.size(); i++) {
			double e = 0.;
			e = v[i].second / (double) (v[i].first + R - S);
			if (e > T) {
				double l = v[i].second - (double) ((v[i].first + R - S) * (double) T);
				ans += T;
				T = 0.;
				ans += l / (double) v[i].first;
			} else {
				T -= e;
				ans += e;
			}
		}
		printf("Case #%d: %.8lf\n", t+1, ans);
	}
	return 0;
}