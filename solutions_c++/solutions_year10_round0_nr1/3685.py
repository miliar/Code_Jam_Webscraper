#include<iostream>

using namespace std;

int main(){
	int tn;cin>>tn;
	for(int ttn=1;ttn<=tn;ttn++){
		int n,m;cin>>n>>m;
		cout<<"Case #"<<ttn<<": ";
		if((m+1)%(1<<n)==0)cout<<"ON"<<endl;
		else cout<<"OFF"<<endl;
	}
	return 0;
}
