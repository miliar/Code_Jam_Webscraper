#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

typedef vector<int> Vi;

int main() {
	int t;
	cin >> t;
	for(int i = 0; i < t; ++i) {
		int n;
		cin >> n;
		Vi v(n);
		for(int j = 0; j < n; ++j) {
			int a;
			cin >> a;
			v[j] = a;
		}
		sort(v.begin(),v.end());
		Vi v1(n);
		v1[0] = v[0];
		for(int j = 1; j < n; ++j) v1[j] = v1[j-1] ^ v[j];
		Vi v2(n);
		v2[0] = v[n-1];
		for(int j = 1; j < n; ++j) v2[j] = v2[j-1] ^ v[n-j-1];
		bool found = false;
		cout << "Case #"<< i+1 << ": ";
		for(int j = 0; j+1 < n and not found; ++j) {
			if(v1[j] == v2[n-j-2]) {
				long long sum = 0;
				for(int k = j+1; k < n; ++k) sum += v[k];
				cout << sum << endl;
				found = true;
			}
		}
		if(not found) cout << "NO" << endl;
	}
}