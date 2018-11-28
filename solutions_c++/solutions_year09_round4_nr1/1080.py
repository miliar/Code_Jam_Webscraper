#include <iostream>
#include <algorithm>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int t, n;
vector< int > k;
string te;

int main() {
	ifstream cin("A-large.in");
	ofstream cout("name1.out");
	cin >> t;
	for (int ts=0;ts<t;ts++) {
		cin >> n;
		k.clear();
		for (int j=0;j<n;j++) {
			cin >> te;
			bool t = false;
			for (int i=n-1;i>=0;i--) {
				if (te[i] == '1') {
					k.push_back(i);
					t = true;
					break;
				}
			}
			if (!t)
				k.push_back(0);
		}
		int ret = 0;
		for (int i=0;i<n;i++) {
			if (k[i] <= i)
				continue;
			int j;
			for (j=i+1;j<n;j++) {
				if (k[j] <= i) {
					break;
				}
			}
			ret += abs(i-j);
			while (j > i) {
				swap(k[j], k[j-1]);
				j--;
			}
		}
		cout << "Case #" << ts+1 << ": " << ret << endl;
	}
	return 0;
}