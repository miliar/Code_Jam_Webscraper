#include<iostream>
#include<string>
using namespace std;
char t[128];
int main(){
	string a[4]={"y qee","ejp mysljylc kd kxveddknmc re jsicpdrysi",
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
	"de kr kd eoya kw aej tysr re ujdr lkgc jv"};
	string b[4]={"a zoo","our language is impossible to understand",
	"there are twenty six factorial possibilities",
	"so it is okay if you want to just give up"};
	for(int i=0;i<4;++i){
		for(int j=0;j<a[i].length();++j)if(a[i][j]!=' ')t[a[i][j]]=b[i][j];
	}
	/*int ct=0;
	for(int i=0;i<128;++i)if(t[i])cout<<(char)i<<(char)t[i]<<endl,++ct;
	cout<<ct<<endl;*/
	t['z']='q';//discovered with the commented above code and sample input :)
	int T;
	cin>>T;
	string s;
	getline(cin,s);
	for(int i=1;i<=T;++i){
		getline(cin,s);
		for(int j=0;j<s.length();++j)if(s[j]!=' ')s[j]=t[s[j]];
		cout<<"Case #"<<i<<": "<<s<<"\n";
	}
}
