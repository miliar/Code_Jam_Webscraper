#include<iostream>
#include<string>
#include<vector>

using namespace std;

int main() {
	unsigned long long int T;
	cin>>T;
	for(unsigned long long int t=0;t<T;t++) {
		unsigned long long int P,L,C,ans=0;
		cin>>L>>P>>C;
		while(C*L<P) {
			C = C*C;
			ans++;
		}
		cout<<"Case #"<<t+1<<": "<<ans<<"\n";
	}
	return 0;
}
