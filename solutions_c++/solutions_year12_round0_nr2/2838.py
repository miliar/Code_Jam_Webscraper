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
main() {
	freopen("B-large.in","r",stdin);
	freopen("test.out","w",stdout);
	ll nTest,x,n,s,p,ans;
	cin >> nTest;
	FOR (test,1,nTest) {
		printf("Case #%d: ",test);
		ans =0;
		cin >> n >> s >> p;
		FOR (i,1,n) {
			cin >> x;
			if (x>=p*3) ans++; else
			if (x>=p*3-2 && x>=1) ans++; else 
				if (x>=p*3-4 && s && x>=2) {
					ans++;
					s--;
				}
		}
		cout << ans << endl;
	}
}
