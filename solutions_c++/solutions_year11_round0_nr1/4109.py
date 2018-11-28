#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
	int t, i, n, m, e;
	cin >> t;
	char c;
	for (i = 0; i < t; ++i) {
		cin >> n;
		int p1 = 1, p2 = 1, t1 = 0, t2 = 0;
		for (e = 0; e < n; ++e) {
			do
				cin >> c;
			while (c != 'O' && c != 'B');
			cin >> m;
			if(c == 'O') {
				t1 += abs(m - p1);
				t1 = max(t1, t2);
				t1++;
				p1 = m;
			}
			else {
				t2 += abs(m - p2);
				t2 = max(t1, t2);
				t2++;
				p2 = m;
			}
		}
		cout<<"Case #"<<i+1<<": "<<max(t1, t2)<<endl;
	}
	return 0;
}
