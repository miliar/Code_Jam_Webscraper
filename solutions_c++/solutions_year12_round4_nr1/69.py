#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

const int nmax = 10000;
int N;
int d[nmax + 1], l[nmax + 1], m[nmax + 1];

int main() {
	int nt, it;

	cin >> nt;
	for (it = 1; it <= nt; it++) {
		memset(m, 0, sizeof m);
		
		int i, j;

		cin >> N;
		for (i = 0; i < N; i++) {
			cin >> d[i] >> l[i];
		}
		cin >> d[N];
		l[N] = 0;
		m[N] = -1;

		m[0] = d[0];
		for (i = 0; i <= N; i++) {
			for (j = i; j--; ) if (m[j] >= d[i] - d[j]) {
				m[i] = max(m[i], min(d[i] - d[j], l[i]));
			}
// 			cout << i << ": " << m[i] << endl;
		}

		cout << "Case #" << it << ": " << (m[N] ? "NO" : "YES") << endl;
	}
	
	return 0;
}
