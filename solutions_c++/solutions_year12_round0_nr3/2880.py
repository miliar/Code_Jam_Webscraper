#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <vector>
#define ll long
#define FOR(i,a,b) for(ll i=a;i<=b;i++)
#define FO(i,a,b) for(ll i=a;i<b;i++)
#define FORD(i,a,b) for(ll i=a;i>=b;i--)
#define FOD(i,a,b) for(ll i=a;i>b;i--)
#define pb push_back
#define mp make_pair
using namespace std;
ll 	check(string x,string a,string b) {
	string s;
	int dem,j,ans=0;
	FO (i,0,x.size()) {
		s="";
		dem=x.size();
		j=i;
		do {
			s.pb(x[j]);
			j=(j+1)%x.size();
		}	while (j!=i);
		if (s>=a && s<=b && x<s) {
			//cout << x << " " << s << endl;
			ans++;
		}
	}
	return ans;
}
ll num(string s) {
	ll ans=0;
	FO (i,0,s.size())
		ans=ans*10+(s[i]-'0');
	return ans;
}
string str(ll x) {
	string ans;
	while (x>0) {
		ans = char(x%10+(int)'0') + ans;
		x/=10;
	}
	return ans;
}
main() {
	freopen("C-small-attempt0.in","r",stdin);
	freopen("test.out","w",stdout);
	ll nTest,ans;
	cin >> nTest;
	string a,b;
	FOR (test,1,nTest) {
		printf("Case #%d: ",test);
		ans=0;
		cin >> a >> b;
		ll x=num(a);
		ll y=num(b);
		FOR (i,x,y)
			ans += check(str(i),a,b);
		cout << ans << endl;
	}
}
