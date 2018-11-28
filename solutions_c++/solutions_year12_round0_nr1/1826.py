#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main()
{
	int n;
	char c[1000],buff;
	char d[200];
	d['a']='y';
	d['b']='h';
	d['c']='e';
	d['d']='s';
	d['e']='o';
	
	d['f']='c';
	d['g']='v';
	d['h']='x';
	d['i']='d';
	d['j']='u';
	
	d['k']='i';
	d['l']='g';
	d['m']='l';
	d['n']='b';
	d['o']='k';
	
	d['p']='r';
	d['q']='z';
	d['r']='t';
	d['s']='n';
	d['t']='w';
	
	d['u']='j';
	d['v']='p';
	d['w']='f';
	d['x']='m';
	d['y']='a';
	
	d['z']='q';
	
	scanf("%d",&n);
	scanf("%c",&buff);
	int m=0;
	while(n--)
		{
			m++;
		scanf("%[^\n]s",c);
		scanf("%c",&buff);
		
		
		for(int i=0;i<strlen(c);i++)
		{
			if(c[i]>=97&&c[i]<=122)
				c[i]=d[c[i]];
		}
		printf("Case #%d: %s\n",m,c);
		
	}
}