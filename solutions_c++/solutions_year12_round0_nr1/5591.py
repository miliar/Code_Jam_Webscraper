#include<stdio.h>
#include<stdlib.h>
#include<cmath>
#include<set>
#include<cstring>
#include<queue>
#include<list>
#include<algorithm>
#include<iostream>
#define PINF 999999999
#define NINF -999999999
using namespace std;
int n,m,k;
char str[1005];
char mem[1005];
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&n);
    scanf("%*c");
    mem[' ']=' ';
    mem['a']='y';
    mem['b']='h';
    mem['c']='e';
    mem['d']='s';
    mem['e']='o';
    mem['f']='c';
    mem['g']='v';
    mem['h']='x';
    mem['i']='d';
    mem['j']='u';
    mem['k']='i';
    mem['l']='g';
    mem['m']='l';
    mem['n']='b';
    mem['o']='k';
    mem['p']='r';
    mem['q']='z';
    mem['r']='t';
    mem['s']='n';
    mem['t']='w';
    mem['u']='j';
    mem['v']='p';
    mem['w']='f';
    mem['x']='m';
    mem['y']='a';
    mem['z']='q';
    for(int i=1;i<=n;i++)
    {
        for(int j=0;;j++)
        {
            scanf("%c",&str[j]);
            if(str[j]=='\n')
            {
                str[j]='\0';
                k=j;
                break;
            }
        }
        printf("Case #%d: ",i);
        for(int j=0;j<k;j++)
            printf("%c",mem[str[j]]);
        printf("\n");
    }
    scanf(" ");
}
