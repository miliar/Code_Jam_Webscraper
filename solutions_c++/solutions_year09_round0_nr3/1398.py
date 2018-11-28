#include <iostream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

int main () {
	
	int n;
	scanf ("%d",&n);

	string pattern = "welcome to code jam";
	string s;
	getline(cin,s);
	for (int T = 1; T <= n; T++) {
		getline(cin,s);		
		vector < vector < int > > S(pattern.size(), vector <int> (s.size(),0));
		for (int i = 0; i < pattern.size(); i++) {
			for (int j = 0; j < s.size(); j++) {
				if (s[j] == pattern[i]) {
					if (i == 0) {
						S[i][j] = 1;
					} else {
						for (int k = 0; k < j; k++) {
							if (s[k] == pattern[i-1]) {
								S[i][j] += S[i-1][k]%10000;
								S[i][j] = S[i][j]%10000;
							}
						}
					}
				}
			}
		}

		int tot = 0;
		for (int i = 0; i < S[18].size(); i++) {
			tot += S[18][i]%10000;
			tot = tot%10000;
		}
		stringstream ss;
		string ret;
		ss << tot;
		ss >> ret;
		int d = 4-ret.size();
		while (d--) ret = "0" + ret;
		cout << "Case #" << T << ": " << ret << "\n";
	}
	return 0;
}
