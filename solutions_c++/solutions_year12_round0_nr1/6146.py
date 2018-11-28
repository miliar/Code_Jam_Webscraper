#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
    int test;
    char map[27]={' '};
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
    scanf("%d",&test);
    int count=1;
    char g[1004]={' '};
	gets(g);//~ts 
    while(test--)
    {
    int i=0;
     //	fflush(stdin);
		
		gets(g);
     printf("Case #%d: ",count++);
         while(g[i]){
    if(g[i]==' ')
    printf(" ");
    else
    printf("%c",map[g[i]]);
    i++;
    }
 printf("\n");
}  
    }
