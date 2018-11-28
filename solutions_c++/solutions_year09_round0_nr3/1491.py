#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <list>
using namespace std;

int main() {
	freopen("inputc.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int t;
	cin >> t >> ws;
	int cnt = 0;
	string p = "welcome to code jam";
	while (t--) {
 		++cnt;
		cout << "Case #" << cnt << ": ";
		string s;
		getline(cin, s);
		//cout << s << endl;
		//cout.flush();
		vector<vector<int> > v(s.size() + 1);
		for (int i = 0; i < v.size(); ++i)
			v[i].resize(p.size() + 1);
		v[0][0] = 1;
		for (int i = 1; i <= s.size(); ++i) {
		  v[i][0] = v[i-1][0];
			for (int j = 1; j <= p.size(); ++j) {
			 v[i][j] = v[i-1][j];
			 if (s[i-1] == p[j-1]) {
			  v[i][j] += v[i-1][j-1];
			 } 
			 if (v[i][j] > (1 << 20))
				 v[i][j] %= 10000;
	 	  }	
		}
		int ans = v[s.size()][p.size()] % 10000;
		cout << (ans / 1000) << (ans / 100 % 10) << (ans / 10 % 10) << (ans % 10) << endl;
	}

	return 0;
}
