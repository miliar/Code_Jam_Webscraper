#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

double X, S, R, t;
int N;

struct WalkWay {
	double L, w;

	bool operator < (const WalkWay& rhs) const {
		return w < rhs.w;
	}
};

vector<WalkWay> walkways;

vector<WalkWay> inp() {
	walkways.clear();

	scanf("%lf%lf%lf%lf%d", &X, &S, &R, &t, &N);

	double L = X;
	for(int i = 0; i < N; ++i) {
		WalkWay inp;
		double B, E;
		scanf("%lf%lf%lf", &B, &E, &inp.w);
		inp.L = E - B;

		walkways.push_back(inp);
		L -= inp.L;
	}

	WalkWay inp;
	inp.L = L;
	inp.w = 0;
	walkways.push_back(inp);

	sort(walkways.begin(), walkways.end());

	return walkways;
}

double calc_duration(int i) {
	double d = walkways[i].L / (walkways[i].w + R);
	if (d > t) {
		double L = walkways[i].L;
		L -= (walkways[i].w + R) * t;
		d = t + L / (walkways[i].w + S);
	}

	return d;
}

void solve() {
	inp();

	double result = 0.;
	for(int i = 0; i < walkways.size(); ++i) {
		double d = calc_duration(i);
		result += d;
		t = max(0., t-d);
	}

	printf("%.9lf\n", result);
}

int main() {
	freopen("C:\\Users\\kiheon\\Downloads\\A-large.in", "r", stdin);
	freopen("C:\\workspace\\GCJ\\output.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; ++i) {
		printf("Case #%d: ", i);
		solve();
	}

	return 0;
}
