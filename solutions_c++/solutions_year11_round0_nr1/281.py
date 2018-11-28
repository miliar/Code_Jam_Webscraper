#include <iostream>
#include <cstdlib>
using namespace std;
int main() {
	int t;cin>>t;
	for(int a=1; a<=t; ++a) {
		int n;cin>>n;
		int ps[2]={1,1}, ts[2]={};
		while(n --> 0) {
			char x;
			int p;
			cin>>x>>p;
			int q = x=='O';
			ts[q] += abs(ps[q]-p)+1;
			ts[q] = max(ts[q],ts[!q]+1);
			ps[q] = p;
		}
		cout<<"Case #"<<a<<": "<<max(ts[0],ts[1])<<'\n';
	}
}
