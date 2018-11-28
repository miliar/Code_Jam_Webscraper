#include<iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;
long long gcd(long long a,long long b){
	if(b==0)
		return a;
	else
		return gcd(b,a%b);
}
int main(){
	//freopen("A-large.in","r",stdin);
	//freopen("out.txt","w",stdout);
	long long pd,pg;
	long long pdl;
	long long nd,ndl;
	long long g;
	long long n;
	long long T;
	long long cas=1;
	cin>>T;
	long long flag;
	while(T--){
		flag=0;
		cin>>n>>pd>>pg;
		pdl=100-pd;
		if(pdl<pd){
			g=gcd(pd,pdl);				
		}
		else
			g=gcd(pdl,pd);
		nd=100/g;
		if(pd==0)
			pdl=1;
		if(pdl==0)
			pd=1;
		if(nd>n)
			flag=1;
		if(pdl!=0&&pg==100)
			flag=1;
		if(pd!=0&&pg==0)
			flag=1;
		cout<<"Case #"<<cas++<<": ";
		if(flag)
			cout<<"Broken"<<endl;
		else
			cout<<"Possible"<<endl;
	}
	return 0;
}