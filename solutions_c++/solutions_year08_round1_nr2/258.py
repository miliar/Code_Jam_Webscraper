#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

void run(int tt)
{
	vector<pair<int, int> > vp[128];
	int n;
	int m;
	scanf("%d %d", &n, &m);
	for (int i = 0; i < m; ++i) {
		int num;
		scanf("%d", &num);
		while (num--) {
			int a, b;
			scanf("%d %d", &a, &b);
			vp[i].push_back(make_pair(a - 1, b));
		}
	}
	int now = 1024;
	int bestmask = 0;
	for (int mm = 0; mm < (1 << n); ++mm) {
		int arr[10];
		int sum = 0;
		for (int i = 0; i < n; ++i) {
			if (mm & (1 << i)) {
				arr[i] = 0;
			}
			else {
				arr[i] = 1;
				++sum;
			}
		}
		int j = 0;
		for (j = 0; j < m; ++j) {
			int k;
			for (k = 0; k < vp[j].size(); ++k) {
				if (arr[vp[j][k].first] == vp[j][k].second) {
					break;
				}
			}
			if (k == vp[j].size()) {
				break;
			}
		}
		if (j == m) {
			if (sum < now) {
				now = sum;
				bestmask = mm;
			}
		}
	}
	printf("Case #%d:", tt);
	if (now == 1024) {
		puts(" IMPOSSIBLE");
	}
	else {
		for (int i = 0; i < n; ++i) {
			if (bestmask & (1 << i)) {
				printf(" 0");
			}
			else {
				printf(" 1");
			}
		}
		puts("");
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		run(i);
	}
	return 0;
}