#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <fstream>

using namespace std;

int main() {
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out", "wt", stdout);
	int T;
	cin>>T;
	int n;
	long long res;
	for(int i = 1; i <= T; i++) {
		res = 0;
		cin >> n;
		vector<int> a(n);
		vector<int> b(n);
		for(int j = 0; j < n; j++) {
			cin>>a[j];
		}
		for(int j = 0; j < n; j++) {
			cin>>b[j];
		}
		sort(a.begin(),a.end());
		sort(b.begin(),b.end());
		for(int j = 0; j < n; j++) {
			res += (long long)(a[j]) * b[n-1-j];
		}
		cout<<"Case #"<<i<<": "<<res<<endl;
	}
	return 0;
}