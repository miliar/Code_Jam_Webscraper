#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

typedef pair<double, double> pd;

vector<pd> dist;
double S, R, T;

void init() {
	double X; int N; scanf("%lf%lf%lf%lf%d", &X, &S, &R, &T, &N);

	vector< pair<pd, double> > dist1;
	dist1.resize(N);

	for (int i = 0; i < N; i++) {
		scanf("%lf%lf%lf", &dist1[i].first.first, &dist1[i].first.second,
				&dist1[i].second);
	}

	sort(dist1.begin(), dist1.end());

	dist.clear();
	double last = 0; double dist0 = 0;
	for (int i = 0; i < N; i++) {
		dist0 += dist1[i].first.first - last;
		dist.push_back(make_pair(dist1[i].second,
					dist1[i].first.second - dist1[i].first.first));
		last = dist1[i].first.second;
	}

	dist0 += X - last;
	dist.push_back(make_pair(0, dist0));

	sort(dist.begin(), dist.end());

//	for (int i = 0; i < dist.size(); i++) {
//		printf("%lf %lf\n", dist[i].first, dist[i].second);
//	}
}

void solve() {
	double ans = 0;
	
	for (int i = 0; i < dist.size(); i++) {
		double v = dist[i].first;
		double len = dist[i].second;

		double t1 = len / (v + R);
		double t2 = min(t1, T);
		T -= t2;

		ans += (len - t2 * (R - S)) / (v + S);
	}

	printf("%.9lf\n", ans);
}


int main() {
	int T; scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		init();
		printf("Case #%d: ", i);
		solve();
	}

	return 0;
}
