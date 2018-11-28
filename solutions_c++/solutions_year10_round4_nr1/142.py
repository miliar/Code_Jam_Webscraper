#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>

using namespace std;

template<class T> T sqr(const T& a) {
	return a * a;
}
template<class T> int size(const T& a) {
	return (int)a.size();
}
char a[200][200];
char s[200];
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int ntests;
	scanf("%d\n", &ntests);
	for (int itest = 1; itest <= ntests; itest++) {
		printf("Case #%d: ", itest);
		int n;
		gets(s);
		sscanf(s, "%d", &n);
		n = n + n - 1;
		for (int i = 0; i < n; i++) {
			memset(a[i], ' ', n);
			gets(a[i]);
			a[i][strlen(a[i])] = ' ';
			a[i][n] = 0;
			for (int j = 0; j < n && a[i][j] == ' '; j++) {
				a[i][j] = '?';				
			}
			for (int j = n - 1; j >= 0 && a[i][j] == ' '; j--) {
				a[i][j] = '?';				
			}
		}
		int res = sqr(n + n + 1);
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				bool g = 1;
				int S = 0;
				for (int r = 0; g && r < n; r++) {
					for (int c = 0; g && c < n; c++) {
						int di = r - i, dj = c - j;
						char num = a[r][c];
						if (num >= '0' && num <= '9') {
							S = max(S, abs(di) + abs(dj));
						}
						if (num == '?') continue;
						di = -di;
						if (i + di >= 0 && i + di < n && j + dj >= 0 && j + dj < n && a[i + di][j + dj] != '?') {
							if (a[i + di][j + dj] != num) {
								g = 0;
							}
						}
						di = -di;
						dj = -dj;
						if (i + di >= 0 && i + di < n && j + dj >= 0 && j + dj < n && a[i + di][j + dj] != '?') {
							if (a[i + di][j + dj] != num) {
								g = 0;
							}
						}
					}
				}
				if (g) {
					S = S + S + 1;
					res = min(res, S);
				}
			}
		}
		printf("%d\n", sqr((res + 1) / 2) - sqr((n + 1) / 2));
	}
	return 0;
}