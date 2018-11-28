#include<stdio.h>
#include<string.h>
#include<string>
#include<algorithm>
using namespace std;

int map[200];

int main()
{

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

    char s[150];
    int test,len,kase=0;
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d ",&test);
    while(test--)
    {
        gets(s);
        len=strlen(s);
        printf("Case #%d: ",++kase);
        for(int i=0;i<len;i++)
        {
            if(s[i]>='a' && s[i]<='z')
                printf("%c",map[s[i]]);
            else
                printf("%c",s[i]);
        }
        printf("\n");
    }
    return 0;

}
