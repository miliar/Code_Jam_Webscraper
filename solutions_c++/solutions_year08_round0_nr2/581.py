#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdlib>
using namespace std;

int main() {
	FILE* fin = fopen("blarge.in", "r");
	FILE* fout = fopen("outlargeb.txt", "w");
	int n;
	fscanf(fin, "%d", &n);
	vector<pair<int, int>> a[2];
	for (int round = 1; round <= n; round++) {
		int t, na, nb;
		fscanf(fin, "%d %d %d", &t, &na, &nb);
		a[0].clear();
		a[1].clear();
		for (int i = 0; i < na; i++) {
			int h1, h2, m1, m2;
			fscanf(fin, "%d:%d %d:%d", &h1, &m1, &h2, &m2);
			a[0].push_back(make_pair<int, int>(h1*60+m1, h2*60+m2));
		}
		for (int i = 0; i < nb; i++) {
			int h1, h2, m1, m2;
			fscanf(fin, "%d:%d %d:%d", &h1, &m1, &h2, &m2);
			a[1].push_back(make_pair<int, int>(h1*60+m1, h2*60+m2));
		}
		sort(a[0].begin(), a[0].end());
		sort(a[1].begin(), a[1].end());
		int ans[2];
		ans[0] = ans[1] = 0;
		int flag;
		while (a[0].size() > 0 || a[1].size() > 0) {
			if (a[1].size() == 0 || (a[0].size() != 0 && a[0][0].first <= a[1][0].first)) {
				flag = 0;
			}
			else
				flag = 1;
			ans[flag]++;
			int now[2];
			now[0] = now[1] = 0;
			int nowtime = 0;
			while (now[flag] < a[flag].size()) {
				nowtime = a[flag][now[flag]].second + t;
				a[flag].erase(a[flag].begin() + now[flag]);
				flag = 1 - flag;
				while (now[flag] < a[flag].size() && nowtime > a[flag][now[flag]].first)
					now[flag]++;
			}
		}
		fprintf(fout, "Case #%d: %d %d\n", round, ans[0], ans[1]);
	}
}
