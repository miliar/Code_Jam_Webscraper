#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
#include <numeric>

using namespace std;

// Expensive Dinner

long long gcd(long long a, long long b) {
	if (b == 0) {
		return a;
	}
	return gcd(b, a % b);
}

int main()
{
	int cases;
	cin >> cases;

	vector <int> primes;
	for (int i = 2; i <= 1000; i++) {
		bool ok = true;
		for (int j = 0; j < primes.size(); j++) {
			if (i % primes[j] == 0) {
				ok = false;
				break;
			}
		}
		if (ok) {
			primes.push_back(i);
		}
	}

	for (int caseno = 1; caseno <= cases; caseno++) {
		int N;
		cin >> N;
		int ret1 = 1;
		int ret2 = (N == 1) ? 1 : 0;
		vector <int> lcd(primes.size(), 0);
		for (int i = 2; i <= N; i++) {
			int n = i;
			bool flag = false;
			for (int j = 0; j < primes.size(); j++) {
				for (int k = 0; n % primes[j] == 0; k++) {
					n /= primes[j];
					if (lcd[j] <= k) {
						flag = true;
						lcd[j]++;
					}
				}
			}
			if (flag) {
				ret1++;
				//printf("%d %d\n", i, ret1);
			}
		}
		lcd = vector <int>(primes.size(), 0);
		for (int j = 0; j < primes.size() && primes[j] <= N; j++) {
			lcd[j] = 100;
			ret2++;
		}
		for (int i = N; i >= 2; i--) {
			int n = i;
			bool flag = false;
			for (int j = 0; j < primes.size(); j++) {
				for (int k = 0; n % primes[j] == 0; k++) {
					n /= primes[j];
					if (lcd[j] <= k) {
						flag = true;
						lcd[j]++;
					}
				}
			}
			if (flag) {
				ret2++;
			}
		}
		//printf("%d %d %d\n", N, ret1, ret2);
		cout << "Case #" << caseno << ": " << ret1 - ret2 << endl;
	}

	return 0;
}
