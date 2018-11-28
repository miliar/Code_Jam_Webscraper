#include <iostream>
using namespace std;

int main(){

	
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	long long k, n, t;
	cin>>t;
	for(int i=0; i<t; i++){
		cin>>n>>k;
		long long temp=(1i64<<n)-1;
		cout<<"Case #"<<i+1<<": ";
		if(temp==k || (k+1)%(temp+1)==0) cout<<"ON";
		else cout<<"OFF";
		cout<<endl;
	}		



	return 0;
}