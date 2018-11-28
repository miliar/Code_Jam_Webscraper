#include <iostream>
using namespace std;

int solve(int d, int K, int i) {
	for(;;) {
		int ipos = (i - 1) % (K + 1 - i) + 1;
		if(ipos == d) return i;
		if(ipos < d) {
			d -= ipos;
			++i;
		}
		else {
			d -= ipos;
			d += (K + 1 - i);
			++i;
		}
	}
}

int main() {
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": ";
		
		int K, n;
		cin >> K >> n;
		for(int i = 0; i != n; ++i) {
			int d;
			cin >> d;
			
			int sol = solve(d, K, 1);
			
			cout << sol;
			if(i == n-1) cout << endl;
			else cout << " ";
		}
	}
}
