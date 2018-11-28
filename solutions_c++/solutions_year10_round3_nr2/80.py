#include <iostream>

using namespace std;

int main() {
	int t;
	cin>>t;
	for (int cc=1;cc<=t;++cc) {
		long long l,p,c;
		cin>>l>>p>>c;
		int k=0;
		while (l*c<p) {
			c*=c;
			k++;
		}
		cout<<"Case #"<<cc<<": "<<k<<endl;
	}
	return 0;
}
