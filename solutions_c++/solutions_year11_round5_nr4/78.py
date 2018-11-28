#include<iostream>
#include<stdio.h>
#include<string>
#include<cmath>
#define fr(i,a,b) for(i=a;i<=b;++i)
using namespace std;
string s;
bool found;
int ti,ca;
void dfs(string s){
	if(found)
		return;
	int i;
	long long tmp=0;
	fr(i,0,(int)s.size()-1)
		if(s[i]=='?'){
			s[i]='0';
			dfs(s);
			s[i]='1';
			dfs(s);
			return;
		}
		else
			tmp=tmp*2+s[i]-'0';
	long long k=floor(sqrt(tmp)+0.5);
	if(k*k==tmp){
		cout<<"Case #"<<ti<<": "<<s<<endl;
		found=true;
	}
}
int main(){
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);
	cin>>ca;
	fr(ti,1,ca){
		cin>>s;
		found=false;
		dfs(s);
	}
}