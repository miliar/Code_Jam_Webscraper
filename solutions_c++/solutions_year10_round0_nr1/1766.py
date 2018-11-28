#include <iostream>
#include <fstream>

using namespace std;

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T; cin>>T;
	for (int t=1; t<=T; t++) {
		long long n,k,r;
		cin>>n>>k;
		r=1;
		r = (r<<n)-1;
		cout<<"Case #"<<t<<": ";
		if (k>=r && (k-r)%(r+1)==0)
			cout<<"ON\n";
		else
			cout<<"OFF\n";
	}
}