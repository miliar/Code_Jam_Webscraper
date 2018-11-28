#include <iostream>

#define LL long long int

using namespace std;

int main() {
	int T;cin>>T;
	for(int iter = 0;iter<T;iter++) {
		LL N;
		cin >>N;
		LL x = 0;
		LL acc = 0;
		LL smallest = 10000000;
		for(int i=0;i<N;i++) {
			LL n; cin>>n;
			x^=n;
			acc+=n;
			smallest = min(smallest,n);
		}
		if(x)
			cout<<"Case #"<<iter+1<<": NO\n";
		else
			cout<<"Case #"<<iter+1<<": "<<acc-smallest<<"\n";
	}
}
