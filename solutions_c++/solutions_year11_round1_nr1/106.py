#include<iostream>
using namespace std;

int gcd(int x,int y){
if(x)while((y%=x)&&(x%=y));return x|y;
}

int main(){
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		long long n,pd,pg;
		cin>>n>>pd>>pg;
		if(100/gcd(pd,100)>n || (pd>0&&pg==0) || (pd<100&&pg==100))
			cout<<"Case #"<<i<<": Broken"<<endl;
		else
			cout<<"Case #"<<i<<": Possible"<<endl;
	}
	return 0;
}

