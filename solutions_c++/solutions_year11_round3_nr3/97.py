#include <iostream>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <map>
#include <string>
using namespace std;
typedef __int64 ll;
const int N=1100000;
int tests,t,r,c;
int n,l,h,a[200];
int main () {
#ifndef ONLINE_JUDGE
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);
#endif
	cin>>tests;
	for (t=1; t<=tests; t++) {
		cin>>n>>l>>h;
		for (int i=1; i<=n; i++) cin>>a[i];
		int ans=0;
		for (int i=l; i<=h; i++) {
			int ok=1;
			for (int j=1; j<=n; j++)
				if (a[j]%i!=0 && i%a[j]!=0) {
					ok=0;
					break;
				}
			if (ok) {
				ans=i;
				break;
			}
		}
		cout<<"Case #"<<t<<": ";
		if (ans) {
			cout<<ans<<endl;
		} else cout<<"NO"<<endl;
	}
}