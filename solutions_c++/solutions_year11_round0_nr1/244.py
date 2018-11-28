#include<iostream>
#include<vector>
#include<string>
#include<cmath>
#include<algorithm>
#include<sstream>
#include<stdio.h>
#define fr(i,a,b) for(i=a;i<=b;i++)
using namespace std;
int ti,ca,n,w;
char ch;
int main(){
	freopen("a2.in","r",stdin);
	freopen("a2.out","w",stdout);
	cin>>ca;
	fr(ti,1,ca){
		int bp=1,op=1,bt=0,ot=0,now=0;
		cin>>n;
		while(n--){
			cin>>ch>>w;
			if(ch=='O'){
				ot=now=max(now,abs(op-w)+ot)+1;
				op=w;
			}
			else{
				bt=now=max(now,abs(bp-w)+bt)+1;
				bp=w;
			}
		}
		cout<<"Case #"<<ti<<": "<<now<<endl;
	}
}