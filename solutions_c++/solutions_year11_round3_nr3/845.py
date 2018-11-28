#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <cmath>
#include <stdint.h>
#include <cstring>
#include <cassert>
#include <iomanip>

using namespace std;

void Do(uint32_t c) {
	uint32_t cc[10001];
	memset(cc, 0, sizeof(cc));
	
	uint64_t n, l, h;
	cin >> n >> l >> h;
	
	uint64_t freq;
	for (uint32_t i = 0; i < n; i++) {
		cin >> freq;
		
		for (uint32_t j = l; j <= h; j++) {
			if (j > freq) {
				if (j % freq == 0) {
					cc[j]++;
				}
			}
			else {
				if (freq % j == 0) {
					cc[j]++;
				}
			}
		}
	}
	

	for (uint32_t j = l; j <= h; j++) {
		if (cc[j] == n) {
			cout << "Case #" << c << ": " << j << endl;
			return;
		}
	}
	
	cout << "Case #" << c << ": NO" << endl;
}

int main() {
	uint32_t n;
	cin >> n;
	
	for (uint32_t i = 1; i <= n; i++) {
		Do(i); 
	}
	
	return 0;
}
