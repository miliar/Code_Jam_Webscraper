#include<cstdio>
#include<iostream>
using namespace std;
int test,Test,n,k;
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	cin>>Test;
	for (int test=1;test<=Test;test++){
		cin>>n>>k;
		cout<<"Case #"<<test<<": ";
		if ((k&((1<<n)-1))==((1<<n)-1))
			cout<<"ON"<<endl;
		else
			cout<<"OFF"<<endl;
	}
	return 0;
}
