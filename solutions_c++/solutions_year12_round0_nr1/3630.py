#include <iostream>
#include <string>
#include <string.h>
#include <cstdio>

using namespace std;

const int MAXN = 2000;

char m[MAXN];
char G[MAXN];

int main(){
    m['a'] = 'y';
    m['b'] = 'h';
    m['c'] = 'e';
    m['d'] = 's';
    m['e'] = 'o';
    m['f'] = 'c';
    m['g'] = 'v';
    m['h'] = 'x';
    m['i'] = 'd';
    m['j'] = 'u';
    m['k'] = 'i';
    m['l'] = 'g';
    m['m'] = 'l';
    m['n'] = 'b';
    m['o'] = 'k';
    m['p'] = 'r';
    m['q'] = 'z';
    m['r'] = 't';
    m['s'] = 'n';
    m['t'] = 'w';
    m['u'] = 'j';
    m['v'] = 'p';
    m['w'] = 'f';
    m['x'] = 'm';
    m['y'] = 'a';
    m['z'] = 'q';
    int t;
    freopen("A.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &t);
    getchar();
    for (int i = 1; i <= t; i++){
        cin.getline(G, MAXN - 1);
        printf("Case #%d: ", i);
        for (int j = 0; j < strlen(G); j++){
            if (G[j] != ' '){
                printf("%c", m[G[j]]);
            }else{
                printf(" ");
            }
        }
        printf("\n");
    }
    return 0;
}
