#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <sstream>
using namespace std;

string line;
string s = "welcome to code jam";

int f[1001][32];

int calc()
{
	if (line.length() == 0) return 0;

	int i, j;
	for (j=1; j<s.length(); ++j) {
		f[0][j] = 0;
	}
	f[0][0] = s[0]==line[0];

	for (i=1; i<line.length(); ++i) {
		f[i][0] = f[i-1][0] + (line[i]==s[0]);
		//cout << f[i][0];
		for (j=1; j<s.length(); ++j) {
			if (line[i] != s[j]) {
				f[i][j] = f[i-1][j];
			} else {
				f[i][j] = f[i-1][j-1] + f[i-1][j];
				f[i][j] %= 10000;
			}
			//cout << ' ' << f[i][j];
		}
		//cout << endl;
	}

	return f[line.length()-1][s.length()-1];

	/*
	int ans = 0;
	for (i=0; i<line.length(); ++i) {
		ans += f[i][s.length()-1];
		ans %= 1000;
	}

	cout << ans << endl;

	return ans;
	*/
}

string format(int a)
{
	stringstream S;
	S << a;
	string s = S.str();
	while (s.length() < 4) s = '0'+s;
	return s;
}


int main(void)
{
	int T;
	cin >> T;
	getline(cin, line);
	for (int ca=1; ca<=T; ++ca) {
		getline(cin, line);
		cout << "Case #" << ca << ": " << format(calc()) << endl;
	}
	return 0;
}
