#include <cstdio>
#include <string>
#include <iostream>
#include <map>
using namespace std;

int n;
string x;
map <char, char> lang;

int main()
{
    int i, j;
    freopen ("test.in", "r", stdin);
    freopen ("test.out", "w", stdout);
    lang[' '] = ' ';
    lang['a'] = 'y';
    lang['b'] = 'h';
    lang['c'] = 'e';
    lang['d'] = 's';
    lang['e'] = 'o';
    lang['f'] = 'c';
    lang['g'] = 'v';
    lang['h'] = 'x';
    lang['i'] = 'd';
    lang['j'] = 'u';
    lang['k'] = 'i';
    lang['l'] = 'g';
    lang['m'] = 'l';
    lang['n'] = 'b';
    lang['o'] = 'k';
    lang['p'] = 'r';
    lang['q'] = 'z';
    lang['r'] = 't';
    lang['s'] = 'n';
    lang['t'] = 'w';
    lang['u'] = 'j';
    lang['v'] = 'p';
    lang['w'] = 'f';
    lang['x'] = 'm';
    lang['y'] = 'a';
    lang['z'] = 'q';
    scanf("%d", &n);
    char c;
    scanf("%c", &c);
    for(i = 1; i <= n; ++i) {
        getline(cin, x);
        for(j = 0; j < x.size(); ++j)
            x[j] = lang[x[j]];
        cout << "Case #" << i << ": " << x << "\n";
    }
    return 0;
}
