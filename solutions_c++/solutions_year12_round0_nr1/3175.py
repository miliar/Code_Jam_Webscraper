#include <iostream>
#include <map>
#include <cstring>
#include <cstdio>
using namespace std;

map<char,char>m;
char ch[500];
int main(){
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	int a,b,c,d,e;
	m['a']='y'; m['q']='z';
	m['b']='h'; m['r']='t';
	m['c']='e'; m['s']='n';
	m['d']='s'; m['t']='w';
	m['e']='o'; m['u']='j';
	m['f']='c'; m['v']='p';
	m['g']='v'; m['w']='f';
	m['h']='x'; m['x']='m';
	m['i']='d'; m['y']='a';
	m['j']='u'; m['z']='q';
	m['k']='i'; m[' ']=' ';
	m['l']='g';
	m['m']='l';
	m['n']='b';
	m['o']='k';
	m['p']='r';
	cin>>e;
	gets(ch);
	string st;
	for(a=1;a<=e;a++){
		gets(ch);
		st="";
		for(b=0;b<strlen(ch);b++) st=st+m[ch[b]];
		cout<<"Case #"<<a<<": "<<st<<endl;
	}
	return 0;
}
	
