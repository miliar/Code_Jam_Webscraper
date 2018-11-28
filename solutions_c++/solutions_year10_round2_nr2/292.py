#include <iostream>
using namespace std;
typedef long long ll;
ll N,K,B,T;
ll xs[1024];
ll vs[1024];
int main()
{
	int t;cin>>t;
	for(int a=1; a<=t; ++a) {
		cin>>N>>K>>B>>T;
		for(int i=0; i<N; ++i) cin>>xs[i];
		for(int i=0; i<N; ++i) cin>>vs[i];
		int ok=0,fail=0;
		ll r=0;
		for(int i=N-1; ok<K && i>=0; --i) {
			if (xs[i]+T*vs[i] >= B) {
				r += fail;
				++ok;
			} else {
				++fail;
			}
		}
		cout<<"Case #"<<a<<": ";
		if (ok==K) cout<<r;
		else cout<<"IMPOSSIBLE";
		cout<<'\n';
	}
}
