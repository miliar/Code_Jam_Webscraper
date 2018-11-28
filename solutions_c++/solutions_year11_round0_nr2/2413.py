#include <cstdio>
#include <vector>
#include <utility>

using namespace std;

const int MAX_ELEM = 30;

int cnt[MAX_ELEM];
vector < int > opposed[MAX_ELEM];
int combination[MAX_ELEM][MAX_ELEM];

int main() {
	int tests; scanf("%d", &tests);
	for (int test = 1; test <= tests; test++) {
		for (int i = 0; i < MAX_ELEM; i++) {
			cnt[i] = 0;
			opposed[i].clear();
			for (int j = 0; j < MAX_ELEM; j++)
				combination[i][j] = -1;
		}

		int c; scanf("%d", &c);
		while (c--) {
			char x, y, z; scanf(" %c %c %c", &x, &y, &z);
			int xx = (x - 'A');
			int yy = (y - 'A');
			int zz = (z - 'A');
			combination[xx][yy] = combination[yy][xx] = zz;
		}

		int d; scanf("%d", &d);
		while (d--) {
			char x, y; scanf(" %c %c", &x, &y);
			int xx = (x - 'A');
			int yy = (y - 'A');
			opposed[xx].push_back(yy);
			opposed[yy].push_back(xx);
		}

		int n; scanf("%d", &n);
		vector < int > ans;
		int last = -1;
		while (n--) {
			char x_; scanf(" %c", &x_);
			int x = (x_ - 'A');
			bool bad = false;
			for (int i = 0; i < (int) opposed[x].size(); i++) if (cnt[opposed[x][i]]) {
				bad = true;
				break;
			}
			
			if (last != -1 && combination[last][x] != -1) {
				cnt[last]--;
				ans.pop_back();
				ans.push_back(combination[last][x]);
				cnt[combination[last][x]]++;
				last = combination[last][x];
				continue;
			}
			if (bad) {
				for (int i = 0; i < MAX_ELEM; i++)
					cnt[i] = 0;
				ans.clear();
				last = -1;
				continue;
			}

			ans.push_back(x);
			cnt[x]++;
			last = x;
		}

		printf("Case #%d: [", test);
		for (int i = 0; i < (int) ans.size(); i++) {
			if (i > 0) printf(", ");
			printf("%c", (char) ('A' + ans[i]));
		}
		printf("]\n");
	}

	return 0;
}
