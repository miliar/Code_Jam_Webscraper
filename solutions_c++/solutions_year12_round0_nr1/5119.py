#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <stdio.h>
#include <string.h>

using namespace std;

string s;
int i, j, n, t = 1;

map<char, char> alph;

void mount(void) {
    alph[' '] = ' ';
    alph['a'] = 'y';
    alph['b'] = 'h';
    alph['c'] = 'e';
    alph['d'] = 's';
    alph['e'] = 'o';
    alph['f'] = 'c';
    alph['g'] = 'v';
    alph['h'] = 'x';
    alph['i'] = 'd';
    alph['j'] = 'u';
    alph['k'] = 'i';
    alph['l'] = 'g';
    alph['m'] = 'l';
    alph['n'] = 'b';
    alph['o'] = 'k';
    alph['p'] = 'r';
    alph['q'] = 'z';
    alph['r'] = 't';
    alph['s'] = 'n';
    alph['t'] = 'w';
    alph['u'] = 'j';
    alph['v'] = 'p';
    alph['w'] = 'f';
    alph['x'] = 'm';
    alph['y'] = 'a';
    alph['z'] = 'q';
}

int main(void) {
    mount();
    freopen("i.in", "r", stdin);
    freopen("i.out", "w", stdout);
    cin >> n;
    cin.ignore();
    for(i = 0; i < n; i++) {
        getline(cin, s);
        for(j = 0; j < (int) s.size(); j++) {
            s[j] = alph[s[j]];
        }
        cout << "Case #" << (t++) << ": " << s << endl;
    }
    return 0;
}

