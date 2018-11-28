#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
typedef unsigned int uint;

int main() {
	uint T;
	cin >> T;
	for (uint casenr = 1; casenr <= T; ++casenr) {
		uint A, B;
		vector< pair<uint, uint> > found;
		cin >> A >> B;

		uint len = 0; // #digits of A and B
		for (uint i = A; i; i /= 10) ++len;
		uint exp = 1;
		for (uint i = 1; i < len; ++i) exp *= 10;

		for (uint n = A; n <= B; ++n) {
			uint m = n;
			for (uint i = 1; i < len; ++i) {
				m = m / 10 + (m % 10) * exp;
				if (m <= n or m > B) continue;
				found.push_back( pair<uint,uint>(n,m) );
			}
		}

		sort(found.begin(), found.end());
		uint cnt = (found.empty()) ? 0 : 1;
		for (uint i = 1; i < found.size(); ++i) {
			if (found[i-1] != found[i]) ++cnt;
		}
		cout << "Case #" << casenr << ": " << cnt << endl;
	}
	return 0;
}
