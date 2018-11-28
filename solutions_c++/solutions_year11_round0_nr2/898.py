#include <iostream>
using namespace std;

char C['Z']['Z'], D['Z']['Z'];

int main() {
	int nc, ic;
	
	cin >> nc;
	for (ic = 1; ic <= nc; ic++) {
		int c, d, n, i, j, l = 0;
		char s[100], t;
		
		cin >> c;
		memset(C, 0, sizeof C);
		for (i = 0; i < c; i++) {
			cin >> s;
			C[s[0]][s[1]] = s[2];
			C[s[1]][s[0]] = s[2];
		}
		
		cin >> d;
		memset(D, 0, sizeof D);
		for (i = 0; i < d; i++) {
			cin >> s;
			D[s[0]][s[1]] = 1;
			D[s[1]][s[0]] = 1;
		}
		
		cin >> n;
		for (i = 0; i < n; i++) {
			cin >> t;
			s[l++] = t;
			while (l > 1 && (t = C[s[l - 2]][s[l - 1]])) s[--l - 1] = t;
			for (j = 0; j < l - 1; j++) if (D[s[j]][s[l - 1]]) l = 0;
		}
		
		cout << "Case #" << ic << ": [";
		for (i = 0; i < l; i++) cout << s[i] << (i + 1 < l ? ", " : "");
		cout << "]\n";
	}
	
	return 0;
}
