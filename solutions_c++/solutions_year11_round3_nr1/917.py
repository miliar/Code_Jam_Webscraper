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

void Do(uint32_t i) {
	uint32_t h, w;
	
	char m[50][50];
	
	cin >> h >> w;
	for (uint32_t y = 0; y < h; y++) {
		for (uint32_t x = 0; x < w; x++) {
			cin >> m[x][y];
		}
	}
	
	bool intile = false;
	for (uint32_t x = 0; x < w; x++) {
		for (uint32_t y = 0; y < h; y++) {
			if (m[x][y] == '#' && (h > y + 1 && m[x][y + 1] == '#') && (w > x + 1 && m[x + 1][y] == '#') && m[x + 1][y + 1] == '#') {
				m[x][y] = '/';
				m[x][y + 1] = '\\';
				m[x + 1][y] = '\\';
				m[x + 1][y + 1] = '/';
			}
		}
	}

	for (uint32_t x = 0; x < w; x++) {
		for (uint32_t y = 0; y < h; y++) {
			if (m[x][y] == '#') {
				cout << "Case #" << i << ":" << endl << "Impossible" << endl;
				return;
			}
		}
	}
	
	cout << "Case #" << i << ":" <<endl;
	for (uint32_t y = 0; y < h; y++) {
		for (uint32_t x = 0; x < w; x++) {
			cout << m[x][y];
		}
		cout << endl;
	}
}

int main() {
	uint32_t n;
	cin >> n;
	
	for (uint32_t i = 1; i <= n; i++) {
		Do(i); 
	}
	
	return 0;
}
