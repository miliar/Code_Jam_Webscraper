#include<iostream>
#include<map>
using namespace std;

map<char,char> c;

int main(){
	int n;cin>>n;
	string s;getline(cin,s);
	c['a']='y';c['b']='h';c['c']='e';c['d']='s';c['e']='o';c['f']='c';c['g']='v';c['h']='x';c['i']='d';c['j']='u';c['k']='i';c['l']='g';c['m']='l';c['n']='b';c['o']='k';c['p']='r';c['q']='z';c['r']='t';c['s']='n';c['t']='w';c['u']='j';c['v']='p';c['w']='f';c['x']='m';c['y']='a';c['z']='q';c[' ']=' ';
	for(int i=1;i<=n;i++){
		getline(cin,s);
		for(int j=0;j<s.size();j++)s[j]=c[s[j]];
		cout<<"Case #"<<i<<": ";
		cout<<s<<endl;
	}
}
