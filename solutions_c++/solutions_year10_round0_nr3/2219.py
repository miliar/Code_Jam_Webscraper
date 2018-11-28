#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int main() {
	long long t, r, k, n, i, res, cur, s;
	long long a[1<<10];
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	cin>>t;
	for(int nt = 1; nt <= t; ++nt) {
		cin>>r>>k>>n;
		cur = 0;
		for(i=0; i<n; ++i) {
			cin>>a[i];
			cur += a[i];
		}
		if (cur <= k) {
			cout<<"Case #"<<nt<<": "<<cur*r<<endl;
			continue;
		}
		res = 0;
		cur = 0;
		for(; r>0; --r) {
			s = 0;
			while(s + a[cur] <= k) {
				s+=a[cur];
				cur = (cur+1)%n;
			}
			res += s;
		}
		cout<<"Case #"<<nt<<": "<<res<<endl;
	}
	return 0;
}