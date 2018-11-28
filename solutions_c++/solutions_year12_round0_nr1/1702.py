#include <cstdio>
using namespace std;

char dict[256];

void init() {
    dict['a'] = 'y';
    dict['b'] = 'h';
    dict['c'] = 'e';
    dict['d'] = 's';
    dict['e'] = 'o';
    dict['f'] = 'c';
    dict['g'] = 'v';
    dict['h'] = 'x';
    dict['i'] = 'd';
    dict['j'] = 'u';
    dict['k'] = 'i';
    dict['l'] = 'g';
    dict['m'] = 'l';
    dict['n'] = 'b';
    dict['o'] = 'k';
    dict['p'] = 'r';
    dict['q'] = 'z';
    dict['r'] = 't';
    dict['s'] = 'n';
    dict['t'] = 'w';
    dict['u'] = 'j';
    dict['v'] = 'p';
    dict['w'] = 'f';
    dict['x'] = 'm';
    dict['y'] = 'a';
    dict['z'] = 'q';
    dict[' '] = ' ';
}

int main() {
    int T;
    char str[110];
    init();
    scanf("%d", &T);
    getchar();
    for (int t = 1; t <= T; t++) {
        scanf("%[^\n]", str);
        getchar();
        for (int i = 0; str[i] != '\0'; i++) {
            str[i] = dict[str[i]];
        }
        printf("Case #%d: %s\n", t, str);
    }
}
