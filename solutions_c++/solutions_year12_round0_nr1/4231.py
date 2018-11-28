#include <iostream>
#include <cstdio>
#include <string>
using namespace std;


int T; 
char c[300];


int main() {
    c['a'] = 'y';  c['b'] = 'h';  c['c'] = 'e';
    c['d'] = 's';  c['e'] = 'o';  c['f'] = 'c';
    c['g'] = 'v';  c['h'] = 'x';  c['i'] = 'd';
    c['j'] = 'u';  c['k'] = 'i';  c['l'] = 'g';
    c['m'] = 'l';  c['n'] = 'b';  c['o'] = 'k';
    c['p'] = 'r';  c['q'] = 'z';  c['r'] = 't';
    c['s'] = 'n';  c['t'] = 'w';  c['u'] = 'j';
    c['v'] = 'p';  c['w'] = 'f';  c['x'] = 'm';
    c['y'] = 'a';  c['z'] = 'q';
    c[' '] = ' ';
    
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    scanf("%d\n", &T);
    for (int xxx = 1; xxx <= T; xxx++) {
        char s[10000];
        cin.getline (s, 100000);
        printf("Case #%d: ", xxx);
        for (int i = 0; i < strlen(s); i++)
            printf("%c", c[s[i]]);
        printf("\n");        
    } 
    
    
    return 0;    
}
