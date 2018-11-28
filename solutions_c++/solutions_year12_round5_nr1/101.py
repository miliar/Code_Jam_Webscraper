#include <cstdio>
#include <cstring>

#include <vector>
#include <algorithm>
#include <string>
#include <map>

using namespace std;

int main() {
	int T;
	scanf("%d", &T);
	for (int cn = 1; cn <= T; ++cn) {
		int n;
		scanf("%d", &n);
		vector<int> L(n), P(n);
		for (int i = 0; i < n; ++i)
			scanf("%d", &L[i]);
		for (int i = 0; i < n; ++i)
			scanf("%d", &P[i]);
		vector<int> ret;
		vector<pair<int, int> > LP(n);
		vector<int> idx(n);
		for (int i = 0; i < n; ++i) {
			LP[i] = make_pair(L[i], P[i]);
			idx[i] = i;
		}
		for (int i = 0; i < n; ++i) {
			for (int j = 1; j < n - i; ++j) {
				if (LP[j - 1].first * LP[j].second > LP[j].first * LP[j - 1].second) {
					swap(LP[j - 1], LP[j]);
					swap(idx[j - 1], idx[j]);
				}
			}
		}
		printf("Case #%d:", cn);
		for (int i = 0; i < n; ++i)
			printf(" %d", idx[i]);
		printf("\n");
	}
	return 0;
}
