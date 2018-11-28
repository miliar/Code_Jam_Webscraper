#include<iostream>
#include<string>

using namespace std;

int power[31];

void init(){
	power[0]=1;
	for(int i=1; i<31; i++)
		power[i]=power[i-1]*2;
}

int main(){
	int C,N,K;
	string str;
	cin>>C;

	init();
	for(int i=1; i<=C; i++){
		cin>>N>>K;
		
		str = ((K+1)%power[N]) ? "OFF" : "ON";
		cout<<"Case #"<<i<<": "<<str<<endl;
	}
	return 0;
}