#include <iostream>
#include <string>
#include <map>

using namespace std;

int main() {
    string x;
    map<char, char> m;

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

    int n;
    cin >> n;
    getline(cin, x);
    for(int i = 1; i<=n;i++) {
        getline(cin, x);
        cout << "Case #" << i << ": ";
        for(int j = 0; j<x.size(); j++) {
            if(x[j] == ' ')
                cout << " ";
            else
                cout << m[x[j]];
        }
        cout << endl;
    }
    return 0;
}
