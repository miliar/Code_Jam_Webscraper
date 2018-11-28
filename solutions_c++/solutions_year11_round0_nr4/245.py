#include <iostream>
#include <cstdio>
#include <string>

using namespace std;
int s[2000];
bool flag[2000];
int main()
{
	freopen("d.in", "r", stdin);
	freopen("d.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; ++t) {
		int n;
		cin >> n;
		int i;
		for (i = 0; i < n; ++i) {
			cin >> s[i];
			--s[i];
			flag[i] = false;
		}
		int ans = 0;
		for (i = 0; i < n; ++i) {
			if (!flag[i] && s[i] != i) {
				int h = 0, j = i;
				do {
					++h;
					flag[j] = true;
					j = s[j];
				} while (j != i);
				ans += h;
			}
		}
		printf("Case #%d: %d.000000\n", t + 1, ans);
	}
}
