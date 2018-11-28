#include<iostream>
using namespace std;
int doit(){
	int n,k;
	cin>>n>>k;
	k%=(1<<n);
	for( int i = 0; i < n; ++i ){
		if( ( ( k>>i ) & 1 ) == 0 )return 0;
	}
	return 1;
}
int main(){
	int T;
	cin>>T;
	int test = 1;
	while( T--){
		cout<<"Case #"<<test<<": "<<( doit() ? "ON" : "OFF" )<<endl;
		test++;
	}
}
