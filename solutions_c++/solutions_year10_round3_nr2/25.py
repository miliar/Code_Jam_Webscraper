#include <iostream>
#include <vector>
using namespace std;

int main(void) {
	int testCases;
	cin >> testCases;
	for (int curCase = 1; curCase <= testCases; curCase++) {
		long long l, p, c;
		cin >> l >> p >> c;
		long long groups = 0;
		while (l < p) {
			l *= c;
			++groups;
		}
		int res = 0;
		while (groups != 1) {
			++res;
			groups = (groups + 1) / 2;
		}
		cout << "Case #" << curCase << ": " << res << endl;
	}
	return 0;
}