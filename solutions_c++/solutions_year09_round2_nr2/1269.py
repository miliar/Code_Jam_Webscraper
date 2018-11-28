#include <iostream>
#include <algorithm>
using namespace std;

int main(int argc, char *argv[]) {
	int ncases, c;
	cin >> ncases;
	for (c = 1; c <= ncases; c++) {
		int number;
		cin >> number;

		int digits[1000];
		int n = number;

		int i = 0;
		while (number > 0) {
			digits[i] = number%10;
			number /= 10;
			i++;
		}
		//digits[i] = 0;
		//i++;

		int j;
		for (j = 0; j < i/2; j++) {
			int t = digits[j];
			digits[j] = digits[i-1-j];
			digits[i-1-j] = t;
		}

		int res = next_permutation(digits, digits + i);
		if (!res) {

			i = 0;
			number = n;
			while (number > 0) {
				digits[i] = number%10;
				number /= 10;
				i++;
			}
			digits[i] = 0;
			i++;

			for (j = 0; j < i/2; j++) {
				int t = digits[j];
				digits[j] = digits[i-1-j];
				digits[i-1-j] = t;
			}

			next_permutation(digits, digits + i);
		}

		cout << "Case #" << c << ": ";
		for (j = 0; j < i; j++) {
			printf("%d", digits[j]);	
		}
		printf("\n");

	}
	return 0;
}

