/*
 *  Author: Exar6
 */

#include <iostream>
#include <map>

using namespace std;

int main()
{
    map<char, char> translate;

    translate['a'] = 'y';
    translate['b'] = 'h';
    translate['c'] = 'e';
    translate['d'] = 's';
    translate['e'] = 'o';
    translate['f'] = 'c';
    translate['g'] = 'v';
    translate['h'] = 'x';
    translate['i'] = 'd';
    translate['j'] = 'u';
    translate['k'] = 'i';
    translate['l'] = 'g';
    translate['m'] = 'l';
    translate['n'] = 'b';
    translate['o'] = 'k';
    translate['p'] = 'r';
    translate['q'] = 'z';
    translate['r'] = 't';
    translate['s'] = 'n';
    translate['t'] = 'w';
    translate['u'] = 'j';
    translate['v'] = 'p';
    translate['w'] = 'f';
    translate['x'] = 'm';
    translate['y'] = 'a';
    translate['z'] = 'q';
    translate[' '] = ' ';

    size_t test_cases = 0;
    
    cin >> test_cases;

    string start;
    string * grese = new string[test_cases];
    string * english = new string[test_cases];

    size_t i = 0;
    getline(cin, start);

    while(i < test_cases)
    {
        getline(cin, grese[i]);

        for(int j = 0; j < grese[i].size(); j++)
        {
            english[i] += translate[ grese[i][j] ];
        }

        i++;
    }

    for(int i = 0; i < test_cases; i++)
    {
        cout << "Case #" << (i + 1) << ": " << english[i];

        if((i + 1) < test_cases)
            cout << endl;
    }

    delete [] grese;
    delete [] english;

    grese = NULL;
    english = NULL;
    
    return 0;
}
