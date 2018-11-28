#include <iostream>
#include <vector>
#include <string>

using namespace std;

string change(vector<int> v, string s, int k) {
	//cout << s << endl;
	string s2 = ""; int g = 0;
	for (unsigned int i = 0; i < s.length(); i++) {
		//cout << g << ' ' << i % k << ' ' << v[i%k] << ' ' << g + v[i % k] << endl;
		s2 += s[g + v[i % k]];
		if (i%k == k-1) g+=k;
		//cout << s2 << endl;
	}
	return s2;
}

int cnt(string s) {
	int changes = 1;
	for (unsigned int i = 0; i < s.length(); i++) {
		if (i!=0 && s[i-1]!=s[i]) changes++;
	}
	return changes;
}

int main(){
	int ntc; cin >> ntc;
	
	for (int tc = 1; tc <= ntc; tc++) {
		int k; string s; cin >> k >> s;
		vector<int> v;
		int min = 200000;
		for (int n = 0; n < k; n++) {
			v.push_back(n);
		}
		
		do {
			string s2 = change(v,s,k);
			int cc = cnt(s2);
			if (cc < min) min = cc;
		} while (next_permutation(v.begin(), v.end()));
		
		cout << "Case #" << tc << ": " << min << endl;
	}
	
	return 0;
}