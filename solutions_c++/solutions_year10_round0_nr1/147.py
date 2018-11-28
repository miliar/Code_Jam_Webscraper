#include<iostream>

using namespace std;

#define rep(i,n) for(int i=0; i<n; i++)

int main(){
	int t,n,k, teste=1; 
	cin>>t;
	rep(i,t){
		cin>>n>>k;
		cout<<"Case #"<<teste++<<": "<<((k%(1<<(n))==((1<<(n))-1))?"ON\n":"OFF\n");
	}
}

