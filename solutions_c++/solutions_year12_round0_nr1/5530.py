#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <memory.h>
using namespace std;

int main2()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    map<char,char> dict;
    dict['a'] = 'y'; dict['n'] = 'b';
    dict['b'] = 'h'; dict['o'] = 'k';
    dict['c'] = 'e'; dict['p'] = 'r';
    dict['d'] = 's'; dict['q'] = 'z';
    dict['e'] = 'o'; dict['r'] = 't';
    dict['f'] = 'c'; dict['s'] = 'n';
    dict['g'] = 'v'; dict['t'] = 'w';
    dict['h'] = 'x'; dict['u'] = 'j';
    dict['i'] = 'd'; dict['v'] = 'p';
    dict['j'] = 'u'; dict['w'] = 'f';
    dict['k'] = 'i'; dict['x'] = 'm';
    dict['l'] = 'g'; dict['y'] = 'a';
    dict['m'] = 'l'; dict['z'] = 'q';
    dict[' '] = ' ';
    int T; scanf("%d\n",&T);
    for(int t=1; t<=T; ++t)
    {
        string a;
        getline(cin, a);
        for(int i=0; i<a.length(); i++)
        {
            a[i] = dict[a[i]];
        }

        printf("Case #%d: %s\n", t, a.c_str());
    }
    return 0;
}

int main()
{
    return main2();
}
