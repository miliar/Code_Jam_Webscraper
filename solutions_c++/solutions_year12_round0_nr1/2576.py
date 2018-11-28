#include <cstdio>
#include <cstdlib>
#include <cstring>

int main(void) {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T, i;
    char str[3010], dec[256];

    scanf("%d\n", &T);
    
    dec['a'] = 'y';
    dec['b'] = 'h';
    dec['c'] = 'e';
    dec['d'] = 's';
    dec['e'] = 'o';
    dec['f'] = 'c';
    dec['g'] = 'v';
    dec['h'] = 'x';
    dec['i'] = 'd';
    dec['j'] = 'u';
    dec['k'] = 'i';
    dec['l'] = 'g';
    dec['m'] = 'l';
    dec['n'] = 'b';
    dec['o'] = 'k';
    dec['p'] = 'r';
    dec['q'] = 'z';
    dec['r'] = 't';
    dec['s'] = 'n';
    dec['t'] = 'w';
    dec['t'] = 'w';
    dec['u'] = 'j';
    dec['v'] = 'p';
    dec['w'] = 'f';
    dec['x'] = 'm';
    dec['y'] = 'a';
    dec['z'] = 'q';

    for (i=1; i<=T; i++) {
        scanf("%[^\n]s", str);
        int x = strlen(str);

        printf("Case #%d: ", i);
        for (int j=0; j!=x; ++j) {
            if ( str[j] >= 'a' && str[j] <= 'z' ) printf("%c", dec[str[j]]);
            else printf("%c", str[j]);
        }

        printf("\n");
        scanf("\n");
    }

    return 0;
}
