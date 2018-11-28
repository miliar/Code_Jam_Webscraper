#include<iostream>
#include<string.h>
#include<string>
#include<string.h>
#include<map>
#include<stdio.h>
#include<queue>

using namespace std;
map<char ,char >str;
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    str['a']='y';
    str['b']='h';
    str['c']='e';
    str['d']='s';
    str['e']='o';
    str['f']='c';
    str['g']='v';
    str['h']='x';
    str['i']='d';
    str['j']='u';
    str['k']='i';
    str['l']='g';
    str['m']='l';
    str['n']='b';
    str['o']='k';
    str['p']='r';
    str['q']='z';
    str['r']='t';
    str['s']='n';
    str['t']='w';
    str['u']='j';
    str['v']='p';
    str['w']='f';
    str['x']='m';
    str['y']='a';
    str['z']='q';
    int T;
    char a[200];
    int n;
    cin>>T;
    getchar();
    for(int l=1;l<=T;++l)
    {
        gets(a);
        n=strlen(a);
        printf("Case #%d: ",l);
        for(int i=0;i<n;++i)
        {
            if(a[i]<='z'&&a[i]>='a')
            printf("%c",str[a[i]]);
            else
            printf("%c",a[i]);
        }
        printf("\n");
    }
    return 0;
}
