#include<cstdio>
#include<algorithm>
#include<map>
#include<string>
#include<iostream>
#include<string.h>
using namespace std;

int main(){
	map<char,char> google;
	google['a']='y';
	google['b']='h';
	google['c']='e';
	google['d']='s';
	google['e']='o';
	google['f']='c';
	google['g']='v';
	google['h']='x';
	google['i']='d';
	google['j']='u';
	google['k']='i';
	google['l']='g';
	google['m']='l';
	google['n']='b';
	google['o']='k';
	google['p']='r';
	google['q']='z';
	google['r']='t';
	google['s']='n';
	google['t']='w';
	google['u']='j';
	google['v']='p';
	google['w']='f';
	google['x']='m';
	google['y']='a';
	google['z']='q';
	string str;
	int t,i,j,len;
	scanf("%d",&t);
	j=0;
	while(j++<=t){
		getline(cin,str);
		i=0;
		len=str.length();
		if(j!=1)
		printf("Case #%d: ",j-1);
		while(i<len){
			if(str[i]==' ') printf(" ");
			else printf("%c",google[str[i]]);
			i++;
		}
		if(j!=1)
			printf("\n");
	}
	return 0;
}


