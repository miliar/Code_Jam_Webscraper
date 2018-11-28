#include<cstdio>
#include<cstring>

using namespace std;

char a[300];

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    a['a']='y';
a['b']='h';
a['c']='e';
a['d']='s';
a['e']='o';
a['f']='c';
a['g']='v';
a['h']='x';
a['i']='d';
a['j']='u';
a['k']='i';
a['l']='g';
a['m']='l';
a['n']='b';
a['o']='k';
a['p']='r';
a['q']='z';
a['r']='t';
a['s']='n';
a['t']='w';
a['u']='j';
a['v']='p';
a['w']='f';
a['x']='m';
a['y']='a';
a['z']='q';
a[' ']=' ';

    char s[110];
    int n;
    scanf("%d\n",&n);
    for (int i=1;i<=n;i++)
    {
        gets(s);
        for (int j=0;j<strlen(s);j++)
            s[j]=a[s[j]];
        printf("Case #%d: %s\n",i,s);
    }
}
