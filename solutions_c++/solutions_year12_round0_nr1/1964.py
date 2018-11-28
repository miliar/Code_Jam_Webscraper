#include <iostream>
#include <cstring>

using namespace std;


int main() {

    ios_base::sync_with_stdio(0);

    char mapping[255];

    mapping[' '] = ' ';
    mapping['a'] = 'y';
    mapping['b'] = 'h';
    mapping['c'] = 'e';
    mapping['d'] = 's';
    mapping['e'] = 'o';
    mapping['f'] = 'c';
    mapping['g'] = 'v';
    mapping['h'] = 'x';
    mapping['i'] = 'd';
    mapping['j'] = 'u';
    mapping['k'] = 'i';
    mapping['l'] = 'g';
    mapping['m'] = 'l';
    mapping['n'] = 'b';
    mapping['o'] = 'k';
    mapping['p'] = 'r';
    mapping['q'] = 'z';
    mapping['r'] = 't';
    mapping['s'] = 'n';
    mapping['t'] = 'w';
    mapping['u'] = 'j';
    mapping['v'] = 'p';
    mapping['w'] = 'f';
    mapping['x'] = 'm';
    mapping['y'] = 'a';
    mapping['z'] = 'q';


    int n;
    cin >> n;

    string line;

    getline(cin, line);

    for(int i=0; i<n; ++i) {
        getline(cin, line);

        cout << "Case #" << i+1 << ": ";

        for(int j=0; j<line.length(); ++j) {
            cout << mapping[line[j]];
        }

        cout << "\n";
    }

    return 0;
}
