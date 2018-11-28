/*
 * A.cpp
 *
 *  Created on: 7 May 2011
 *      Author: Admin
 */

#include<cstdio>
#include<vector>
#define min(A,B) ((A)<(B)?(A):(B))
#define max(A,B) ((A)<(B)?(B):(A))
#define abs(a) ((a)<0?(a)*-1:(a))
using namespace std;
int main() {

	freopen("A-large.in", "rt", stdin);
	freopen("a.txt", "wt", stdout);

	int t, n;
	char c;
	int x;
	scanf("%d", &t);
	for (int K = 1; K <= t; ++K) {
		scanf("%d", &n);
		vector<pair<int, int> > o, b;
		for (int i = 0; i < n; ++i) {
			scanf(" %c%d", &c, &x);
			if (c == 'O')
				o.push_back(make_pair(i, x));
			else
				b.push_back(make_pair(i, x));
		}
		size_t i = 0, j = 0, cnt = 0;
		int ci = 1, cj = 1, delta1, delta2;
		while (i < o.size() && j < b.size()) {
			if (o[i].first < b[j].first) {
				delta1 = abs(ci - o[i].second) + 1;
				ci = o[i].second;
				delta2 = b[j].second - cj;
				cj += min(abs(delta2), delta1) * (delta2) / (delta2 == 0 ? 1
						: abs(delta2));
				cnt += delta1;
				++i;
			} else {
				delta1 = abs(cj - b[j].second) + 1;
				cj = b[j].second;
				delta2 = o[i].second - ci;
				ci += min(abs(delta2), delta1) * (delta2) / (delta2 == 0 ? 1
						: abs(delta2));
				cnt += delta1;
				++j;
			}
		}
		while (i < o.size()) {
			cnt += abs(ci-o[i].second) + 1;
			ci = o[i].second;
			++i;
		}
		while (j < b.size()) {
			cnt += abs(cj-b[j].second) + 1;
			cj = b[j].second;
			++j;
		}
		printf("Case #%d: %d\n", K, cnt);
	}

	return 0;
}
