#include <iostream>
#include <cstdio>
using namespace std;
void fill(int number, int bitmap []) {
	while (number > 0) {
		int digit = number % 10;
		bitmap[digit] += 1;
		number /= 10;
	}
}

int equal(int bitmap [], int bitmaptest[]) {
	for(int a = 1; a < 10; ++a) {
		if (bitmaptest[a] != bitmap[a])
			return 0;
	}
	return 1;
}

int main () {
	int N;
	cin >> N;
	for(int a = 1; a <= N; ++a) {
		int bitmap[10];
		int bitmaptest[10];
		memset(bitmap, 0, 10*sizeof(int));
		int number;
		cin >> number;

		fill(number, bitmap);
		
		for(int b = number+1; 1; ++b) {
			memset(bitmaptest, 0, 10*sizeof(int));
			fill(b, bitmaptest);
			if (equal(bitmap, bitmaptest)) {
				cout << "Case #" << a << ": " << b << endl;
				break;
			}
		}
	}
}