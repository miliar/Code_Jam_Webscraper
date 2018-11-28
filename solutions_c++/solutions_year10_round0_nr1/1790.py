#include<iostream>
using namespace std;
int main(){
	unsigned int t,n,k;
	cin>>t;
	for(unsigned int i=1;i<=t;++i){
		cin>>n>>k;
		cout<<"Case #"<<i<<": "<<((((k^(k+1))+1)%(1<<(n+1))==0)?"ON":"OFF")<<endl;	//is xxxxxx11111 format when n=5
	}
	return 0;
}
