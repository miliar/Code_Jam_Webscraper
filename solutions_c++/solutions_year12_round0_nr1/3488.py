/*
TASK: Speaking in Tongues
LANG: C++
*/
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<map>
#include<set>
#include<list>
#include<queue>
#include<iostream>
using namespace std;
#define X first
#define Y second
int N,M,T;
char str[127];
char num[127];
int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("xxx.out","w",stdout);
    int i,j,k;
    num[' ']=' ';
    num['a']='y';
    num['b']='h';
    num['c']='e';
    num['d']='s';
    num['e']='o';
    num['f']='c';
    num['g']='v';
    num['h']='x';
    num['i']='d';
    num['j']='u';
    num['k']='i';
    num['l']='g';
    num['m']='l';
    num['n']='b';
    num['o']='k';
    num['p']='r';
    num['q']='z';    //--
    num['r']='t';
    num['s']='n';
    num['t']='w';
    num['u']='j';
    num['v']='p';
    num['w']='f';
    num['x']='m';
    num['y']='a';
    num['z']='q';   //--
    gets(str);
    sscanf(str,"%d",&T);
    int ii=1;
    while(T--)
    {
        gets(str);
        printf("Case #%d: ",ii);
        k=strlen(str);
        for(i=0;i<k;i++)
            printf("%c",num[str[i]]);
        printf("\n");
        ii++;
    }
}
