#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
	int t,n,i,u,j,ot=0,bt=0,op=1,bp=1,p;
	char s[2];
	cin>>t;
	for (u=0; u<t; u++){
		ot=bt=0;
		op=bp=1;
		cin>>n;
		for (i=0; i<n; i++){
			cin>>s>>p;
			if (s[0]=='O'){ ot=max(ot+abs(op-p)+1,bt+1); op=p;}			
			else          { bt=max(bt+abs(bp-p)+1,ot+1); bp=p;}
		}
		cout<<"Case #"<<(u+1)<<": "<<max(ot,bt)<<endl;
	}
	return 0;
}
