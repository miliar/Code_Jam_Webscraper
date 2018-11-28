#include <iostream>
#include <algorithm>
#include <numeric>

using namespace std;

int main() {
	int nTests;
	scanf("%d", &nTests);
	for (int test = 1; test <= nTests; ++test) {
		long long N, Pd, Pg;
		scanf("%lld %lld %lld", &N, &Pd, &Pg);
		bool possible = true;
		long long D = 100/__gcd(100ll, Pd);
		if (D > N) {
			possible = false;
		}
		if (possible) {
			long long Min, Max;
			if (Pd == 100) {
				Min = 1;
				Max = 100;
			} else if (Pd == 0) {
				Min = 0;
				Max = 99;
			} else {
				Min = 1;
				Max = 99;
			}
			if (Pg < Min || Pg > Max) {
				possible = false;
			}
		}
		printf("Case #%d: ", test);
		if (possible) {
			printf("Possible\n");
		} else {
			printf("Broken\n");
		}
	}
	return 0;
}
