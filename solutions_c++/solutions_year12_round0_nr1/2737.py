#include<cstdio>
#include<cstring>
#include<map>
#include<iostream>
#include<algorithm>

using namespace std;

const int maxN = 10086;

char str[maxN];

map<char, char> g;

void init()
{
    g.clear();
    g['a'] = 'y';
    g['b'] = 'h';
    g['c'] = 'e';
    g['d'] = 's';
    g['e'] = 'o';
    g['f'] = 'c';
    g['g'] = 'v';
    g['h'] = 'x';
    g['i'] = 'd';
    g['j'] = 'u';
    g['k'] = 'i';
    g['l'] = 'g';
    g['m'] = 'l';
    g['n'] = 'b';
    g['o'] = 'k';
    g['p'] = 'r';
    g['q'] = 'z'; // 1
    g['r'] = 't';
    g['s'] = 'n';
    g['t'] = 'w';
    g['u'] = 'j';
    g['v'] = 'p';
    g['w'] = 'f';
    g['x'] = 'm';
    g['y'] = 'a';
    g['z'] = 'q'; // 2
    g[' '] = ' ';
}

int main()
{
    //freopen("data.in", "r", stdin);
    //freopen("data.out", "w", stdout);
    init();
    int nt, idx = 0; scanf("%d", &nt); gets(str);
    while( (nt --) > 0 ) {
        gets(str); printf("Case #%d: ", ++idx);
        for(int i = 0; str[i]; ++i)
            putchar( g[ str[i] ] );
        puts("");
    }
    return 0;
}
