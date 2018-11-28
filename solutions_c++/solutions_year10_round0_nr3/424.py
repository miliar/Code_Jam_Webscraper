#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

int main () {
	freopen("C-large.in","r",stdin);
	freopen("C.out","w",stdout);
	int t;
	cin >> t;
	for (int ii=1;ii<=t;ii++) {
		vector<int> a,b,c;
		int r,k,n;
		cin >> r >> k >> n;
		a.clear(); a.resize(n);
		b.clear(); b.resize(n);
		c.clear(); c.resize(n);
		for (int i=0;i<n;i++) cin >> a[i];
		for (int i=0;i<n;i++) {
			int sum=k,j=i;
			while (sum>=a[j]) {
				sum-=a[j];
				j++;
				if (j==n) j=0;
				if (j==i) break;
			}
			b[i]=j;
			c[i]=k-sum;
		}
		long long res=0,tek=0;
		for (int i=0;i<r;i++) {
			res+=c[tek];
			tek=b[tek];
		}
		cout << "Case #" << ii << ": " << res << endl;
		cerr << "Case #" << ii << ": " << res << endl;
	}
	return 0;
}
