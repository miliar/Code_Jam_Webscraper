#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		int n;
		int o = 1, b = 1;
		int cur = 0;
		cin >> n;
		char op[200];
		int d[200];
		for (int i = 0; i < n; ++i) {
			cin >> op[i] >> d[i];
		}
		for (int i = 0; i < n; ++i) {
			int d2 = -1, j;
			for (j = i + 1; j < n; ++j)
				if (op[j] != op[i]) {
					d2 = d[j];
					break;
				}
			if (op[i] == 'O') {
				while (1) {
					++cur;
					if (d2 != -1) {
						if (b < d2) ++b;
						else if (b > d2) --b;
					}
					if (o < d[i]) ++o;
					else if (o > d[i]) --o;
					else break;
				}
			} else {
				while (1) {
					++cur;
					if (d2 != -1) {
						if (o < d2) ++o;
						else if (o > d2) --o;
					}
					if (b < d[i]) ++b;
					else if (b > d[i]) --b;
					else break;
				}
			}
		}
		printf("Case #%d: %d\n", t + 1, cur);
	}
}
