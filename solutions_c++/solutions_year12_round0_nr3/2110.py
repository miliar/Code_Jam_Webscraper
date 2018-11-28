#include <iostream>
#include <cstring>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <algorithm>
#include <set>
#include <stack>
#include <map>
#pragma comment(linker, "/STACK:165777216")
using namespace std;
string inttostring(int a){
	if(a==0) return "0";
	string str;
	while(a!=0){
		str=(char)('0'+a%10)+str;
		a/=10;
	}
	return str;
}
int strtoint(string str){
	int a=0;
	for(int i=0; i<str.length(); i++){
		a*=10;
		a+=str[i]-'0';
	}
	return a;
}
int ch[2000013];
int tt[]={1,10,100,1000,10000,100000,1000000,10000000};
int func(int a, int b){
	int n;
	
	int ans=0;
	int t=0;
	memset(ch,0,sizeof(ch));
	for(int i=a; i<=b; i++){
		set <int> st;
		n=1;
		if(i>9) n=1+1;
		if(i>99) n=2+1;
		if(i>999) n=3+1;
		if(i>9999) n=4+1;
		if(i>99999) n=5+1;
		if(i>999999) n=6+1;
		int k=tt[n-1];
		int nn=n;
		n=i;
		for(int j=1; j<nn; j++){
			t=n/10+(n%10)*k;
			if(t>=a && t<=b && i<t && (n%10!=0) && (ch[t]<i)){
				ans++;
				ch[t]=i;
			}
			n=t;
		}
	}
	return ans;
}
int main(){
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	int t;
	cin>>t;
	for(int i=0; i<t; i++){
		int a,b;
		cin>>a>>b;
		cout<<"Case #"<<i+1<<": "<<func(a,b)<<endl;
	}
	return 0;
}