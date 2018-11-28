#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
	int t;
	cin >> t;
	for(int i = 0; i < t;) {
		string s;
		cin >> s;
		int b = 1;
		vector<int> n;
		n.push_back(1);
		for(int j = 1; j < s.size(); j++) {
			if(s[j] == s[j - 1]) n.push_back(1);
			else break;
		}
		if(n.size() < s.size()) {
			n.push_back(0);
		}
		for(int j = n.size(); j < s.size(); j++) {
			int k = 0;
			for(; k < j; k++)
				if(s[k] == s[j]) {
					n.push_back(n[k]);
					break;
				}
			if(k >= j) {
				n.push_back(++b);
			}
		}
		b++;
		long long r = 0, weight = 1;
		for(int j = n.size(); j-- > 0;) {
			r += weight * n[j];
			weight *= b;
		}
		cout << "Case #" << ++i << ": " << r << endl;
	}
	return 0;
}
