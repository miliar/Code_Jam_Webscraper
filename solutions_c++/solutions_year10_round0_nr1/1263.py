#include<iostream>
using namespace std;

int main(){
	int t,n,k,counter;
	cin>>t;
	for(counter=1;counter<=t;++counter){
		cin>>n>>k;
		cout<<"Case #"<<counter<<": "<<((k&((1<<n)-1))==((1<<n)-1)?"ON":"OFF")<<endl;
	}
	return 0;
}
