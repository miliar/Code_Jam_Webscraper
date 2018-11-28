#include <cstdio>
#include <algorithm>
using namespace std;

const int MAXN = 1024 + 1;

int n, L[MAXN], P[MAXN], order[MAXN];

bool cmp(int a, int b) {
	return L[a] * P[a] > L[b] * P[b] || (L[a] * P[a] == L[b] * P[b] && P[a] > P[b]) || (L[a] * P[a] == L[b] * P[b] && P[a] == P[b] && a < b);
}

int main() {
	int taskNumber;
	scanf("%d", &taskNumber);
	for (int taskIdx = 0; taskIdx < taskNumber; taskIdx++) {
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%d", &L[i]);
			order[i] = i;
		}
		for (int i = 0; i < n; i++) {
			scanf("%d", &P[i]);
		}
		sort(order, order + n, cmp);
		printf("Case #%d:", taskIdx + 1);
		for (int i = 0; i < n; i++) {
			printf(" %d", order[i]);
		}
		putchar('\n');
	}
}
