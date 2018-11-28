#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<sstream>
#include<set>
using namespace std;
int main(){
	string a="our language is impossible to understand";
	string aa="ejp mysljylc kd kxveddknmc re jsicpdrysi";
	string b="there are twenty six factorial possibilities";
	string bb="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	string c="so it is okay if you want to just give up";
	string cc="de kr kd eoya kw aej tysr re ujdr lkgc jv";
	map<char,char> m;
	for(int i=0;i!=a.size();++i){
		m[a[i]]=aa[i];
	}
	for(int i=0;i!=b.size();++i){
		m[b[i]]=bb[i];
	}
	for(int i=0;i!=c.size();++i){
		m[c[i]]=cc[i];
	}
	m['z']='q';
	m['q']='z';
	map<char,char>::iterator p=m.begin();
	map<char,char> r;
	while(p!=m.end()){
		r[p->second]=p->first;
		p++;
	}
	int T;
	cin>>T;
	string line;
	getline(cin,line);
	for(int i=0;i<T;++i){
		getline(cin,line);
		cout<<"Case #"<<i+1<<": ";
		for(int i=0;i!=line.size();++i){
			cout<<r[line[i]];
		}
		cout<<endl;
	}
}
