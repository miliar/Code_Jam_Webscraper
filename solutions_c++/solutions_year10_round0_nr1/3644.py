#include <iostream>
#include <cmath>

using namespace std;

bool isOn(long  N,long  K){
	long double X=pow(2.0,N);
	long Y=X;

	if((K+1)%Y)
		return true;
	else
		return false;


}

int main(){

	int grp;
	cin>>grp;

	int i=0;
	while(i<grp){
		long  N,K;
		cin>>N>>K;

		
		cout<<"Case #"<<i+1<<": "<<(isOn(N,K)?"OFF":"ON")<<endl;

		i++;




	}


}