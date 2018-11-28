#include <cstdio>
#include <iostream>
#include <map>
#include <string>
using namespace std;

int main () {
    map<char, char> mapa;
    mapa['a'] = 'y';
    mapa['b'] = 'h';
    mapa['c'] = 'e';
    mapa['d'] = 's';
    mapa['e'] = 'o';
    mapa['f'] = 'c';
    mapa['g'] = 'v';
    mapa['h'] = 'x';
    mapa['i'] = 'd';
    mapa['j'] = 'u';
    mapa['k'] = 'i';
    mapa['l'] = 'g';
    mapa['m'] = 'l';
    mapa['n'] = 'b';
    mapa['o'] = 'k';
    mapa['p'] = 'r';
    mapa['q'] = 'z';
    mapa['r'] = 't';
    mapa['s'] = 'n';
    mapa['t'] = 'w';
    mapa['u'] = 'j';
    mapa['v'] = 'p';
    mapa['w'] = 'f';
    mapa['x'] = 'm';
    mapa['y'] = 'a';
    mapa['z'] = 'q';
    mapa[' '] = ' ';
    int t;
    scanf("%d\n", &t);
    for (int i = 1; i <= t; i++) {
        char s[200];
        gets(s);
        cout << "Case #" << i << ": ";
        for (int i = 0; s[i] != 0; i++) cout << mapa[s[i]];
        cout << endl;
    }
    return 0;
}
