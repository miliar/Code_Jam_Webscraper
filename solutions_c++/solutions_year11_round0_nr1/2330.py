#include <vector>
#include <algorithm>
#include <iostream>
#include <stdint.h>
#include <string>
#include <cmath>

using namespace std;

void Count(uint32_t c) {
	int32_t n;
	cin >> n;

	int32_t op = 1;
	int32_t bp = 1;
	
	int32_t bm = 0;
	int32_t om = 0;
	
	bool o, b;
	o = b = false;
	
	char r;
	int32_t nb;
	
	for (int32_t i = 0; i < n; i++) {
		cin >> r >> nb;
		
		if (r == 'O') {
			if (b) { // blue moved last
				if (om + abs(nb - op) <= bm) {
					om = bm + 1;
				}
				else {
					om += abs(nb - op) + 1;
				}
			}
			else {
				om += abs(nb - op) + 1;
			}
			op = nb;
			o = true;
		}
		else {
			if (o) {
				if (bm + abs(nb - bp) <= om) {
					bm = om + 1;
				}
				else {
					bm += abs(nb - bp) + 1;
				}
			}
			else {
				bm += abs(nb - bp) + 1;
			}
			bp = nb;
			b = true;
		}
	}
	
	cout << "Case #" << c << ": " << max(om, bm) << endl;
}

int main() {
	uint64_t n;
	cin >> n;

	for (uint32_t i = 1; i <= n; i++) {
		Count(i);
	}
	
	return 0;
}

