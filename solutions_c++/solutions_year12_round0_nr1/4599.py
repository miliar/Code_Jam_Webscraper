#include<cstdio>
#include<iostream>
#include<string>
#include<algorithm>
#include<map>
using namespace std;

const string key="abcdefghijklmnopqrstuvwxyz ";
const string value="yhesocvxduiglbkrztnwjpfmaq ";
int n;
string s;
map<char,char>dict;

struct Translate{char operator()(char c){return dict[c];}};

int main(void){
	for(int i=0;i<key.size();++i)dict[key[i]]=value[i];
	scanf("%d\n",&n);
	for(int i=0;i<n;++i){
		getline(cin,s);
		transform(s.begin(),s.end(),s.begin(),Translate());
		cout<< "Case #"<< i+1<< ": "<< s<< "\n";
	}
	return 0;
}
