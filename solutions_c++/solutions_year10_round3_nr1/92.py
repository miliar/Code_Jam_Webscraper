#include <iostream>
using namespace std;

int n;
const int nmax = 1000;
int a[nmax], b[nmax];

int main() {
	int nt, it;
	
	for (cin >> nt, it = 0; it < nt; it++) {
		int i, j, r = 0;
		
		cin >> n;
		for (i = 0; i < n; i++) {
			cin >> a[i] >> b[i];
			for (j = 0; j < i; j++) if (a[j] < a[i] && b[j] > b[i] || a[j] > a[i] && b[j] < b[i]) r++;
		}
		
		cout << "Case #" << it + 1 << ": " << r << '\n';
	}
	
	return 0;
}
