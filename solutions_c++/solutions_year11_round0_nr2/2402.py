#include <iostream>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

map <string, char> mp1;
map <string, bool> mp2;

string solve(string &s) {
	string ans;
	for(int i = 0; i < s.size(); i ++) {
		string tmp;
		if (ans.empty()) {
			ans.push_back(s[i]);
			continue;
		}
		tmp.push_back(ans[ans.size() - 1]);
		tmp.push_back(s[i]);
		if (mp1.count(tmp)) {
			ans.pop_back();
			ans.push_back(mp1[tmp]);
		}
		else {
			bool f = false;
			for(int j = 0; j < ans.size(); j ++) {
				string tmp;
				tmp.push_back(ans[j]);
				tmp.push_back(s[i]);
				if (mp2.count(tmp)) {
					ans.clear();
					f = true;
					break;
				}
			}
			if (!f)
				ans.push_back(s[i]);
		}
	}
	return ans;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for(int i = 0; i < t; i ++) {
		int c, d, n;
		mp1.clear();
		mp2.clear();
		string s;
		cin >> c;
		for(int j = 0; j < c; j ++) {
			cin >> s;
			char ch = s[2];
			char x, y;
			x = s[0];
			y = s[1];
			s.clear();
			s.push_back(x);
			s.push_back(y);
			mp1[s] = ch;
			reverse(s.begin(), s.end());
			mp1[s] = ch;
		}
		cin >> d;
		for(int j = 0; j < d; j ++) {
			cin >> s;
			mp2[s] = true;
			reverse(s.begin(), s.end());
			mp2[s] = true;
		}
		cin >> n >> s;
		string ans = solve(s);
		printf("Case #%d: [", i + 1);
		for(int j = 0; j < ans.size(); j ++) {
			cout << ans[j];
			if (j < ans.size() - 1)
				cout << ", ";
		}
		cout << "]\n";
	}
	return 0;
}