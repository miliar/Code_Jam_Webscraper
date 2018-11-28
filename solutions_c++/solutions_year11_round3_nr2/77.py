#include <cstdio>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

long long L, t, N, C;
vector<long long> dist;

void getDist() {
	dist.clear();
	vector<int> temp;
	for(int i = 0; i < C; ++i) {
		int inp;
		scanf("%d", &inp);
		temp.push_back(inp * 2);
	}

	for(int i = 0; i < N; ++i) {
		dist.push_back(temp[i%C]);
	}
}

void solve() {
	scanf("%lld%lld%lld%lld", &L, &t, &N, &C);

	getDist();

	long long res = 0;
	for(int i = 0; i < N; ++i) {
		t -= dist[i];
		res += dist[i];
		dist[i] = 0;
		if (t <= 0) {
			dist[i] = -t;
			res -= dist[i];
			sort(dist.begin(), dist.end(), greater<long long>());
			break;
		}
	}

	for(int i = 0; i < L; ++i) {
		dist[i] /= 2;
	}

	for(int i = 0; i < N; ++i) {
		res += dist[i];
	}

	printf("%lld\n", res);
}

int main() {
	freopen("C:\\Users\\kiheon\\Downloads\\B-large.in", "r", stdin);
	freopen("C:\\workspace\\GCJ\\output.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; ++i) {
		printf("Case #%d: ", i);
		solve();
	}

	return 0;
}
