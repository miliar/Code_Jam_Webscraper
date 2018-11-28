#include<cstdio>
#include<cstring>
#include<cmath>
#include<map>
#include<cstdlib>
#include<cctype>
using namespace std;
map<char,char>t;
int main()
{
    t.clear();
    t['a']='y';
    t['b']='h';
    t['c']='e';
    t['d']='s';
    t['e']='o';
    t['f']='c';
    t['g']='v';
    t['h']='x';
    t['i']='d';
    t['j']='u';
    t['k']='i';
    t['l']='g';
    t['m']='l';
    t['n']='b';
    t['o']='k';
    t['p']='r';
    t['q']='z';
    t['r']='t';
    t['s']='n';
    t['t']='w';
    t['u']='j';
    t['v']='p';
    t['w']='f';
    t['x']='m';
    t['y']='a';
    t['z']='q';
    freopen("ans.txt","w",stdout);
    int n;
    scanf("%d",&n);
    char    tmp;
    scanf("%*c");
    for(int c=1;c<=n;c++)
    {
        printf("Case #%d: ",c);
        while(scanf("%c",&tmp)==1&&tmp!='\n')
        if(islower(tmp))
        {
            printf("%c",t[tmp]);
        }
        else printf("%c",tmp);
        printf("%c",tmp);
    }


    return 0;
}
