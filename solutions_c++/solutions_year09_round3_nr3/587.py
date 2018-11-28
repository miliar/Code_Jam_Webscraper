#include <iostream>

using namespace std;

bool used[10], empty[200];
int nr[20], eile[10], ats, p, q, n;

int cost() {
	fill(empty, empty + p + 2, false);
	int c = 0;
	for (int r = 0; r < q; r++) {
		empty[eile[r]] = true;
		for (int t = eile[r] - 1; t > 0 && !empty[t]; t--)
			c++;
		for (int t = eile[r] + 1; t <= p && !empty[t]; t++)
			c++;
	}
	return c;
}

void generuok(int vt) {
	if (vt == q) {
		ats = min(ats, cost());
		return;
	}
	for (int i = 0; i < q; i++)
		if (!used[i]) {
			used[i] = true;
			eile[vt] = nr[i];
			generuok(vt + 1);
			used[i] = false;
		}
}
	

int main() {
	freopen("small.in", "r", stdin);
	freopen("small.out", "w", stdout);
	scanf("%d", &n);
	for (int x = 1; x <= n; x++) {
		scanf("%d %d", &p, &q);
		fill(used, used + 8, false);
		for (int i = 0; i < q; i++)
			scanf(" %d", &nr[i]);
		ats = 1 << 30;
		generuok(0);
		printf("Case #%d: %d\n", x, ats);
	}
	return 0;
}
