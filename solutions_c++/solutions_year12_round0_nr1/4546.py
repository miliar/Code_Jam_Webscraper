#include<stdio.h>
#include<iostream>

using namespace std;

int main()
{
	char map[200];
	map['a']='y';
	map['b']='h';
	map['c']='e';
	map['d']='s';
	map['e']='o';
	map['f']='c';
	map['g']='v';
	map['h']='x';
	map['i']='d';
	map['j']='u';
	map['k']='i';
	map['l']='g';
	map['m']='l';
	map['n']='b';
	map['o']='k';
	map['p']='r';
	map['q']='z';
	map['r']='t';
	map['s']='n';
	map['t']='w';
	map['u']='j';
	map['v']='p';
	map['w']='f';
	map['x']='m';
	map['y']='a';
	map['z']='q';
	map['\n']='\n';
	map[' ']=' ';
	int n,t=0;
	char c;
	scanf("%d%c",&n,&c);
	while(t!=n)
	{
		t++;
		printf("Case #%d: ",t);
		while(1)
		{
			scanf("%c",&c);
			printf("%c",map[c]);
			if(c=='\n')
				break;
		}
	}
	return 0;
}
