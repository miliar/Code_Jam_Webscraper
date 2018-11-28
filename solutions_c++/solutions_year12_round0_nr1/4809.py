#include <stdio.h>
#include <string.h>
#include <map>

using namespace std;

int main() {
    map <char,char> A;
    A['a'] = 'y';
    A['b'] = 'h';
    A['c'] = 'e';
    A['d'] = 's';
    A['e'] = 'o';
    A['f'] = 'c';
    A['g'] = 'v';
    A['h'] = 'x';
    A['i'] = 'd';
    A['j'] = 'u';
    A['k'] = 'i';
    A['l'] = 'g';
    A['m'] = 'l';
    A['n'] = 'b';
    A['o'] = 'k';
    A['p'] = 'r';
    A['q'] = 'z';
    A['r'] = 't';
    A['s'] = 'n';
    A['t'] = 'w';
    A['u'] = 'j';
    A['v'] = 'p';
    A['w'] = 'f';
    A['x'] = 'm';
    A['y'] = 'a';
    A['z'] = 'q';

    int tests;
    scanf("%d\n", &tests);
    char str[128];
    for (int t = 1; t <= tests; t++) {
        fgets(str, 128, stdin);
        int l = strlen(str);
        printf("Case #%d: ", t);
        for (int i = 0; i < l; i++) {
            if (A.count(str[i])) {
                printf("%c", A[str[i]]);
            } else {
                printf("%c", str[i]);
            }
        }
    }

    return 0;
}
