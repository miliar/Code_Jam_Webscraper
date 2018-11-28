#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main () {
	int  digits [50];
	int T;
	scanf("%d", &T);
	long num;
	for (int i = 1; i <= T; i ++)
	{
		scanf("%ld", &num);

		int count = 0;
		do {
			digits[count] = num % 10;
			num /= 10;
			count ++;
		} while (num > 0);

		for (int j = 0, k = count - 1; j < k; j ++, k--) {
			int temp = digits[j];
			digits[j] = digits[k];
			digits[k] = temp;
		}
		long ans = 0;
		if (! next_permutation(digits, digits + count)) {
			sort(digits, digits + count);
			int zc = 0;
			for (;digits[zc] == 0; zc ++);
			ans = digits[zc];
			for (int j = 0; j <= zc; j ++) ans *= 10;
			zc ++;
			while (zc < count) {
				ans *= 10;
				ans += digits[zc];
				zc ++;
			}
		}
		else {
			for (int j = 0; j < count; j ++) {
				ans *= 10;
				ans += digits[j];
			}
		}

		printf("Case #%d: %ld\n", i, ans);
	}
	return 0;
  }
