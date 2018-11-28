#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;
int main()
{
	int t;cin>>t;
	for(int a=1; a<=t; ++a) {
		string s;
		cin>>s;
		ll ignore=0;
		ll val=0;
		reverse(s.begin(),s.end());
		for(size_t i=0; i<s.size(); ++i) {
			char c = s[i];
			if (c=='?') ignore |= 1LL<<i;
			else if (c=='1') val |= 1LL<<i;
		}
		ll i=1;
		for(; ; ++i) {
			ll x = i*i;
//			cout<<"testing "<<x<<' '<<val<<' '<<ignore<<'\n';
			if (((x^val)&~ignore) == 0) break;
		}
		string b;
		ll x=i*i;
		while(x) {
			b += '0' + (x&1);
			x >>= 1;
		}
		reverse(b.begin(),b.end());
		cout<<"Case #"<<a<<": "<<b<<'\n';
	}
}
