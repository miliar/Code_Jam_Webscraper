#include<stdio.h>
#include<string.h>
#include<iostream>
char tab[256];
void init()
{
    tab[' ']=' ';
    tab['a']='y';tab['b']='h';tab['c']='e';tab['d']='s';
    tab['e']='o';tab['f']='c';tab['g']='v';tab['h']='x';
    tab['i']='d';tab['j']='u';tab['k']='i';tab['l']='g';
    tab['m']='l';tab['n']='b';tab['o']='k';tab['p']='r';
    tab['q']='z'; tab['r']='t';tab['s']='n';tab['t']='w';
    tab['u']='j';tab['v']='p';tab['w']='f';tab['x']='m';
    tab['y']='a';tab['z']='q';


}
int main()
{
    init();
    int zes;scanf("%d\n",&zes);
    for (int z=1;z<=zes;z++)
    {
	char buf[200];
	gets(buf);
	printf("Case #%d: ",z);
	int len=strlen(buf);
	for (int i=0;i<len;i++)
	    printf("%c",tab[buf[i]]);
	printf("\n");
    }
}
