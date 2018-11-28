#include <iostream>
#include <cstdio>
#include <algorithm>

int a[1100];
int b[1100];
int c[1100];

int main() 
{
	freopen("p2.in", "r", stdin);
	freopen("p2.out", "w", stdout);
	int T;
	std::cin >> T;
	int n;
	for (int t = 0; t < T; t++) {
		std::cin >> n;
		for (int i = 0; i < n; i++)
			std::cin >> a[i];
		std::sort(a, a + n);
		for (int i = 0; i < n; i++) {
			b[i] = c[i] = 0;
		}
		int all = 0;
		for (int i = 0; i < n; i++) {
			int d = -1;
			for (int j = all - 1; j >= 0; j--) 
				if (b[j] == a[i] - 1) {
					if (d == -1 || c[j] < c[d]) d = j;
				}
		    if (d == -1) {
				b[all] = a[i];
			    c[all] = 1;
				all++;
			} else {
				b[d] = a[i];
				c[d]++;
			}
		}
		int ans = n;
		for (int i = 0; i < all; i++)
			if (c[i] < ans) ans = c[i];
/*		int min = 1; 
		int max = n;
		while (min < max) {
			int mid = (min + max) / 2;
			if (check(mid)) {
				if (mid > ans) ans = mid;
				min = mid + 1;
			} else max = mid - 1;
		}
		if (check(min)) 
			if (min > ans) ans = min;*/
		std::cout << "Case #" << t + 1 << ": ";
		std::cout << ans << std::endl;
	}
	return 0;
}