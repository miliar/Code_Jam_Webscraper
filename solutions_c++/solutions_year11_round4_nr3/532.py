#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int N;
vector<int> primes;
int ct[2000];

void calc_primes() {
	bool flag[2000] = {false};

	primes.push_back(2);
	for(int i = 3; i <= 1000; i += 2) {
		if (flag[i] == false) {
			primes.push_back(i);

			for(int j = i; j <= 1000; j += i) {
				flag[j] = true;
			}
		}
	}
}

bool call_waiter(int n) {
	bool result = false;

	for(int i = 0; i < primes.size() && primes[i] <= n; ++i) {
		int c = 0;
		while(primes[i] <= n && n % primes[i] == 0) {
			++c;
			n /= primes[i];
		}

		if (c > ct[i]) {
			result = true;
			ct[i] = c;
		}
	}

	return result;
}

void solve() {
	scanf("%d", &N);

	for(int i = 0; i < primes.size(); ++i)
		ct[i] = 0;

	int s1 = 0;
	for(int i = 1; i <= N; ++i) {
		if (call_waiter(i))
			++s1;
	}

	int s2 = 0;
	for(int i = 1; i <= primes.size(); ++i) {
		if (ct[i] != 0)
			++s2;
	}

	printf("%d\n", s1 - s2);
}

int main() {
	freopen("C:\\Users\\kiheon\\Downloads\\C-small-attempt1.in", "r", stdin);
	freopen("C:\\workspace\\GCJ\\output.txt", "w", stdout);

	calc_primes();
	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; ++i) {
		printf("Case #%d: ", i);
		solve();
	}

	return 0;
}
