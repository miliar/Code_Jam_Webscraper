#include <cstdio>
#include <string>
#include <iostream>
#include <set>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <map>
#include <algorithm>
using namespace std;

#define FILEIO
string _input="A-small-attempt0.in";

char s1[1000],s2[1000];

int main()
{
#ifdef FILEIO
    freopen(_input.c_str(),"r",stdin);
    freopen((_input+".txt").c_str(), "w", stdout);
#endif
    char a[256];
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

    int T; scanf("%d",&T); getchar();
    for(int IT=0;IT<T;IT++)
    {
        gets(s1);
        printf("Case #%d: ", IT+1);
        for(int i=0;i<strlen(s1);i++)
        {
            putchar(a[s1[i]]);
        }
        putchar('\n');
        //printf("Case #%d: ", IT+1);
    }
    //for(char ch='a';ch<='z';ch++)printf("a['%c']='%c';\n",ch,trans[ch]);
    return 0;
}
