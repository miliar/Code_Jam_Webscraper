#include <iostream>

using namespace std;

int main(){
	freopen("aa.in","r",stdin);
	freopen("aa.out","w",stdout);
	long long casos,ind=1;
	cin>>casos;
	while(casos--){
		long long n,k;
		cin>>n>>k;
		k++;
		n=1<<n;
		cout<<"Case #"<<ind++<<": ";
		if(k%n)
			cout<<"OFF"<<endl;
		else
			cout<<"ON"<<endl;
	}
	return 0;
}
