#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;

char p[500];
int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	p['y']='a';p['c']='e';p['k']='i';p['x']='m';p['z']='q';p['j']='u';
	p['n']='b';p['w']='f';p['u']='j';p['s']='n';p['p']='r';p['g']='v';
	p['f']='c';p['l']='g';p['o']='k';p['e']='o';p['d']='s';p['t']='w';
	p['i']='d';p['b']='h';p['m']='l';p['v']='p';p['r']='t';p['h']='x';
	p['a']='y';p['q']='z';
	int N;string s;
	cin>>N;
	getline(cin,s);
	for(int k=0;k<N;k++){
		cout<<"Case #"<<k+1<<": ";
		getline(cin,s);
		for(int i=0;i<s.length();i++){
			if (s[i]!=' ') cout<<p[s[i]];
			else cout<<s[i];
		}
		cout<<endl;
	}
	return 0;
}


