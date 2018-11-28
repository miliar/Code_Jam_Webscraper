#include <cstdio>
#include <cstdlib>
#include <cstring>
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

// Perpetual Motion

long long isqrt(long long x)
{
	if (x <= 0) {
		return 0;
	}
	long long s = 1;
	long long t = x;
	while (s < t) {
		s <<= 1;
		t >>= 1;
	}
	do {
		t = s;
		s = (x / s + s) >> 1;
	} while (s < t);

	return t;
}

int main()
{
	int cases;
	cin >> cases;

	for (int caseno = 1; caseno <= cases; caseno++) {
		string s;
		cin >> s;
		for (int b = 0; b < 1 << 20; b++) {
			long long num = 0;
			int d = 0;
			for (int i = 0; i < s.size(); i++) {
				num *= 2;
				if (s[i] == '1') {
					num++;
				} else if (s[i] == '?') {
					if (!(b & (1 << d))) {
						num++;
					}
					d++;
				}
			}
			long long sq = isqrt(num);
			if (sq * sq == num) {
				cout << "Case #" << caseno << ": ";
				int d = 0;
				for (int i = 0; i < s.size(); i++) {
					if (s[i] == '?') {
						cout << ((b & (1 << d)) ? '0' : '1');
						d++;
					} else {
						cout << s[i];
					}
				}
				cout << endl;
				break;
			}
		}
	}

	return 0;
}
