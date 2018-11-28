#include <iostream>
#include <map>
#include <stdio.h>
using namespace std;
char st[200];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out","w",stdout);
    map<char,char>Map;
    Map['a']='y';
    Map['b']='h';
    Map['c']='e';
    Map['d']='s';
    Map['e']='o';
    Map['f']='c';
    Map['g']='v';
    Map['h']='x';
    Map['i']='d';
    Map['j']='u';
    Map['k']='i';
    Map['l']='g';
    Map['m']='l';
    Map['n']='b';
    Map['o']='k';
    Map['p']='r';
    Map['q']='z';
    Map['r']='t';
    Map['s']='n';
    Map['t']='w';
    Map['u']='j';
    Map['v']='p';
    Map['w']='f';
    Map['x']='m';
    Map['y']='a';
    Map['z']='q';
    int n;
    while(scanf("%d",&n)!=EOF)
    {
        getchar();
        for(int i=1;i<=n;i++)
        {
            printf("Case #%d: ",i);
            gets(st);
            for(int j=0;st[j]!='\0';j++)
            {
                if(st[j]>='a'&&st[j]<='z')cout<<Map[st[j]];
                else cout<<st[j];
            }
            cout<<endl;
        }
    }
    return 0;
}
