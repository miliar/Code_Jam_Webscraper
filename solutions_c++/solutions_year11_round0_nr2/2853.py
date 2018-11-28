#include <iostream>

using namespace std;

int main()
{
	int t;
	int c, d, n, i, j, k;
	char last = '0';
	int flag;
	string s;
	string sol;
	cin >> t;

	for ( k = 1; k <= t; k++ ) {
		cin >> c;
		
		char m1[255] = {0}, m2[255] = {0};
		char o1[255] = {0};
		
		last = '0';

		while (c--) {
			cin >> s;

			m1[s[0]] = s[1];
			m1[s[1]] = s[0];
			m2[s[0]] = m2[s[1]] = s[2];
		}
		
		cin >> d;

		while (d--) {
			cin >> s;
			o1[s[0]] = s[1];
			o1[s[1]] = s[0];
		}

		cin >> n;

		cin >> s;
		
		last = s[0];
		sol = "";
	        sol += s[0];

		for ( i = 1; i < s.size(); i++ ) {
			if ( m1[s[i]] == last || m1[last] == s[i] ) {
				sol[sol.size() - 1] = m2[last];
				last = sol[sol.size() - 1];
			} else {
				flag = 0;

				if ( o1[s[i]] != 0 ) {
					for ( j = sol.size() - 1; j >= 0; j-- ) {
						if ( sol[j] == o1[s[i]] ) {
							sol = "";
							flag = 1;
							last = '0';
							break;
						}
					}
				}

				if ( flag != 1 ) {	
					sol += s[i];
					last = s[i];
				}				
			}
		}

		cout << "Case #" << k << ": [";
		for ( i = 0; sol.size() != 0 && i < sol.size() - 1; i++ ) {
			cout << sol[i] << ", ";
		}
		if ( sol.size() > 0 )
			cout << sol[sol.size() - 1];

				cout << "]" << endl;
	}

	return 0;
}
