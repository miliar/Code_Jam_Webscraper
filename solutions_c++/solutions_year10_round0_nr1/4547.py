#include <iostream>
#include <vector>
using namespace std;
int main() {
	int t;
	unsigned long n, k;
	cin >> t;
	for (int xx=1; xx <= t; xx++) {
		cin >> n >> k;
		cout << "Case #" << xx << ": "; 
		vector<bool> v(n, false);
		for (; k>0; k--) {
			int i=0;
			while (i<v.size() && v[i]) {
				v[i] = false;
				i++;
			}
			if (i < v.size()) v[i] = true;
		}
		bool qq = true;
		for (int i=0; i<v.size(); i++)
			qq = qq && v[i];
		cout << (qq?"ON":"OFF") << endl;
	}
	return 0;
}
