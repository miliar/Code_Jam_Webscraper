#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
using namespace std;
typedef long long ll;

ll a1[1024], a2[1024];
ll gcd(ll n, ll m){
	if(m == 0)return n;
	return gcd(m, n%m);
}

int main(){
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	int T;
	int n;
	cin>>T;
	for(int tt = 1; tt <= T; ++tt){
		cin>>n;
		for(int i = 0; i < n; ++i)
			cin>>a1[i];
		sort(a1, a1+n);
	//	for(int i = 0; i < n; ++i)
	//		cout<<i<<' '<<a1[i]<<endl;
		for(int i = 1; i < n; ++i)
			a2[i] = a1[i]-a1[i-1];
	//	for(int i = 1; i < n; ++i)
	//		cout<<a2[i]<<endl;
		ll g = a2[1];
		for(int i = 2; i < n; ++i)
			g = gcd(g, a2[i]);
		cout<<"Case #"<<tt<<": ";
		cout<<(g-a1[0]%g)%g<<endl;
	}
	return 0;	
}
