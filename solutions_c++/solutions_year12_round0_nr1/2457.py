#include <iostream>
#include <map>

using namespace std;

int main() {

    map<char,char> mapper;
    mapper['a'] = 'y';
    mapper['c'] = 'e';
    mapper['b'] = 'h';
    mapper['e'] = 'o';
    mapper['d'] = 's';
    mapper['g'] = 'v';
    mapper['f'] = 'c';
    mapper['i'] = 'd';
    mapper['h'] = 'x';
    mapper['k'] = 'i';
    mapper['j'] = 'u';
    mapper['m'] = 'l';
    mapper['l'] = 'g';
    mapper['o'] = 'k';
    mapper['n'] = 'b';
    mapper['p'] = 'r';
    mapper['s'] = 'n';
    mapper['r'] = 't';
    mapper['u'] = 'j';
    mapper['t'] = 'w';
    mapper['w'] = 'f';
    mapper['v'] = 'p';
    mapper['y'] = 'a';
    mapper['x'] = 'm';
    mapper['z'] = 'q';
    mapper['\n'] = '\n';
    mapper[' '] = ' ';
    mapper['z'] = 'q';
    mapper['q'] = 'z';
    
    int T;
    scanf("%d\n",&T);
    for (int i=1; i<=T ; i++) {
        printf("Case #%d: ", i);
        char next = 'a';
        while (next!='\0' && next!='\n') {
            scanf("%c",&next);
            printf("%c",mapper[next]);
        }
    }

    return 0;
}