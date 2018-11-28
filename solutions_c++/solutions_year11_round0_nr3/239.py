#include<iostream>
#include<vector>
#include<string>
#include<cmath>
#include<algorithm>
#include<sstream>
#include<stdio.h>
#define fr(i,a,b) for(i=a;i<=b;i++)
using namespace std;
int ti,ca,sum,mi,x,i,n,v;
int main(){
	freopen("c2.in","r",stdin);
	freopen("c2.out","w",stdout);
	cin>>ca;
	fr(ti,1,ca){
		cin>>n;
		sum=0;
		mi=1<<30;
		x=0;
		fr(i,1,n){
			cin>>v;
			sum+=v;
			mi=min(v,mi);
			x^=v;
		}
		if(x)
			cout<<"Case #"<<ti<<": NO"<<endl;
		else
			cout<<"Case #"<<ti<<": "<<sum-mi<<endl;
	}
}