#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <iostream>

using namespace std;

#pragma comment(linker, "/STACK:160000000")

const int N = 333;

char comb[N][N];
bool opp[N][N];
vector <char> ans;

int main() {
#ifndef ONLINE_JUDGE
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
#endif
	int t;
	scanf("%d", &t);

	for (int tt = 0; tt < t; ++tt) {
		memset(comb, 0, sizeof(comb));
		memset(opp, 0, sizeof(opp));
		ans.clear();

		int c, d, n;

		scanf("%d ", &c);
		for (int i = 0; i < c; ++i) {
			char aq, bq, cq;
			scanf(" %c %c %c ", &aq, &bq, &cq);
			comb[aq][bq] = cq;
			comb[bq][aq] = cq;
		}

		scanf("%d ", &d);
		for (int i = 0; i < d; ++i) {
			char aq, bq;
			scanf(" %c %c ", &aq, &bq);
			opp[aq][bq] = 1;
			opp[bq][aq] = 1;
		}

		scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			char q;
			scanf(" %c ", &q);
			ans.push_back(q);
			while (ans.size() >= 2) {
				if (comb[ans.back()][ans[ans.size() - 2]] != 0) {
					char nq = comb[ans.back()][ans[ans.size() - 2]];
					ans.pop_back();
					ans.pop_back();
					ans.push_back(nq);
				} else {
					break;
				}
			}
			for (int x = 0; x < ans.size(); ++x) {
				for (int y = x + 1; y < ans.size(); ++y) {
					if (opp[ans[x]][ans[y]]) {
						ans.clear();
					}
				}
			}
		}

		printf("Case #%d: [", tt + 1);
		if (ans.size() > 0) {
			printf("%c", ans[0]);
		}
		for (int i = 1; i < ans.size(); ++i) {
			printf(", %c", ans[i]);
		}
		printf("]\n");
	}

	return 0;
}
