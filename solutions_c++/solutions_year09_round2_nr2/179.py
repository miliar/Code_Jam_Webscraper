#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
	int t;
	cin >> t;
	for (int T=1; T<=t; T++) {
		string x;
		vector<int> y(10, -1);
		cin >> x;
		y[x[x.size()-1]-'0'] = x.size()-1;
		bool found = false;
		for (int i=x.size()-2; i>=0 && !found; i--) {
			y[x[i]-'0'] = i;
			for (int j=x[i]+1; j<='9' && !found; j++)
				if (y[j-'0'] != -1) {
					int idx = y[j-'0'];
					swap(x[i], x[idx]);
					sort(x.begin()+i+1, x.end());
					found = true;
				}
		}
		if (!found) {
			sort(x.begin(), x.end());
			int idx;
			for (idx=0; x[idx]=='0'; idx++);
			char first = x[idx];
			x.erase(idx, 1);
			x = string("") + first + "0" + x;
		}
		cout << "Case #" << T << ": " << x << "\n";
	}
	return 0;
}