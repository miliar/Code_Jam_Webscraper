#include<iostream>
#include<iomanip>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cstdlib>
#include<cmath>
#include<map>
#include<set>
#include<queue>
#include<string>
#include<vector>
#include<ctime>
using namespace std;
map<char,char> mymap;
char s[105];
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.out","w",stdout);
    mymap['y']='a';
    mymap['n']='b';
    mymap['f']='c';
    mymap['i']='d';
    mymap['c']='e';
    mymap['w']='f';
    mymap['l']='g';
    mymap['b']='h';
    mymap['k']='i';
    mymap['u']='j';
    mymap['o']='k';
    mymap['m']='l';
    mymap['x']='m';
    mymap['s']='n';
    mymap['e']='o';
    mymap['v']='p';
    mymap['z']='q';
    mymap['p']='r';
    mymap['d']='s';
    mymap['r']='t';
    mymap['j']='u';
    mymap['g']='v';
    mymap['t']='w';
    mymap['h']='x';
    mymap['a']='y';
    mymap['q']='z';
    mymap[' ']=' ';
    int t,tt=0,len,i;
    scanf("%d",&t);
    getchar();
    while(t--)
    {
        tt++;
        gets(s);
        len=strlen(s);
        for(i=0;i<len;i++)
            s[i]=mymap[s[i]];
        printf("Case #%d: ",tt);
        puts(s);
    }
    return 0;
}
