#include <stdio.h>
#include <string>
#include <iostream>
using namespace std;
string str[50];

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int i, j, k, n, ans;
	int cas;
	int m;
	scanf("%d", &n);
	for (cas = 1; cas <= n; cas ++) {
		scanf("%d", &m);
		for (i = 0;i < m;i++)
			cin >> str[i];
		ans = 0;
		for (i = 0;i < m;i++) {
			for (j = i;j < m;j++) {
				for (k = i + 1;k < m;k++)
					if (str[j][k] == '1')break;
				if (k == m)break;
			}
			for (k = j;k > i;k--) {
				str[k] = str[k-1];
				ans++;
			}
		}
		printf("Case #%d: %d\n", cas, ans);
	}
	return 0;
}
