#include<stdio.h>
#include<map>
#include<string.h>
using namespace std;
map<char,char> change;
void init()
{
    change['a']='y';
    change['b']='h';
    change['c']='e';
    change['d']='s';
    change['e']='o';
    change['f']='c';
    change['g']='v';
    change['h']='x';
    change['i']='d';
    change['j']='u';
    change['k']='i';
    change['l']='g';
    change['m']='l';
    change['n']='b';
    change['o']='k';
    change['p']='r';
    change['q']='z';
    change['r']='t';
    change['s']='n';
    change['t']='w';
    change['u']='j';
    change['v']='p';
    change['w']='f';
    change['x']='m';
    change['y']='a';
    change['z']='q';
    change[' ']=' ';
}
char a[110];
int main()
{
    int T;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&T);
    init();
    getchar();
    int cnt=1;
    while(T--)
    {
        gets(a);
        printf("Case #%d: ",cnt++);
        for(int i=0;i<strlen(a);i++)
            printf("%c",change[a[i]]);
        printf("\n");
    }
}
