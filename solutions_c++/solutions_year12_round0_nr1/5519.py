#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <map>
#include <sstream>
using namespace std;

string s;
int t;
map<char, char> mp;

int main() {
    freopen("a-small.in", "r", stdin);
    freopen("a-small.out", "w", stdout);
    mp['a'] = 'y';
    mp['b'] = 'h';
    mp['c'] = 'e';
    mp['d'] = 's';
    mp['e'] = 'o';
    mp['f'] = 'c';
    mp['g'] = 'v';
    mp['h'] = 'x';
    mp['i'] = 'd';
    mp['j'] = 'u';
    mp['k'] = 'i';
    mp['l'] = 'g';
    mp['m'] = 'l';
    mp['n'] = 'b';
    mp['o'] = 'k';
    mp['p'] = 'r';
    mp['q'] = 'z';
    mp['r'] = 't';
    mp['s'] = 'n';
    mp['t'] = 'w';
    mp['u'] = 'j';
    mp['v'] = 'p';
    mp['w'] = 'f';
    mp['x'] = 'm';
    mp['y'] = 'a';
    mp['z'] = 'q';
    getline(cin, s);
    istringstream in(s);
    in >> t;
    int xx = 1;
    while (t--) {
        getline(cin, s);
        printf("Case #%d: ", xx++);
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == ' ') printf("%c", s[i]);
            else printf("%c", mp[s[i]]);
        }
        printf("\n");
    }
    return 0;
}
