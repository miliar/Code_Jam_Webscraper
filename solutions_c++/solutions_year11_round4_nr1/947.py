#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

const int maxn = 100000;

double B[maxn], E[maxn], w[maxn];
double X, S, R, t;
int N;

struct Segment {
	double length, w, key;

	Segment() {
	}

	Segment(double length, double w) : length(length), w(w) {
		key = (w + S) * (w + R);
	}
};

bool operator < (const Segment &a, const Segment &b) {
	return a.key < b.key;
}

vector<Segment> seg_list;

void solve() {
	scanf("%lf %lf %lf %lf %d", &X, &S, &R, &t, &N);
	for (int i = 0; i < N; i++)
		scanf("%lf %lf %lf", &B[i], &E[i], &w[i]);
	seg_list.clear();
	seg_list.push_back(Segment(B[0], 0));
	for (int i = 0; i < N; i++) {
		seg_list.push_back(Segment(E[i] - B[i], w[i]));
		if (i + 1 < N)
			seg_list.push_back(Segment(B[i + 1] - E[i], 0));
	}
	seg_list.push_back(Segment(X - E[N - 1], 0));
	sort(seg_list.begin(), seg_list.end());
	double ans = 0, left_time = t;
	for (int i = 0; i < seg_list.size(); i++) {
		double walk = seg_list[i].length / (seg_list[i].w + S);
		double run = seg_list[i].length / (seg_list[i].w + R);
		double actual_cost = min(left_time, run);
		ans += actual_cost;
		left_time -= actual_cost;
		double left_dist = seg_list[i].length - (seg_list[i].w + R) * actual_cost;
		ans += left_dist / (seg_list[i].w + S);
	}
	printf("%.10lf\n", ans);
}

int main() {
	int t, i;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}