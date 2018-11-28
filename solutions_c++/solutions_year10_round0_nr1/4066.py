#include <iostream>
using namespace std;

typedef unsigned long long int ulli;

bool result(ulli N, ulli K) {
	ulli KK = K;
	for(ulli i=0;i<N;i++) {
		if(KK%2 != 0)
			return false;
		KK = KK/2;
	}
	return true;
}

int main() {
	int T;
	ulli N,K;
	cin>>T;
	for(int cc=1;cc<=T;cc++) {
		cin>>N>>K;
		cout<<"Case #"<<cc<<": ";
		if(result(N,K+1))
			cout<<"ON";
		else
			cout<<"OFF";
		cout<<endl;
	}
	return 0;
}