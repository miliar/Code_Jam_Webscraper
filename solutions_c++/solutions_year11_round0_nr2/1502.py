#include <cstdio>
#include <vector>
#include <cstring>

using namespace std;

const int SIGMA = 256 + 10;

bool opps[SIGMA][SIGMA];
char make[SIGMA][SIGMA];

int main() {
	int nCase;
	scanf("%d", &nCase);
	for (int re = 1; re <= nCase; ++re) {
		int N, C, D;
		char x, y, z;
		memset(opps, 0, sizeof(opps));
		memset(make, 0, sizeof(make));

		scanf("%d", &C);
		for (int i = 0; i < C; ++i) {
			scanf(" %c%c%c", &x, &y, &z);
			make[x][y] = z;
			make[y][x] = z;
		}

		scanf("%d", &D);
		for (int i = 0; i < D; ++i) {
			scanf(" %c%c", &x, &y);
			opps[x][y] = true;
			opps[y][x] = true;
		}

		scanf("%d", &N);
		vector<char> ans;
		for (int i = 0; i < N; ++i) {
			scanf(" %c", &x);
			if (!ans.empty() && make[ans.back()][x]) {
				ans.back() = make[ans.back()][x];
			} else {
				ans.push_back(x);
				for (int j = ans.size() - 1; j >= 0; --j) {
					if (opps[ans[j]][x]) {
						ans.clear();
						break;
					}
				}
			}
		}

		printf("Case #%d: [", re);
		for (int i = 0; i < ans.size(); ++i) {
			printf("%c", ans[i]);
			if (i != ans.size() - 1) {
				printf(", ");
			}
		}
		puts("]");
	}
	return 0;
}
