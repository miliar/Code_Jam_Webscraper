#include <iostream>

using namespace std;

const int N = 1010;

bool p[N];

void prime() {
	
	p[0] = p[1] = false;

	for (int i = 2; i < N; ++i) {
		p[i] = true;
	}
	

	for (int i = 2; i < N; ++i) {
		if (p[i] == true) {
			for (int j = i; i * j < N; ++j) {
				p[i * j] = false;
			}
		}
	}
}

int number[N];

int main() {

	int Tc;
	
	freopen("C-small-attempt2.in", "r", stdin);
	freopen("c.smal.out", "w", stdout);


	prime();

	scanf("%d", &Tc);

	for (int tc = 1; tc <= Tc; ++tc) {
		int n;

		scanf("%d", &n);

		for (int i = 0; i <= n; ++i) {
			number[i] = 0;
		}
		
		int max = 0;
		
	
		for (int i = 2; i <= n; ++i) {
			bool flag = false;
			for (int j = 2; j <= n; ++j) {
				if (p[j] == true) {
					int cnt = 0;

					int tmp = i;

					while (tmp % j == 0) {
						cnt++;
						tmp /= j;
					}

					if (cnt > number[j]) {
						flag = true;
						number[j] = cnt;
					}
				}
			}

			if (flag == true) {
				max++;
			}
		}
		
		max++;

		int min = 0;
		
		for (int i = 0; i <= n; ++i) {
			number[i] = 0;
		}

		for (int i = 2; i <= n; ++i) {
			for (int j = 2; j <= n; ++j) {
				if (p[j] == true) {
					int cnt = 0;

					int tmp = i;

					while (tmp % j == 0) {
						cnt++;
						tmp /= j;
					}

					if (cnt > number[j]) {
						number[j] = cnt;
					}
				}
			}
		}

		for (int i = 2; i <= n; ++i) {
			if (number[i] > 0) {
				min++;
			}
		}
		
		int ans = max - min;
		
		if (n == 1) {
			ans = 0;
		}

		printf("Case #%d: %d\n", tc, ans);
	}

	return 0;
}

