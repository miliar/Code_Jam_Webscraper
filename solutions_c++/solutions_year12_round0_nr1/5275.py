#include <stdlib.h>
#include <stdio.h>
#include <string.h>


int maps[256];


char line[1000];

int main()
{
	maps['a']='y';
	maps['b']='h';
	maps['c']='e';
	maps['d']='s';
	maps['e']='o';
	maps['f']='c';
	maps['g']='v';
	maps['h']='x';
	maps['i']='d';
	maps['j']='u';
	maps['k']='i';
	maps['l']='g';
	maps['m']='l';
	maps['n']='b';
	maps['o']='k';
	maps['p']='r';
	maps['q']='z';
	maps['r']='t';
	maps['s']='n';
	maps['t']='w';
	maps['u']='j';
	maps['v']='p';
	maps['w']='f';
	maps['x']='m';
	maps['y']='a';
	maps['z']='q';
	maps[' ']=' ';
	int t;
	scanf("%d\n",&t);
	for(int i=1;i<=t;++i)
	{
		fgets(line,1000,stdin);
		int len = strlen(line);
		for(int j=0;j<len;++j)
			line[j]=maps[line[j]];
		printf("Case #%d: %s\n",i,line);
	}
	return 0;
}
