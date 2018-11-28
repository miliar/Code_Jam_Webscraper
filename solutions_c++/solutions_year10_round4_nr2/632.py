#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int cases, n, m;
vector< pair<int, int> > v;
vector< vector<int> > price;
int cost;

int main() {
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);

	scanf("%d", &cases);
	for(int i = 0; i < cases; ++i) {
		scanf("%d", &n);

		v.clear();
		for(int j = 0; j < (1 << n); ++j) {
			scanf("%d", &m);
			v.push_back(make_pair(m, j));
		}

		sort(v.begin(), v.end());

		price.clear();
		price.resize(n);
		for(int j = 0; j < n; ++j) {
			price[j].clear();
			for(int k = 0; k < (1 << (n - 1 - j)); ++k) {
				scanf("%d", &m);
				price[j].push_back(m);
			}
		}

		cost = 0;
		for(int j = 0; j < v.size(); ++j) {

			vector< pair<int, int> > cand;
			int index = v[j].second;

			cand.clear();
			for(int k = 0; k < n; ++k) {
				index /= 2;
				cand.push_back(make_pair(price[k][index], -k));
			}

			sort(cand.begin(), cand.end());

			for(int k = 0; k < n - v[j].first; ++k) {
				cost += cand[k].first;
				price[ -cand[k].second ][ v[j].second / (1 << (1 - cand[k].second)) ] = 0;
			}
		}

		printf("Case #%d: %d\n", i + 1, cost);
	}

	return 0;
}