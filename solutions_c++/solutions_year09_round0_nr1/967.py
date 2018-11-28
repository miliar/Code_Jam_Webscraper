#include <cstdio>
#include <cstring>

using namespace std;

char w[5000][16];
char s[1000];
int can[5000];
int now[26];

int main () {
	int l, d, n;
	scanf ("%d%d%d\n", &l, &d, &n);
	for (int i = 0; i < d; i++) scanf ("%s", w[i]);
	for (int i = 0; i < n; i++) {
		scanf ("%s", s);
		for (int j = 0; j < d; j++) can[j] = 1;
		int j = 0;
		for (int p = 0; s[j]; p++) {
			memset (now, 0, sizeof (now));
			if (s[j] == '(') {
				j++;
				while (s[j] != ')') now[s[j++] - 'a'] = 1;
			} else now[s[j] - 'a'] = 1;
			for (int k = 0; k < d; k++)
				if (can[k] && !now[w[k][p] - 'a'])
					can[k] = 0;
			j++;
		}
		int ans = 0;
		for (int j = 0; j < d; j++)
			ans += can[j];
		printf ("Case #%d: %d\n", i + 1, ans);
	}
}