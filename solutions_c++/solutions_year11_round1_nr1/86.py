#include <cstdio>
#include <iostream>
using namespace std;

typedef long long LL;

LL gcd(int a, int b){
	return (b==0)?a:gcd(b, a%b);
}

int main(){
	int t,u,ok,g,pd,pg;
	LL n;
	cin>>t;
	for (u=0; u<t; u++){
		ok=1;
		cin>>n>>pd>>pg;
		g=gcd(pd,100);
		if (n<100/g) ok=0;
		else if (pd!=0&&pg==0) ok=0;
		else if (pd!=100&&pg==100) ok=0;
		cout<<"Case #"<<(u+1)<<": "<<(ok?"Possible":"Broken")<<endl;
	}
	return 0;
}
