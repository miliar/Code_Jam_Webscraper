/// Windows XP / Dev-C++ 4.9.9.2
#include <set>
#include <map>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

typedef long long llong;

const int nsize = 1000;
llong f[nsize];

int main() {
	/*
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-0.out", "w", stdout);
	//*/
	//*
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	//*/
	int Kase;
	llong p, k, l, sum, res, i;
	cin>>Kase;
	for ( int kase = 1; kase <= Kase; kase++ ) {
		cin>>p>>k>>l;
		for ( i = 0; i < l; i++ ) {
			cin>>f[i];
		}
		sort(f, f+l, greater<llong>());
		p = 0; sum = 0; res = 0;
		for ( i = 0; i < l; i++ ) {
			if ( 0 == i%k ) {
				res += sum * p;
				p++; sum = 0;
			}
			sum += f[i];
		}
		res += sum * p;
		cout<<"Case #"<<kase<<": "<<res<<endl;
	}
	return 0;
}
