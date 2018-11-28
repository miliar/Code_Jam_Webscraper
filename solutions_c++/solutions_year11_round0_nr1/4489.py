#include <iostream>
#include <vector>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int test = 0; test < T; ++test) {
		int n;
		cin >> n;
		
		vector<char> a;
		vector<int> b;

		for (int j = 0; j < n; ++j) {
			char aa; int bb;
			cin >> aa >> bb;
			a.push_back(aa);
			b.push_back(bb);
		}

		int total = 0, last = 0;
		int posO = 1, posB = 1;
		for (int j = 0; j < n; ++j) {
			int m = 0;
			if (a[j] == 'O') {
				m = abs(posO - b[j]);
				if (j > 0 && a[j-1] != a[j]) {
					m = last >= m ? 0 : m-last;
				}
				posO = b[j];
			} else {
				m = abs(posB - b[j]);
				if (j > 0 && a[j-1] != a[j]) {
					m = last >= m ? 0 : m-last;
				}
				posB = b[j];
			}
			++m;
			if (j > 0 && a[j] == a[j-1])
				last += m;
			else
				last = m;
			total += m;
		}
		cout << "Case #" << test+1 << ": " << total << endl;
	}
	return 0;
}