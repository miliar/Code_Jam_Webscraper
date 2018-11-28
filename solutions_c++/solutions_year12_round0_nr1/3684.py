#include<cstdio>
#include<iostream>
#include<map>
#include<string>
using namespace std;

map<char,char> mapa;

void f(string s1, string s2){
	for(int i=0; i<s1.length(); i++){
		mapa[s1[i]]=s2[i];
	}
}

int n;
string s;

string f2(string s1){
	string dupa;
	for(int i=0; i<s1.length(); i++){
		dupa+=mapa[s1[i]];
	}
	return dupa;
}

string getl(){
	string dupa;
	char c=getchar();
	while(c!='\n'){
		dupa+=c;
		c=getchar();
	}
	return dupa;
}

int main(){
	f("ejp mysljylc kd kxveddknmc re jsicpdrysi","our language is impossible to understand");
	f("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","there are twenty six factorial possibilities");
	f("de kr kd eoya kw aej tysr re ujdr lkgc jv","so it is okay if you want to just give up");
	f("z","q");
	f("q","z");
	cin >> n;
	getchar();
	for(int i=1; i<=n; i++){
		s=getl();
		cout << "Case #" << i << ": " << f2(s) << endl;
	}
}

