#include <iostream>
#include <stdint.h>
#include <string>
#include <cstring>

using namespace std;

int main() {
	int32_t t;
	
	cin >> t;

	for (int32_t j = 0; j < t; j++) {
		int32_t n, s, p;
		cin >> n >> s >> p;
		
		uint32_t c = 0;
		uint32_t a;
		for (int32_t i = 0; i < n; i++) {
			cin >> a;
			if (3 * p <= a) {
				c++;
				continue;
			}
			else if (3 * p - 2 <= a) {
				c++;
			}
			else if(s > 0 && 3 * p - 4 <= a) {
				c++;
				s--;
			}
		}
		
		cout << "Case #" << j + 1 << ": " << c << endl;
	}
}
