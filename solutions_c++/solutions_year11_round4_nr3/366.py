#include <iostream>

long long prime[1000022];
bool pp[1000022];
int tot = 0;

bool getP(long long a)
{
	if (a == 2) return true;
	for (int j = 0; j < tot; j++)
		if ((a % prime[j]) == 0) return false;
	return true;
}

int main()
{
	freopen("p2.in" ,"r", stdin);
	freopen("p2.out", "w", stdout);
	for (int i = 0; i < 1001112; i++)
		pp[i] = true;
    for (int i = 2; i < 1001112; i++)
		if (pp[i])
			for (int j = 2; j <= 1001111 / i; j++)
				pp[i * j] = false;

	for (int i = 2; i < 1001112; i++)
		if (pp[i]) {
			prime[tot] = i;
			tot++;
		}
	int T;
	long long n;
	long long ans;
	std::cin >> T;
	for (int t0 = 0; t0 < T; t0++) {
		std::cin >> n;
		int p = 0;
		ans = 1;
		while (p < tot && prime[p] * prime[p] <= n) {
			long long q = prime[p] * prime[p];
			int s = 0;
			while (q <= n) {
				q *= prime[p];
				s++;
			}
			ans +=s;
			p++;
		}
		if ( n == 1) ans = 0;
		
		std::cout << "Case #" << t0 + 1 << ": " << ans << std::endl;
	}
	return 0;
}