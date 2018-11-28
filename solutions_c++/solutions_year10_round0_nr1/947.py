#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
	int T,n,k,a,kase=0;
	bool flag;
	cin>>T;
	while (T--) {
		cin>>n>>k;
		a=1;
		for (int i=0;i<n;i++)
			a*=2;
		while (k>a)
			k-=a;
		if (k==a-1)
			flag=true;
		else
			flag=false;
		cout<<"Case #"<<++kase<<": ";
		if (flag)
			cout<<"ON"<<endl;
		else
			cout<<"OFF"<<endl;
	}
	return 0;
}
