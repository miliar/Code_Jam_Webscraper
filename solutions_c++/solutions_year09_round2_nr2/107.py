#include <iostream>

using namespace std;

string s;
string res;
int dd[11];
int n;



void Load()
{
	cin >> s;
	n = s.size();
	int i;
	for (i = 0; i < s.size(); i++) {
		dd[s[i] - '0']++;
	}
}



void Solve()
{
	int i, j, k;
	s = '0' + s;
	res = s;
	memset(dd, 0, sizeof(dd));
	for (i = (int)s.size() - 1; i >= 0; i--) {
		for (k = s[i] - '0' + 1; k <= 9; k++) {
			if (dd[k]) break;
		}
		if (k == 10) {
			dd[s[i] - '0']++;
		} else {
//			cerr << i << " " << res.substr(0, i + 1) << "\n";
//			for (j = 0; j < 10; j++) cerr << dd[j] << " ";
//			cerr << "\n";
			dd[s[i] - '0']++;
			res[i] = k + '0'; i++;
			dd[k]--;
			for (j = 0; j < 10; j++) {
				for (k = 0; k < dd[j]; k++) {
					res[i] = j + '0'; i++;
				}
			}
			break;
		}
	}
	if (res[0] == '0') res = res.substr(1, res.size() - 1);
	cout << res << "\n";
}



int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int tt, nt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++) {
		cout << "Case #" << tt << ": ";
		Load();
		Solve();
	}	
	return 0;
}