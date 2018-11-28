
#include<cstdio>
#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<cmath>
#include<cstring>
using namespace std;
int main(){
	int t,c;
	cin>>t;
	map<char,char> m;
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
	for(c=1;c<=t;c++){
		char s[200],ch;
		scanf("%c",&ch);
		scanf("%[^\n]",s);
		int l=strlen(s),i;
		for(i=0;i<l;i++){
			if(s[i]==' ')
				continue;
			s[i]=m[s[i]];
		}
		printf("Case #%d: %s\n",c,s);
	}
	return 0;
}
