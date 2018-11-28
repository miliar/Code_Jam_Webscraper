#include <cstdio>
#include <map>
#include <vector>

using namespace std;

const int N = 30;

int usual[N + 1];
int sup[N + 1];

void init() {
	for (int i = 0; i <= N; ++i) {
		usual[i] = sup[i] = 0;
	}
	for (int i = 0; i <= 10; ++i) {
		for (int j = 0; j <= 10; ++j) {
			for (int k = 0; k <= 10; ++k) {
				int l = min(i, min(j, k));
				int g = max(i, max(j, k));
				int sum = i + j + k;
				if (g - l <= 1) {
					usual[sum] = max(usual[sum], g);
				}
				if (g - l == 2) {
					sup[sum] = max(sup[sum], g);
				}
			}
		}
	}
}

vector<int> need_sup;
vector<int> need_usual;
vector<int> same;

int solve(int n, int s, int p, vector<int>& t) {

	need_sup.resize(0);
	need_usual.resize(0);
	same.resize(0);

	for (int i = 0; i < n; ++i) {
		int cur = t[i];
		if (usual[cur] >= p && sup[cur] >= p) {
			same.push_back(cur);
		}
		else if (usual[cur] >= p) {
			need_usual.push_back(cur);
		}
		else if (sup[cur] >= p) {
			need_sup.push_back(cur);
		}
	}
	int ans = 0;

	for (int i = 0; i < need_sup.size(); ++i) {
		if (s) --s, ++ans;
	}
	for (int i = 0; i < same.size(); ++i) {
		if (s) --s;
		++ans;
	}
	for (int i = 0; i < need_usual.size(); ++i) {
		if (s) --s;
		else ++ans;
	}
	return ans;
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	init();
	int n, s, p, T;
	scanf("%d", &T);
	vector<int> a;
	for (int t = 1; t <= T; ++t) {
		scanf("%d %d %d", &n, &s, &p);
		a.resize(n);
		for (int i = 0; i < n; ++i) {
			scanf("%d", &a[i]);
		}
		printf("Case #%d: %d\n", t, solve(n, s, p, a));
	}
	return 0;
} 