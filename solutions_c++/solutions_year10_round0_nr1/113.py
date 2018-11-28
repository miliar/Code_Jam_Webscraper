#include<iostream>
using namespace std;

int t,T,N,M;

int main() {
	cin>>T;
	for(t=1;t<=T;t++) {
		cin>>N>>M;
		M%=1<<N;
		cout<<"Case #"<<t<<": ";
		if(M+1==(1<<N)) cout<<"ON"<<endl;
		else cout<<"OFF"<<endl;		
	}
}
