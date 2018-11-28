#include<iostream>
#include<map>
using namespace std;
map <char,char> ar;
int main()
{
ar['a']='y';ar['b']='h';ar['c']='e';ar['d']='s';ar['e']='o';ar['f']='c';
ar['g']='v';ar['h']='x';ar['i']='d';ar['j']='u';ar['k']='i';ar['l']='g';ar['m']='l';ar['n']='b';ar['o']='k';ar['p']='r';
ar['q']='z';ar['r']='t';ar['s']='n';ar['t']='w';ar['u']='j';ar['v']='p';ar['w']='f';ar['x']='m';ar['y']='a';ar['z']='q';
int t,i,j;

char a[101];

scanf("%d",&t);
getchar();
for(j=1;j<=t;j++)
{
	gets(a);
	for(i=0;a[i]!='\0';i++)
	{
		if(a[i]!=' ')
        a[i]=ar[a[i]];
	}
	printf("Case #%d: %s\n",j,a);
}
getchar();
}
