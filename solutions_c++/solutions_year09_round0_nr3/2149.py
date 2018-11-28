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
const char a[] = "welcome to code jam";
char s[1000];
int dm[1000][20];
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, l = (int)(strlen(a));
	gets(s);
	sscanf(s, "%d", &t);
	for (int ti = 1; ti <= t; ti++) {
		printf("Case #%d: ", ti);
		gets(s);
		ZeroMemory(dm);
		int res = 0;
		for (int i = 0; s[i]; i++) {
			dm[i][0] = 1;
			for (int j = 0; j < l; j++) {
				dm[i + 1][j + 1] = dm[i][j + 1];
				if (s[i] == a[j]) {
					dm[i + 1][j + 1] += dm[i][j];
				}
				dm[i + 1][j + 1] %= 10000;
			}
			res = dm[i + 1][l];
		}
		printf("%04d\n", res);
	}
	return 0;
}