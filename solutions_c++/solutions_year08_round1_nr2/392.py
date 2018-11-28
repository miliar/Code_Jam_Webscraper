#include <cstdio>
#include <utility>
#include <vector>
using namespace std;

const int M = 128;
vector<pair<int, int> > mat[128];
int vec[16];
int res[16];

int main() {
	int t, n, m;
	scanf("%d", &t);
	for (int k = 0; k < t; ++k) {
		scanf("%d%d", &n, &m);
		int ret = n + 1;
		memset(mat, 0, sizeof(mat));
		for (int i = 0; i < M; ++i) mat[i].clear();
		for (int i = 0; i < m; ++i) {
			int r, ind, val;
			scanf("%d", &r);
			for (int j = 0; j < r; ++j) {
				scanf("%d%d", &ind, &val);
				mat[i].push_back(make_pair(ind - 1, val));
			}
		}
		for (int i = 0; i < (1u << n); ++i) {
			int tmp = i, cnt = 0;
			memset(vec, 0, sizeof(vec));
			for (int j = 0; tmp; ++j) {
				vec[j] = tmp % 2;
				cnt += tmp % 2;
				tmp /= 2;
			}
			if (cnt >= ret) continue;
			bool ok = true;
			for (int j = 0; ok && j < m; ++j) {
				bool ok2 = false;
				for (int r = 0; !ok2 && r < mat[j].size(); ++r) {
					int index = mat[j][r].first;
					if (vec[index] == mat[j][r].second) {
						ok2 = true;
					}
				}
				if (!ok2) ok = false;
			}
			if (ok && cnt < ret) {
				ret = cnt;
				for (int j = 0; j < n; ++j) res[j] = vec[j];
			}
		//	printf("%d\n", cnt);
		}
		printf("Case #%d: ", k + 1);
		if (ret <= n) {
			printf("%d", res[0]);
			for (int i = 1; i < n; ++i)
				printf(" %d", res[i]);
			printf("\n");
		} else {
			printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}

