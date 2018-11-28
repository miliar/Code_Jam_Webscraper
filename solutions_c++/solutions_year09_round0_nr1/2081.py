#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>

using namespace std;

#define ZeroMemory(a) memset(a, 0, sizeof(a))
#define FillMemory(a, b) memset(a, b, sizeof(a))
char a[5000][30];
char s[100000];
char* w[5000];
char can[26];
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int l, n, t;
	scanf("%d %d %d", &l, &n, &t);
	for (int i = 0; i < n; i++) {
		scanf("%s", a[i]);
	}
	for (int ti = 1; ti <= t; ti++) {
		printf("Case #%d: ", ti);
		scanf("%s", s);
		char *p = s;
		int u = n;
		for (int i = 0; i < n; i++) {
			w[i] = a[i];
		}
		for (int i = 0; i < l; i++) {
			ZeroMemory(can);
			if (p[0] == '(') {
				p++;
				while (p[0] != ')') {
					can[p[0] - 'a'] = true;
					p++;
				}
				p++;
			} else {
				can[p[0] - 'a'] = true;
				p++;
			}
			int m = u;
			u = 0;
			for (int j = 0; j < m; j++) {
				if (can[w[j][i] - 'a']) {
					w[u++] = w[j];
				}
			}
		}
		printf("%d\n", u);
	}
	return 0;
}