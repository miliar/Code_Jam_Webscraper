#include<cstdio>
#include<iostream>
#include<cstring>
#include<string>
#include<algorithm>
using namespace std;
typedef long long LL;
int main()
{
    char in[10000],out[10000];
    char tr[1000];
    int i,t;
    tr['y']='a';
    tr['n']='b';
    tr['f']='c';
    tr['i']='d';
    tr['c']='e';
    tr['w']='f';
    tr['l']='g';
    tr['b']='h';
    tr['k']='i';
    tr['u']='j';
    tr['o']='k';
    tr['m']='l';
    tr['x']='m';
    tr['s']='n';
    tr['e']='o';
    tr['v']='p';
    tr['z']='q';
    tr['p']='r';
    tr['d']='s';
    tr['r']='t';
    tr['j']='u';
    tr['g']='v';
    tr['t']='w';
    tr['h']='x';
    tr['a']='y';
    tr['q']='z';
    freopen("gca.in","r",stdin);
    freopen("gca.out","w",stdout);
    scanf("%d",&t);getchar();
    for(int cn=1;cn<=t;cn++)
    {
        gets(in);
        for(i=0;i<strlen(in);i++)
        {
            if(in[i]>='a'&&in[i]<='z')
            {
                out[i]=tr[in[i]];
            }
            else
                out[i]=in[i];
        }
        out[i]=0;
        printf("Case #%d: ",cn);
        puts(out);
    }
    return 0;
}
