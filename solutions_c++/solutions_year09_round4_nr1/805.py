#include <cstdio>
#define maxn 52

using namespace std;

char s[maxn][maxn];
int n, i, j, tt, rez;
int v[maxn];

inline int max(int a, int b) {
	if (a > b)
		return a;
	return b;
}

void read() {
	int pmax = 0;
	scanf("%d ", &n);

	for (i = 1; i <= n; i++) {
		scanf("%s", s[i]);
		pmax = 0;

		for (j = 0; j < n; j++)
			if (s[i][j] == '1')
				pmax = max(pmax, j + 1);
		v[i] = pmax;
	}
}

void solve() {
	int i, j, poz, aux;
	for (i = 1; i <= n; i++) {
		if (v[i] > i) {
			for (j = i + 1; j <= n; j++)
				if (v[j] <= i) {
					poz = j;
					break;
				}
			aux = v[poz];
			rez += poz - i;
			for (j = poz; j >= i + 1; j--)
				v[j] = v[j - 1];
			v[i] = v[poz];
		}
		
	}
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("a.out", "w", stdout);

	scanf("%d", &tt);
	for (int q = 1; q <= tt; q++) {
		read();
		rez = 0;
		solve();
		printf("Case #%d: %d\n", q, rez);
	}

	return 0;
}
