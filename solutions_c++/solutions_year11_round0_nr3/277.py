#include <iostream>
using namespace std;
int main()
{
	int t;cin>>t;
	for(int a=1; a<=t; ++a) {
		int n;cin>>n;
		int t=0,o=0,s=1e9;
		while(n --> 0) {
			int x;cin>>x;
			t += x;
			o ^= x;
			s = min(s,x);
		}
		cout<<"Case #"<<a<<": ";
		if (o==0) cout<<t-s<<'\n';
		else cout<<"NO\n";
	}
}
