#include <cstring>
#include <cstdio>
using namespace std;
char s[10008];
int n, character[1008];
int main()
{
    freopen("out.txt", "w", stdout);
    character['a'] = 'y';
    character['b'] = 'h';
    character['c'] = 'e';
    character['d'] = 's';
    character['e'] = 'o';
    character['f'] = 'c';
    character['g'] = 'v';
    character['h'] = 'x';
    character['i'] = 'd';
    character['j'] = 'u';
    character['k'] = 'i';
    character['l'] = 'g';
    character['m'] = 'l';
    character['n'] = 'b';
    character['o'] = 'k';
    character['p'] = 'r';
    character['q'] = 'z';
    character['r'] = 't';
    character['s'] = 'n';
    character['t'] = 'w';
    character['u'] = 'j';
    character['v'] = 'p';
    character['w'] = 'f';
    character['x'] = 'm';
    character['y'] = 'a';
    character['z'] = 'q';
    character[' '] = ' ';
    int t, cnt = 0;
    scanf("%d%*c", &t);
    while (t--)
    {
        gets(s);
        ++cnt;
        printf("Case #%d: ", cnt);
        int n = strlen(s);
        for (int i = 0 ; i < n ; ++i)
            printf("%c", character[s[i]]);
        puts("");
    }
    return 0;
}
