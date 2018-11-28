#include <iostream>

using namespace std;

int main(){
	int c, cases, n, k;
	
	cin>>cases;
	for (c=1; c<=cases; c++){
		cin>>n>>k;
		
		cout<<"Case #"<<c<<": ";
		if (((k+1) % (1<<n)) == 0) cout<<"ON"<<endl;
		else cout<<"OFF"<<endl;
	}
	
	return 0;
}
