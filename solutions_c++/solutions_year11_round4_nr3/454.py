#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;
const int MAXN = 1010;
int prime[MAXN + 10], cnt;
bool isPrime[MAXN + 10];

void init() {
	cnt = 0;
	memset(isPrime, -1, sizeof (isPrime));
	isPrime[0] = isPrime[1] = false;
	for (int i = 2; i <= MAXN; ++i) {
		if (isPrime[i]) {
			prime[cnt++] = i;
			for (int j = i * i; j <= MAXN; j += i) {
				isPrime[j] = false;
			}
		}
	}
}

int main(int argc, char** argv) {
	init();
	int T;
	scanf("%d", &T);
	for (int nCase = 1; nCase <= T; ++nCase) {
		int n, ans = 0;
		scanf("%d", &n);
		if (n > 1) {
			++ans;
		}
		for (int i = 0; prime[i] <= n; ++i) {
			for (long long j = prime[i] * prime[i]; j <= n; j *= prime[i]) {
				++ans;
			}
		}
		printf("Case #%d: %d\n", nCase, ans);
	}
	return 0;
}
