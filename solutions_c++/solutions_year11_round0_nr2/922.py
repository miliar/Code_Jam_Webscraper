#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

const int MXN = 107;

char s[MXN], t[MXN];
char g[MXN][MXN];
bool h[MXN][MXN];

int main()
{
	int T;
	scanf("%d", &T);
	for (int numCase = 1; numCase <= T; ++numCase) {
		memset(g, 0, sizeof g);
		memset(h, 0, sizeof h);

		int c, d, n;
		scanf("%d", &c);
		while (c--) {
			scanf("%s", s);
			g[s[0] - 'A'][s[1] - 'A'] = g[s[1] - 'A'][s[0] - 'A']
				= s[2];
		}
		scanf("%d", &d);
		while (d--) {
			scanf("%s", s);
			h[s[0] - 'A'][s[1] - 'A'] = h[s[1] - 'A'][s[0] - 'A']
				= true;
		}

		scanf("%d%s", &n, s);
		int len = 0;
		for (int i = 0; i < n; ++i) {
			bool ok = true;
			char c = s[i];
			while (len > 0 && g[c - 'A'][t[len - 1] - 'A']) {
				c = g[c - 'A'][t[len - 1] - 'A'];
				--len;
			}
			t[len++] = c;

			for (int j = 0; j < len; ++j)
				if (h[t[j] - 'A'][c - 'A']) {
					ok = false;
					break;
				}
			if (!ok) len = 0;
		}
		printf("Case #%d: [", numCase);
		for (int i = 0; i < len; ++i) {
			if (i != 0) putchar(' ');
			printf("%c", t[i]);
			if (i + 1 != len) putchar(',');
		}
		puts("]");
	}
}
