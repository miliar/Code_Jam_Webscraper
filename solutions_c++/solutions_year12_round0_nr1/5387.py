//#include<iostream>
#include<fstream>
#include<map>
#include<string>
using namespace std;

ifstream fin("out");
ifstream cin("cin");
ofstream cout("cout");

int main(){
	
	map<char,char> m;
	m.clear();
	m[' ']=' ';
	do{
		char a,b;
		fin>>a>>b;
		m[a]=b;
	} while(fin);

	int T;
	cin>>T;
	cin.ignore();
	for(int i=0;i<T;i++){
		string s1,s2;
		getline(cin,s1);
		int l=s1.length();
		s2.assign(l,'b');
		for(int j=0;j<l;j++)
			s2[j]=m[s1[j]];
		cout<<"Case #"<<i+1<<": "<<s2<<endl;
	}
	return 0;
}