// Mike Terranova
// Compiled with MS Visual Studio 2010
// April 13, 2012

#include <iostream>
#include <iomanip>
#include <fstream>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>
#include <functional>
#include <cmath>
#include <cstdio>

using namespace std;
using namespace std::placeholders;

typedef __int64 int64;

map<char, char> charMap;

int main()
{
    ofstream outfile("out.txt");
    
    charMap['a'] = 'y';
    charMap['b'] = 'h';
    charMap['c'] = 'e';
    charMap['d'] = 's';
    charMap['e'] = 'o';
    charMap['f'] = 'c';
    charMap['g'] = 'v';
    charMap['h'] = 'x';
    charMap['i'] = 'd';
    charMap['j'] = 'u';
    charMap['k'] = 'i';
    charMap['l'] = 'g';
    charMap['m'] = 'l';
    charMap['n'] = 'b';
    charMap['o'] = 'k';
    charMap['p'] = 'r';
    charMap['q'] = 'z';
    charMap['r'] = 't';
    charMap['s'] = 'n';
    charMap['t'] = 'w';
    charMap['u'] = 'j';
    charMap['v'] = 'p';
    charMap['w'] = 'f';
    charMap['x'] = 'm';
    charMap['y'] = 'a';
    charMap['z'] = 'q';
    charMap[' '] = ' ';

    int numCases;
    cin >> numCases;
    
    char bf[255];
    cin.getline(bf, 255);

    for (int i = 1; i <= numCases; i++)
    {
        char buffer[255];
        cin.getline(buffer, 255);

        string input = buffer;
        for (int j = 0; j < input.size(); j++)
        {
            input[j] = charMap[input[j]];
        }

        outfile << "Case #" << i << ": " << input << endl;
    }

    outfile.close();
    return 0;
}

