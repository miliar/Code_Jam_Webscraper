#include<iostream>
#include<cstdio>
using namespace std;
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int tt;
	cin>>tt;
	for(int t=1;t<=tt;++t){
		int n,k;
		cin>>n>>k;
		k%=(1<<n);
		int yes=(k==(1<<n)-1);

		cout<<"Case #"<<t<<": ";
		if(yes)
			cout<<"ON";
		else
			cout<<"OFF";
		cout<<endl;
	}
	return 0;
}