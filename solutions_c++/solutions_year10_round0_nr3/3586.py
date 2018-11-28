#include <iostream>

using namespace std;

int main()
{
	freopen("c:\\C-small-attempt0.in", "r", stdin);
	freopen("c:\\output.txt", "w", stdout);
	
	int t, r, k, n;
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		scanf("%d%d%d", &r, &k, &n);
		int *g = new int[n];
		for (int j = 0; j < n; j++) {
			scanf("%d", &g[j]);
		}

		int s = 0;
		int p = 0, q = 0, temp = 0;
		for (int j = 0; j < r; j++) {
			q = 0;
			temp = 0;
			temp += g[(p + q) % n];
			while (q < n && temp <= k) {
				q++;
				temp += g[(p + q) % n];
			}
			temp -= g[(p + q) % n];
			p = p + q;
			s += temp;
		}

		printf("Case #%d: %d\n", i + 1, s);
	}
	return 0;
}