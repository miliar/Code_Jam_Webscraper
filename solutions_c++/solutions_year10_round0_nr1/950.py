#include <iostream>
using namespace std;
typedef long long int64;

int main() {
	int n,T;
	int64 k;
	cin>>T;
	for (int i=0;i<T;i++) {
		cin>>n>>k;
		cout<<"Case #"<<i+1<<": ";
		int64 x = 1;
		if ((k & (x<<(n-1)) !=0)&& ((k+1) % (x<<n) == 0)) cout<<"ON"<<endl; else cout<<"OFF"<<endl;
	}
}
