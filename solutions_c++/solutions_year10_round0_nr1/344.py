#include<iostream>
#define fr(i,a,b) for(i=a;i<=b;++i)
using namespace std;
long long t,ca,n,k,tmp;
int main(){
	freopen("a.out","w",stdout);
	cin>>ca;
	fr(t,1,ca){
		cin>>n>>k;
		tmp=(1<<n)-1;
		cout<<"Case #"<<t<<": ";
		if((k&tmp)==tmp)
			cout<<"ON"<<endl;
		else
			cout<<"OFF"<<endl;
	}
}