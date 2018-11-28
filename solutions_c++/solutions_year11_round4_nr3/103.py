#include <iostream>
#include <cstring>

using namespace std;

long long n;
bool isPrime[2000000];

void prepare()
{
	memset(isPrime, 1, sizeof(isPrime));
	for (int i = 2; i <  2000000; i++) {
		if (isPrime[i]) {
			int j = i + i;
			while (j < 2000000) {
				isPrime[j] = false;
				j += i;
			}
		}
	}
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int test;
	cin >> test;
	prepare();
	for (int tt = 1; tt <= test; tt++) {
		cout << "Case #" << tt << ": ";
		cin >> n;
		if (n == 1) {
			cout << 0 << endl;
			continue;
		}
		long long ans = 0;
		for (long long i = 2; i * i <= n; i++) {
			if (isPrime[i]) {
				long long tmp = i;
				while (tmp * i <= n) {
					tmp *= i;
					ans++;
				}
			}
		}
		cout << ans + 1 << endl;
	}
}