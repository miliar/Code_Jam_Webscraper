#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

char ht[256];

void init() {
     ht['a'] = 'y';
     ht['b'] = 'h';
     ht['c'] = 'e';
     ht['d'] = 's';
     ht['e'] = 'o';
     ht['f'] = 'c';
     ht['g'] = 'v';
     ht['h'] = 'x';
     ht['i'] = 'd';
     ht['j'] = 'u';
     ht['k'] = 'i';
     ht['l'] = 'g';
     ht['m'] = 'l';
     ht['n'] = 'b';
     ht['o'] = 'k';
     ht['p'] = 'r';
     ht['q'] = 'z';
     ht['r'] = 't';
     ht['s'] = 'n';
     ht['t'] = 'w';
     ht['u'] = 'j';
     ht['v'] = 'p';
     ht['w'] = 'f';
     ht['x'] = 'm';
     ht['y'] = 'a';
     ht['z'] = 'q';
     ht[' '] = ' ';
}

int main() {
    init();
    int t, l;
    char s[256];
    scanf("%d\n", &t);
    for (int i = 1; i <= t; ++i) {
        gets(s);
        l = strlen(s);
        for (int j = 0; j < l; ++j) {
            s[j] = ht[s[j]];
        }
        printf("Case #%d: %s\n", i, s);
    }
    return 0;
}
