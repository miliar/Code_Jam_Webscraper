
#include<iostream>
#include<cstring>
#include<cstdlib>
#include<vector>
#include<algorithm>
#include<string>
#include<set>
#include<map>
#include<queue>
#include<cstdio>

using namespace std;
int main()
{
    int T;
    scanf("%d ",&T);
    int iT;
    map<char,char> m;
    m['a'] = 'y';
    m['b'] = 'h';
    m['c'] = 'e';
    m['d'] = 's';
    m['e'] = 'o';
    m['f'] = 'c';
    m['g'] = 'v';
    m['h'] = 'x';
    m['i'] = 'd';
    m['j'] = 'u';
    m['k'] = 'i';
    m['l'] = 'g';
    m['m'] = 'l';
    m['n'] = 'b';
    m['o'] = 'k';
    m['p'] = 'r';
    m['q'] = 'z';
    m['r'] = 't';
    m['s'] = 'n';
    m['t'] = 'w';
    m['u'] = 'j';
    m['v'] = 'p';
    m['w'] = 'f';
    m['x'] = 'm';
    m['y'] = 'a';
    m['z'] = 'q';
    m[' '] = ' ';
    char buf[1231];
    for(iT = 1; iT <= T; iT++) {
        printf("Case #%d: ", iT);
        gets(buf);
        for(int i = 0; buf[i]; i++) {
            printf("%c",m[buf[i]]);
        }
        puts("");

    }
   return 0;
}
