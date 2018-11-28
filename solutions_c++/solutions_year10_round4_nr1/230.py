#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

int a[200][200];
int sum[200];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	for (int i = 1; i < 200; ++i)
		sum[i] = i + sum[i - 1];
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		memset(a, 0, sizeof(a));
		int n;
		scanf("%d", &n);
		int start = n;
		for (int i = 1; i <= n; ++i) {
			int tmp = start;
			for (int j = 0; j < i; ++j) {
				scanf("%d", &a[i][tmp]);
				a[i][tmp] += 1;
				tmp += 2;
			}
			--start;
		}
		start = 2;
		for (int i = n + 1; i < 2 * n; ++i) {
			int tmp = start;
			for (int j = 0; j < 2 * n - i; ++j) {
				scanf("%d", &a[i][tmp]);
				a[i][tmp] += 1;
				tmp += 2;
			}
			++start;
		}
		int res = 1000000000;
		//for (int i = 1; i < 2 * n; ++i) {
		//	for (int j = 1; j < 2 * n; ++j)
		//		printf("%d ", a[i][j]);
		//	puts("");
		//}
		//puts("");
		vector<int> f1(2 * n, 0), f2(2 * n, 0);
		for (int i = 1; i < 2 * n; ++i) {
			bool flag = true;
			for (int j = 1; j < i && flag; ++j) {
				int k = i + i - j;
				if (k >= 2 * n)
					continue;
				for (int l = 1; l < 2 * n && flag; ++l)
					if (a[j][l] && a[k][l] && a[j][l] != a[k][l])
						flag = false;
			}
			for (int j = i + 1; j < 2 * n && flag; ++j) {
				int k = i - (j - i);
				if (k < 1)
					continue;
				for (int l = 1; l < 2 * n && flag; ++l)
					if (a[j][l] && a[k][l] && a[j][l] != a[k][l])
						flag = false;
			}
			f1[i] = flag;
		}
		for (int i = 1; i < 2 * n; ++i) {
			bool flag = true;
			for (int j = 1; j < i && flag; ++j) {
				int k = i + i - j;
				if (k >= 2 * n)
					continue;
				for (int l = 1; l < 2 * n && flag; ++l)
					if (a[l][j] && a[l][k] && a[l][j] != a[l][k])
						flag = false;
			}
			for (int j = i + 1; j < 2 * n && flag; ++j) {
				int k = i - (j - i);
				if (k < 1)
					continue;
				for (int l = 1; l < 2 * n && flag; ++l)
					if (a[l][j] && a[l][k] && a[l][j] != a[l][k])
						flag = false;
			}
			f2[i] = flag;
		}
		for (int i = 1; i < 2 * n; ++i) {
			if (!f1[i]) continue;
			for (int ii = 1; ii < 2 * n; ++ii) {
				if (!f2[ii]) continue;
				bool flag = true;
				for (int j = 1; j < i && flag; ++j) {
					for (int l = 1; l < 2 * n && flag; ++l) {
						set<int> s;
						if (a[j][l])
							s.insert(a[j][l]);
						int k = i + i - j;
						if (k < 2 * n && a[k][l])
							s.insert(a[k][l]);
						int kk;
						if (l < ii)
							kk = ii + ii - l;
						else
							kk = ii - (l - ii);
						if (a[j][kk])
							s.insert(a[j][kk]);
						if (k < 2 * n && a[k][kk])
							s.insert(a[k][kk]);
						if (s.size() > 1)
							flag = false;
					}
				}
				for (int j = i + 1; j < 2 * n && flag; ++j) {
					for (int l = 1; l < 2 * n && flag; ++l) {
						set<int> s;
						if (a[j][l])
							s.insert(a[j][l]);
						int k = i - (j - i);
						if (k >= 1 && a[k][l])
							s.insert(a[k][l]);
						int kk;
						if (l < ii)
							kk = ii + ii - l;
						else
							kk = ii - (l - ii);
						if (a[j][kk])
							s.insert(a[j][kk]);
						if (k >= 1 && a[k][kk])
							s.insert(a[k][kk]);
						if (s.size() > 1)
							flag = false;
					}
				}
				if (!flag)
					continue;
				int x = max(i, 2 * n - i);
				int y = max(ii, 2 * n - ii);
				x += y - n;
				res = min(res, sum[x] + sum[x - 1] - sum[n] - sum[n - 1]);
			}
		}
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}