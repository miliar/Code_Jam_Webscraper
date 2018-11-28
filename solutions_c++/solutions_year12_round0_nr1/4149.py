#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

int i, j, k, T, ca, N;
char s[105], res[105], t[205];

int main()
 {
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    t['e'] = 'o';
    t['j'] = 'u';
    t['p'] = 'r';
    t['m'] = 'l';
    t['y'] = 'a';
    t['s'] = 'n';
    t['l'] = 'g';
    t['c'] = 'e';
    t['k'] = 'i';
    t['d'] = 's';
    t['x'] = 'm';
    t['v'] = 'p';
    t['n'] = 'b';
    t['r'] = 't';
    t['i'] = 'd';
    t['b'] = 'h';
    t['t'] = 'w';
    t['a'] = 'y';
    t['w'] = 'f';
    t['f'] = 'c';
    t['u'] = 'j';
    t['o'] = 'k';
    t['g'] = 'v';
    t['h'] = 'x';
    t['z'] = 'q';
    t['q'] = 'z';
    t[' '] = ' ';
    for (scanf("%d", &T), ca = 1, gets(s); ca <= T; ca ++)
     {
        gets(s), memset(res, 0, sizeof(res));
        for (i = 0; i < strlen(s); i ++)
            res[i] = t[s[i]];
        printf("Case #%d: %s\n", ca, res);
     }
    return 0;
 }
