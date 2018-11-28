#include <cstdio>
#include <map>

using namespace std;

const int maxn = 100;

int row[maxn];
int n;

void Solve() {
	scanf("%d", &n);
	char ch;
	int i, j;
	for (i = 0; i < n; i++) {
		row[i] = -1;
		for (j = 0; j < n; j++) {
			scanf(" %c", &ch);
			if (ch == '1') row[i] = j;
		}
	}
	int ans = 0;
	for (i = 0; i < n; i++) {
		for (j = i; j < n; j++)
			if (row[j] <= i) break;
		for (; i < j; swap(row[j - 1], row[j]), ans++, j--);
	}
	printf("%d\n", ans);
}

int main() {
	int t, i;
	scanf("%d", &t);
	for (i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		Solve();
	}
	return 0;
}