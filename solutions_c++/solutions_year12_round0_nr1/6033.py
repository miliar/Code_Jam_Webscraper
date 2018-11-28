#include<stdio.h>

char mapp[500],inp[200];


int main()
{
	int t,i,k;

	mapp['a']='y',mapp['b']='h',mapp['c']='e',mapp['d']='s',mapp['e']='o',mapp['f']='c';
	mapp['g']='v',mapp['h']='x',mapp['i']='d',mapp['j']='u',mapp['k']='i',mapp['l']='g';
	mapp['m']='l',mapp['n']='b',mapp['o']='k',mapp['p']='r',mapp['q']='z',mapp['r']='t';
	mapp['s']='n',mapp['t']='w',mapp['u']='j',mapp['v']='p',mapp['w']='f',mapp['x']='m';
	mapp['y']='a',mapp['z']='q',mapp[' ']=' ';


	//freopen("A-small-attempt0 (1).in","r",stdin);
	freopen("out.txt","w",stdout);

	scanf("%d\n",&t);
	for(k=1;k<=t;k++)
	{
		gets(inp);
		for(i=0;inp[i];i++)
			inp[i] = mapp[inp[i]];
		printf("Case #%d: %s\n",k,inp);
	}
	return 0;
}



 