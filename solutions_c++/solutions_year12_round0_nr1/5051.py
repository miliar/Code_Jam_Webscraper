#include <iostream>

using namespace std;

char mapa[500];

int
main()
{
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
    mapa['x'] = 'm';
    mapa['y'] = 'a';
    mapa['w'] = 'f';
    mapa['z'] = 'q';
    int cases, i, j ;
    string line;
    cin >> cases;
    getline(cin, line);
    for (j = 1; j <= cases; j++)
    {
        cout << "Case #" << j << ": ";
        getline(cin, line);
        for (i = 0; i < line.size(); i++) {
            if (isalpha(line[i]))
                cout << mapa[line[i]];

            else
                cout << line[i];
        }
        cout << endl;
    }
    return 0;
}
