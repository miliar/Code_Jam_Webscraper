#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin>>t;
	for (int nt = 1; nt <= t; ++nt) {
		int x[10], y[10], r[10];
		int n;
		cin>>n;
		for (int i = 0; i < n; ++i)
			cin>>x[i]>>y[i]>>r[i];
		if (n > 3)
			continue;

		cout<<"Case #"<<nt<<": ";
		if (n == 1) 
			cout<<r[0]<<endl;
		else if (n == 2)
			cout<<max(r[0], r[1])<<endl;
		else {
			double ret = 1.0e9;
			for (int i = 0; i < n; ++i)
				for (int j = i + 1; j < n; ++j) {
					double dist = sqrt((double)(x[i] - x[j]) * (x[i] - x[j]) + (double)(y[i] - y[j]) * (y[i] - y[j]));
					double req = max((dist + r[i] + r[j]) / 2, (double)r[3 - i - j]);
					ret = std::min(ret, req);
				}
			cout<<ret<<endl;
		}
	}
	return 0;
}
