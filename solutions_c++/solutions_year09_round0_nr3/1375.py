#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <string>
using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define N 505

const string key = "welcome to code jam";
const int MOD = 10000;

int d[20][N];
char s[N];
int n, m;


int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	n = (int) key.length();

	gets(s);
	int tk;
	sscanf(s, "%d", &tk);

	for(int tc = 1; tc <= tk; ++tc) {
		gets(s);
		m = (int) strlen(s);
		forn(i, n + 1)
			forn(j, m + 1)
				d[i][j] = 0;
		d[0][0] = 1;
		forn(i, n + 1)
			forn(j, m) {
				d[i][j + 1] = (d[i][j + 1] + d[i][j]) % MOD;
				if (i < n && key[i] == s[j])
					d[i + 1][j + 1] = (d[i + 1][j + 1] + d[i][j]) % MOD;
			}
		printf("Case #%d: %04d\n", tc, d[n][m]);
	}
	return 0;
}