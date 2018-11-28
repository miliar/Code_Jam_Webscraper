#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

using namespace std;

int main()
{
    int n;
    string line;
    vector<string> lines;
    map<char, char> m;

    m[' '] = ' ';

    m['y'] = 'a';
    m['n'] = 'b';
    m['f'] = 'c';
    m['i'] = 'd';
    m['c'] = 'e';
    m['w'] = 'f';
    m['l'] = 'g';
    m['b'] = 'h';
    m['k'] = 'i';
    m['u'] = 'j';
    m['o'] = 'k';
    m['m'] = 'l';
    m['x'] = 'm';
    m['s'] = 'n';
    m['e'] = 'o';
    m['v'] = 'p';
    m['z'] = 'q';
    m['p'] = 'r';
    m['d'] = 's';
    m['r'] = 't';
    m['j'] = 'u';
    m['g'] = 'v';
    m['t'] = 'w';
    m['h'] = 'x';
    m['a'] = 'y';
    m['q'] = 'z';

    /*
    m['a'] = 'y';
    m['b'] = 'n';
    m['c'] = 'f';
    m['d'] = 'i';
    m['e'] = 'c';
    m['f'] = 'w';
    m['g'] = 'l';
    m['h'] = 'b';
    m['i'] = 'k';
    m['j'] = 'u';
    m['k'] = 'o';
    m['l'] = 'm';
    m['m'] = 'x';
    m['n'] = 's';
    m['o'] = 'e';
    m['p'] = 'v';
    m['q'] = 'z';
    m['r'] = 'p';
    m['s'] = 'd';
    m['t'] = 'r';
    m['u'] = 'j';
    m['v'] = 'g';
    m['w'] = 't';
    m['x'] = 'h';
    m['y'] = 'a';
    m['z'] = 'q';
    */

    ifstream input("A-small-attempt1.in");

    input >> n;

    getline(input, line);
    for(int i = 0; i < n; i++)
    {
        getline(input, line);

        lines.push_back(line);
    }
    input.close();

    ofstream output("A-small-attempt1.out");
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < lines[i].length(); j++)
        {
            lines[i][j] = m[ lines[i][j] ];
        }

        output << "Case #" << i + 1 << ": ";
        output << lines[i];
        output << endl;
    }
    output.close();

    return 0;
}
