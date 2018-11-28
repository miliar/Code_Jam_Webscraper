#include<cstdio>
#include<map>
#include<algorithm>
using namespace std;

map<char,char> m;

int main(){
	m['a']='y';
	m['b']='h';
	m['c']='e';
	m['d']='s';
	m['e']='o';
	m['f']='c';
	m['g']='v';
	m['h']='x';
	m['i']='d';
	m['j']='u';
	m['k']='i';
	m['l']='g';
	m['m']='l';
	m['n']='b';
	m['o']='k';
	m['p']='r';
	m['q']='z';
	m['r']='t';
	m['s']='n';
	m['t']='w';
	m['u']='j';
	m['v']='p';
	m['w']='f';
	m['x']='m';
	m['y']='a';
	m['z']='q';
	int cas,i=0;
	scanf("%d\n",&cas);
	char c;
	while(cas--){
		printf("Case #%d: ",++i);
		while(c=getchar()){
			if(m.count(c)) c = m[c];
			putchar(c);
			if(c=='\n')break;
		}
	}
}
