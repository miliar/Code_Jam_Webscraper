#include <iostream>
#include <vector>
#include <string>

using namespace std;

const int nmax = 10;
int y[1 << nmax], z[1 << nmax];

int main() {
	int nt, it;
	
	cin >> nt;
	for (it = 1; it <= nt; it++) {
		int m, n, i, j, k, c, r = 0;
		
		cin >> m >> n;
		
		vector<string> s(m);
		int d[nmax + 1][1 << nmax] = {0}, x[nmax] = {0};
		
		// sagatavo aizliegtos šablonus
		memset(y, 0, sizeof y);
		for (i = 0; i < 1 << n; i++) {
			for (j = 0; j < n; j++) if (j && (i & (1 << (j - 1))) || j < n - 1 && (i & (1 << (j + 1)))) y[i] |= 1 << j;
		}
		// nedrīkst taču blakus arī
		for (i = 0; i < 1 << n; i++) {
			for (j = 1; j < n; j++) if ((i & (1 << j)) && (i & (1 << (j - 1)))) z[i] = 1;
		}
		for (i = 0; i < m; i++) cin >> s[i];
		for (j = 0; j <= m; j++) for (i = 0; i < 1 << n; i++) d[0][i] = -1000000000;
		d[0][0] = 0;
		for (i = 0; i < m; i++) {
			for (j = 0; j < n; j++) if (s[i][j] == 'x') x[i] |= 1 << j;
			for (j = 0; j < 1 << n; j++) if (!z[j] && !(j & x[i])) { // sēdināsim i+1-jā rindā šādi
				c = 0;
				for (k = 0; k < n; k++) if (j & (1 << k)) c++;
				for (k = 0; k < 1 << n; k++) if (!(j & y[k])) { // pa visiem pieļaujamajiem i-ās rindas sēdinājumiem
					d[i + 1][j] >?= d[i][k] + c;
				}
			}
		}
		for (i = 0; i < 1 << n; i++) r >?= d[m][i];
		
		cout << "Case #" << it << ": " << r << '\n';
	}
	
	return 0;
}
