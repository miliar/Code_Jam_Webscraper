#include<iostream>
using namespace std;

int main(){
	long long int t,down,top,bonus,counter,b,sum;
	cin>>t;
	for(counter=1;counter<=t;++counter){
		cin>>down>>top>>bonus;
		for(b=down,sum=0;down<top;down*=bonus,++sum);
		for(b=0;sum>(1<<b);++b);
		cout<<"Case #"<<counter<<": "<<b<<endl;
	}
	return 0;
}
