#include <cstdio>
#include <cstring>
#define maxn 512
#define mod 10000

using namespace std;

int n, a[maxn][20], tt, q;
char s[20], v[maxn];

inline void read() {
	memset(a, 0, sizeof(a));
	fgets(v + 1, 510, stdin);

	n = 1;
	while (v[n] != 0)
		n++;
	n--;
}

inline int solve() {
	int i, j, sol = 0;
	for (i = 1; i <= n; i++)
		for (j = 0; j <= 18; j++)
			if (s[j] == v[i]) {
				if (j == 0)
					a[i][j] = (a[i][j] + 1) % mod;
				else {
					for (int k = 1; k < i; k++)
						a[i][j] = (a[i][j] + a[k][j - 1]) % mod;
				}
			}

	for (i = 1; i <= n; i++) 
		sol = (sol + a[i][18]) % mod;
	return sol;
}

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("c.out", "w", stdout);

	sprintf(s, "welcome to code jam");

	scanf("%d ", &tt);
	for (q = 1; q <= tt; q++) {
		read();
		printf("Case #%d: %04d\n", q, solve());
	}

	return 0;
}
