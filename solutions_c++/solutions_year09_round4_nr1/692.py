#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <list>
#include <algorithm>
using namespace std;

char a[100][100];
int m[100];

int main() {
	freopen("inputa.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; ++tt) {
		cout << "Case #" << tt << ": ";
		int n;
		cin >> n;
		fill(m, m+100, 0);
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				cin >> ws >> a[i][j] >> ws; 
			}
			for (int j = n-1; j >= 0; --j) {
				if (a[i][j] == '1') {
					m[i] = j+1;
					break;
				}
			}
		}
		int cnt = 0;
		for (int i = 0; i < n; ++i) {
			if (m[i] > i+1) {
				int j = i;
				while (m[j] > i+1) {
					++j;
					++cnt;
				}
				int t = m[j];
				for (int k = j; k > i; --k) {
					m[k] = m[k-1];
				}
				m[i] = t;				
			}
		}
		cout << cnt << endl;		
	}
	return 0;
}