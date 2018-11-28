#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cstdlib>
using namespace std;

#define N 110
int t, xx, n, m;
char s[N][N];

void open() {
	freopen("A.txt", "r", stdin);
	freopen("A2.txt", "w", stdout);
}

int main() {
	open();
	xx = 1;
	scanf("%d", &t);
	while (t--) {
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++) {
			scanf("%s", s[i]);
		}
		for (int i = 0; i < n - 1; i++) {
			for (int j = 0; j < m - 1; j++) {
				if (s[i][j] == '#' && s[i][j+1] == '#' && s[i+1][j] == '#' && s[i+1][j+1] == '#') {
					s[i][j] = '/';
					s[i][j+1] = '\\';
					s[i+1][j] = '\\';
					s[i+1][j+1] = '/';
				}
			}
		}
		bool impossible = false;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (s[i][j] == '#') impossible = 1;
			}
		}
		printf("Case #%d:\n", xx++);
		if (impossible) printf("Impossible\n");
		else {
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					printf("%c", s[i][j]);
				}
				printf("\n");
			}
		}
	}
	return 0;
}