#include<iostream>
#include<string>
using namespace std;
char T[256];
int main()
{
	char ch;
	int i,N;
T['a']='y';
T['b']='h';
T['c']='e';
T['d']='s';
T['e']='o';
T['f']='c';
T['g']='v';
T['h']='x';
T['i']='d';
T['j']='u';
T['k']='i';
T['l']='g';
T['m']='l';
T['n']='b';
T['o']='k';
T['p']='r';
T['q']='z';	//!!!
T['r']='t';
T['s']='n';
T['t']='w';
T['u']='j';
T['v']='p';
T['w']='f';
T['x']='m';
T['y']='a';
T['z']='q';	//!!!

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	scanf("%d\n",&N);
	for(i=1;i<=N;i++)
	{
		printf("Case #%d: ",i); 
		while(scanf("%c",&ch)!=EOF)
		{
			if(ch>='a'&&ch<='z') printf("%c",T[ch]);
			else printf("%c",ch);
			if(ch=='\n') break;
		}


	}

	return 0;
}