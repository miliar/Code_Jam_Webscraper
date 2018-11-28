#include <iostream>
#include <iomanip>
using namespace std;

const int nmax = 100;
int n;
char a[nmax][nmax + 1];
typedef long double ld;
int op[nmax];
ld owp[nmax], r[nmax];

ld wp(int ip, int except = -1) {
	int i;
	ld r = 0;
	
	for (i = 0; i < n; i++) if (i != except) r += a[ip][i] == '1';
	
	return r / (op[ip] - (except != -1));
}

int main() {
	int nt, it;
	
	cin >> nt;
	for (it = 1; it <= nt; it++) {
		int i, j;
		
		cin >> n;
		for (i = 0; i < n; i++) {
			cin >> a[i];
			op[i] = 0;
			for (j = 0; j < n; j++) op[i] += a[i][j] != '.';
		}
		
		for (i = 0; i < n; i++) {
			owp[i] = 0;
			for (j = 0; j < n; j++) if (a[i][j] != '.') owp[i] += wp(j, i) / op[i];
		}
		
		cout << "Case #" << it << ":\n";
		for (i = 0; i < n; i++) {
			r[i] = 0;
			for (j = 0; j < n; j++) if (a[i][j] != '.') r[i] += owp[j] / op[i];
			r[i] = .25 * wp(i) + .50 * owp[i] + .25 * r[i];
			cout << setprecision(20) << r[i] << '\n';
		}
	}
	
	return 0;
}
