#include <iostream>
#include <map>
#include <utility>

using namespace std;

map<pair<string, int>, int> M;

int solvei(string s, int i) {
	if (M.find(make_pair(s,i)) != M.end()) return M[make_pair(s,i)];
	string t = "welcome to code jam";
	int total = 0;	

	if (i == t.length()) return 1;
	if (s.length() == 0) return 0;
	if (s[0] == t[i]) total += solvei(s.substr(1), i + 1) % 10000; 
	total += solvei(s.substr(1), i) % 10000;

	M[make_pair(s,i)] = total;

	return total % 10000;
}

void solve(string s) {
	M.clear();
	int total = solvei(s, 0);
	if (total < 10) cout << "000" << total;
	else if (total < 100) cout << "00" << total;
	else if (total < 1000) cout << "0" << total;
	else if (total < 10000) cout << "" << total;
}

int main() {
	int n; cin >> n;
	string dummy; getline(cin, dummy);

	for (int i = 0; i < n; i++){
		string s; getline(cin, s);
		cout << "Case #" << (i+1) << ": ";
		solve(s);
		cout << endl; 	
	}

	return 0;
}
