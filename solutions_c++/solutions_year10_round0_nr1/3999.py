#include<iostream>
using namespace std;

long long n, k, a, t;
int main() {
	cin>>t;
	for (int i=1; i<=t; i++) {
		cin>>n>>k;
		if (k == 0) {
			cout<<"Case #"<<i<<": OFF"<<endl;
			continue;
		}
		a = 1<<n;
		if (k%a == (a-1)) {
			cout<<"Case #"<<i<<": ON"<<endl;
		} else {
			cout<<"Case #"<<i<<": OFF"<<endl;
		}		
	}
	return 0;
}

