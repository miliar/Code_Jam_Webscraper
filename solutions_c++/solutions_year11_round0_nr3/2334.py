#include <vector>
#include <algorithm>
#include <iostream>
#include <stdint.h>
#include <string>
#include <cmath>
#include <cstring>

using namespace std;

void Solve(int32_t t) {
	uint64_t n, a;
	uint64_t totx, tot;
	tot = totx = 0;
	
	//uint32_t s1, x1, s2, x2;
	uint64_t mn = 0xFFFFFFFF;
	
	cin >> n;
	for (uint32_t i = 0; i < n; i++) {
		cin >> a;
		if (a < mn) mn = a;
		totx ^= a;
		tot += a;
	}
	
	if (totx != 0) {
		cout << "Case #" << t << ": NO" << endl;
		return;
	}
	else {
		cout << "Case #" << t << ": " << (tot - mn) << endl;
	}
}

int main() {
	int32_t t;
	cin >> t;

	for (int32_t i = 1; i <= t; i++) {
		Solve(i);
	}
	
	return 0;
}

