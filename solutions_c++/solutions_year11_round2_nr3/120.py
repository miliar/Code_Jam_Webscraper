#include <cstdio>

#include <vector>
#include <algorithm>

using namespace std;

typedef vector<int> TIntVector;
typedef vector<TIntVector> TIntVectorVector;

int maxC;
TIntVector maxColors;

void BT(int n, int bMaxColors, const TIntVectorVector& split, TIntVector& colors) {
	if (colors.size() == n) {
		TIntVector scolors = colors;
		sort(scolors.begin(), scolors.end());
		scolors.erase(unique(scolors.begin(), scolors.end()), scolors.end());
		if (scolors.back() + 1 == scolors.size()) {
			for (size_t i = 0; i < split.size(); ++i) {
				TIntVector has(split[i].size());
				for (size_t j = 0; j < split[i].size(); ++j)
					has[j] = colors[split[i][j]];
				sort(has.begin(), has.end());
				has.erase(unique(has.begin(), has.end()), has.end());
				if (has.size() != scolors.size())
					return;
			}
			if (scolors.size() > maxC) {
				maxC = scolors.size();
				maxColors = colors;
			}
		}
	} else {
		for (size_t i = 0; i < bMaxColors; ++i) {
			colors.push_back(i);
			BT(n, bMaxColors, split, colors);
			colors.pop_back();
		}
	}
}

int main() {
	// freopen("input.txt", "r", stdin);

	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int iTest = 0; iTest < t; ++iTest) {
		int n;
		scanf("%d", &n);
		TIntVector all;
		for (size_t i = 0; i < n; ++i)
			all.push_back(i);
		TIntVectorVector split(1, all);
		int m;
		scanf("%d", &m);

		TIntVector b(m);
		for (size_t i = 0; i < m; ++i)
			scanf("%d", &b[i]);
		TIntVector e(m);
		for (size_t i = 0; i < m; ++i)
			scanf("%d", &e[i]);

		for (size_t i = 0; i < m; ++i) {
			TIntVectorVector newSplit;
			--b[i];
			--e[i];
			for (size_t j = 0; j < split.size(); ++j) {
				TIntVector first;
				TIntVector second;
				for (size_t k = 0; k < split[j].size(); ++k) {
					if (split[j][k] == b[i] || split[j][k] == e[i]) {
						first.push_back(split[j][k]);
						second.push_back(split[j][k]);					
					} else if ( split[j][k] >= b[i] && split[j][k] <= e[i] ) {
						first.push_back(split[j][k]);
					} else {
						second.push_back(split[j][k]);
					}
				}
				if (first.size() > 1)
					newSplit.push_back(first);
				if (second.size() > 1)
					newSplit.push_back(second);
			}
			split = newSplit;
		}

		size_t bMaxColors = n;
		for (size_t i = 0; i < split.size(); ++i)
			bMaxColors = min(bMaxColors, split[i].size());

		maxC = 0;
		TIntVector colors;
		BT(n, bMaxColors, split, colors);

		printf("Case #%d: %d\n", iTest + 1, maxC);
		for (size_t i = 0; i < n; ++i)
			printf("%d ", maxColors[i] + 1);
		printf("\n");
		/*
		for (size_t i = 0; i < split.size(); ++i) {
			for (size_t j = 0; j < split[i].size(); ++j)
				printf("%d ", split[i][j]);
			printf("\n");
		}
		*/
	}

	return 0;
}