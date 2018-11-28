#include <cstdio>
#include <utility>
#include <algorithm>
using namespace std;

const int MaxN = 1111;
int n, w, h, r[MaxN], result[MaxN][2];
pair<int, int> rx[MaxN];
pair<int, pair<int, int> > resultx[MaxN];

void work() {
	scanf("%d%d%d", &n, &h, &w);
	for (int i = 0; i < n; ++ i) {
		scanf("%d", &rx[i].first);
		rx[i].second = i;
	}

	sort(rx, rx + n);
	for (int i = 0; i < n; ++ i) {
		r[i] = rx[i].first;
	}

	int p = 0, t = 0;
	while (p < n) {
		int q = p, sum = 0, mt = 0;
		do {
			sum += sum == 0 ? r[q] : r[q] + r[q];
			++ q;
		} while (q < n && sum + r[q] <= w);
		sum = 0;
		for (int i = p; i < q; ++ i) {
			resultx[i].first = rx[i].second;
			resultx[i].second.first  = t == 0 ? 0 : t + r[i];
			resultx[i].second.second = sum == 0 ? 0 : sum + r[i];
			sum += sum == 0 ? r[i] : r[i] + r[i];
			mt = max(mt, r[i]);
		}
		t += t == 0 ? mt : mt + mt;
		p = q;
	}

	for (int i = 0; i < n; ++ i) {
		result[resultx[i].first][0] = resultx[i].second.first;
		result[resultx[i].first][1] = resultx[i].second.second;
	}

	for (int i = 0; i < n; ++ i) {
		printf(" %d.0 %d.0", result[i][0], result[i][1]);
		if (result[i][0] > h || result[i][1] > w) fprintf(stderr, "orz\n");
	}
	printf("\n");
}

int main() {
	int tn;
	scanf("%d", &tn);
	for (int t = 1; t <= tn; ++ t) {
		printf("Case #%d:", t);
		work();
	}
	return 0;
}
