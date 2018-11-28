#include <stdio.h>

char s[300], t[300], mp[300];
bool used[300];

int main()
{
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small-attempt1.out", "w", stdout);
//    freopen("1.in", "r", stdin);
//    freopen("1.out", "w", stdout);
//    for (int i = 0; i < 3; ++i)
//    {
//        gets(s);
//        gets(t);
//        for (int j = 0; s[j]; ++j) mp[s[j]] = t[j];
//    }
//    mp['q'] = 'z';
//    mp['z'] = 'q';
//    for (int i = 'a'; i <= 'z'; ++i) printf("mp['%c'] = '%c';\n", i, mp[i]);
mp['a'] = 'y';
mp['b'] = 'h';
mp['c'] = 'e';
mp['d'] = 's';
mp['e'] = 'o';
mp['f'] = 'c';
mp['g'] = 'v';
mp['h'] = 'x';
mp['i'] = 'd';
mp['j'] = 'u';
mp['k'] = 'i';
mp['l'] = 'g';
mp['m'] = 'l';
mp['n'] = 'b';
mp['o'] = 'k';
mp['p'] = 'r';
mp['q'] = 'z';
mp['r'] = 't';
mp['s'] = 'n';
mp['t'] = 'w';
mp['u'] = 'j';
mp['v'] = 'p';
mp['w'] = 'f';
mp['x'] = 'm';
mp['y'] = 'a';
mp['z'] = 'q';
int T, cas = 0;
    scanf("%d", &T);
    gets(s);
    while (T--)
    {
        gets(s);
        printf("Case #%d: ", ++cas);
        for (int i = 0; s[i]; ++i) putchar(s[i] <= 'z' && s[i] >= 'a' ? mp[s[i]] : s[i]);
        puts("");
    }
    return 0;
}
