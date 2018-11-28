#include <iostream>
using namespace std;

#include <cmath>

int main(){
	int T;
	cin >> T;
	for (int c=1; c<=T; c++){
		int N,K; cin>>N>>K;

		int stage = 2;
		if (N>1) stage = 4*pow(2,N-2);
 
		//cout<<stage<<endl;
		bool status = ((K+1)%stage)==0;
		if (status)	cout<<"Case #"<<c<<": ON"<<endl;
		else	cout<<"Case #"<<c<<": OFF"<<endl;

	}
	return 0;
}
