#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
char dat[256], s[256];
int n, count;
int main()
{
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    dat['a'] = 'y';
    dat['b'] = 'h';
    dat['c'] = 'e';
    dat['d'] = 's';
    dat['e'] = 'o';
    dat['f'] = 'c';
    dat['g'] = 'v';
    dat['h'] = 'x';
    dat['i'] = 'd';
    dat['j'] = 'u';
    dat['k'] = 'i';
    dat['l'] = 'g';
    dat['m'] = 'l';
    dat['n'] = 'b';
    dat['o'] = 'k';
    dat['p'] = 'r';
    dat['q'] = 'z';
    dat['r'] = 't';
    dat['s'] = 'n';
    dat['t'] = 'w';
    dat['u'] = 'j';
    dat['v'] = 'p';
    dat['w'] = 'f';
    dat['x'] = 'm';
    dat['y'] = 'a';
    dat['z'] = 'q';
    scanf( "%d", &n );
    gets(s);
    count = 0;
    for (int i = 0; i < n; ++i)
    {
        count++;
        printf("Case #%d: ", count);
        gets(s);
        int len = strlen(s);
        for (int j = 0; j < len; ++j)
        {
            if ((s[j] >= 'a') && (s[j] <= 'z')
                printf("%c", dat[s[j]]);
            else
                printf("%c", s[j]);
        }
        printf("\n");
    }
    return 0;
}

