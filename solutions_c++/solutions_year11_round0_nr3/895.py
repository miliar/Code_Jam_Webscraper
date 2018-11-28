#include <iostream>
using namespace std;

int main() {
	int nc, ic;
	
	cin >> nc;
	for (ic = 1; ic <= nc; ic++) {
		int n, c, x = 0, s = 0, m = 1E6;
		
		cin >> n;
		while (n--) cin >> c, x ^= c, s += c, m <?= c;
		
		cout << "Case #" << ic << ": ";
		if (x) cout << "NO"; else cout << s - m;
		cout << '\n';
	}
	
	return 0;
}
