#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<string>
#include<vector>
#include<unordered_map>
#include<iostream>
using namespace std;
int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small.out","w",stdout);
	unordered_map<char,char> m;
	unordered_map<char,char> mr;
	string a="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
	string aa="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
	m['z']='q';
	m['q']='z';
	mr['q']='z';
	for(int i=0;i<a.size();i++){
		m[a[i]]=aa[i];
		mr[aa[i]]=a[i];
	}
	// for(int i='a';i<='z';i++){
		// cout<<(char)i<<"="<<m[i]<<" "<<(char)i<<"="<<mr[i]<<endl;
	// }
	int cases;
	cin>>cases;
	cin.ignore();
	for(int i=1;i<=cases;i++){
		string s;
		getline(cin,s);
		cout<<"Case #"<<i<<": ";
		for(int j=0;j<s.size();j++){
			cout<<m[s[j]];
		}
		cout<<endl;
	}
}