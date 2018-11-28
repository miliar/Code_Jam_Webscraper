#include<iostream>
using namespace std;

int main() {
	char mapping[256];
	mapping['a']='y';
	mapping['b']='h';
	mapping['c']='e';
	mapping['d']='s';
	mapping['e']='o';
	mapping['f']='c';
	mapping['g']='v';
	mapping['h']='x';
	mapping['i']='d';
	mapping['j']='u';
	mapping['k']='i';
	mapping['l']='g';
	mapping['m']='l';
	mapping['n']='b';
	mapping['o']='k';
	mapping['p']='r';
	mapping['q']='z';
	mapping['r']='t';
	mapping['s']='n';
	mapping['t']='w';
	mapping['u']='j';
	mapping['v']='p';
	mapping['w']='f';
	mapping['x']='m';
	mapping['y']='a';
	mapping['z']='q';
	int T;
	cin>>T;
	string st;
	getline(cin,st);
	for(int tc=1;tc<=T;tc++) {
		string s;
		getline(cin,s);
		for(int i=0;i<s.length();i++) if(s[i]!=' ') s[i]=mapping[s[i]];
		cout<<"Case #"<<tc<<": "<<s<<endl;
	}
}
