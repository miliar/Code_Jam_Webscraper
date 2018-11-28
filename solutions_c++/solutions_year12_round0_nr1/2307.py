#include <iostream>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
using namespace std;
int n;
string str;
map<char,char> m;
string h1="abcdefghijklmnopqrstuvwxyz";
string h2="yhesocvxduiglbkrztnwjpfmaq";
void solve(){
	for(int i=0;i<str.size();i++){
		if(str[i]==' ')cout<<' ';
		else if(str[i]>='a'&&str[i]<='z')cout<<m[str[i]];
	}
	cout<<endl;
}
void init(){
	for(int i=0;i<26;i++){
		m[h1[i]]=h2[i];
	}
}
int main(){
	cin>>n;
	init();
	getline(cin,str);
	for(int i = 0; i < n; i++){
		getline(cin,str);
		printf("Case #%d: ",i+1);
		solve();
	}


	return 0;
}