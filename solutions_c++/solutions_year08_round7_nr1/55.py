#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <iomanip>

using namespace std;

map<string, vector<string> > mp;
map<string, int> dp;

#define MAX 100000
bool bowl[MAX];

bool upper(char c) {
	return (c >= 'A' && c <= 'Z');
}

int cnt = 0;

int num(string s) {
	int i, j;
	if (dp.find(s) != dp.end()) return dp[s];
	vector<string> v=mp[s];
	int ma=1;
	vector<int> vec;
	for (i=0; i<v.size(); i++) {
		if (upper(v[i][0])) {
			int r = num(v[i]);
			vec.push_back(r);
		}
	}
	sort(vec.begin(), vec.end());
	for (i=vec.size()-1; i>=0; i--) {
		int t = vec[i]+vec.size()-1-i;
		//cout << vec[i] << " " << vec.size() << " " << i << endl;
		//cout << t << endl;
		if (t > ma) ma = t;
		if (t > cnt) cnt = t;
	}
	int t = vec.size() + 1;
	//cout << t << endl;
	if (vec.size()+1 > ma) ma = vec.size()+1;
	if (t > cnt) cnt = t;
	dp[s] = ma;
	return ma;
}

int main () {
	int T, cse=0;
	cin >> T;
	int n;
	int i, j, k;

	while (T--) {
		cin >> n;
		cnt = 0;
		mp.clear();
		dp.clear();
		string s1, s2;
		int m=0;
		string st;
		//cout << "woot" << endl;
		for (i=0; i<n; i++) {
			cin >> s1 >> m;
			if (i==0) st = s1;
			vector<string> v;
			for (j=0; j<m; j++) {
				cin >> s2;
				v.push_back(s2);
			}
			mp[s1] = v;
		}
		//cout << "ok" << endl;
		num(st);
		map<string, int>::iterator it;
		for (it=dp.begin(); it!=dp.end(); it++) {
			//cout << it->first << " " << it->second << endl;
		}
		cout << "Case #" << ++cse << ": " << cnt << endl;
	}
	return 0;
}
