#include <iostream>
using namespace std;
typedef long long ll;
int main()
{
	int t;cin>>t;
	for(int a=1; a<=t; ++a) {
		ll n,d,g;
		cin>>n>>d>>g;
		cout<<"Case #"<<a<<": ";
		if (g==100) {
			if (d==100) {
				cout<<"Possible\n";
			} else {
				cout<<"Broken\n";
			}
		} else if (g==0) {
			if (d==0) {
				cout<<"Possible\n";
			} else {
				cout<<"Broken\n";
			}
		} else {
			ll k = min(100LL,n);
			bool ok=0;
			for(ll i=1; i<=k; ++i) {
				if (d*i % 100==0) {
//					cout<<"ok: "<<d<<' '<<i<<'\n';
					cout<<"Possible\n";
					ok=1;
					break;
				}
			}
			if (!ok) cout<<"Broken\n";
		}
	}
}
