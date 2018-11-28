#include <cstdlib>
#include <iostream>
#include <fstream>
#include "Map.h"

using namespace std;

int main(int argc, char *argv[])
{
    ifstream in; ofstream out; in.open("./input.txt"); out.open("./output.txt");
    char d;
    map <char, char> g;
    g['y'] = 'a';
    g['n'] = 'b';
    g['f'] = 'c';
    g['i'] = 'd';
    g['c'] = 'e';
    g['w'] = 'f';
    g['l'] = 'g';
    g['b'] = 'h';
    g['k'] = 'i';
    g['u'] = 'j';
    g['o'] = 'k';
    g['m'] = 'l';
    g['x'] = 'm';
    g['s'] = 'n';
    g['e'] = 'o';
    g['v'] = 'p';
    g['z'] = 'q';
    g['p'] = 'r';
    g['d'] = 's';
    g['r'] = 't';
    g['j'] = 'u';
    g['g'] = 'v';
    g['t'] = 'w';
    g['h'] = 'x';
    g['a'] = 'y';
    g['q'] = 'z';
    g[' '] = ' ';

    
    int count = 0, i = 0, j = 0;
    in >> count;
    
    string s; getline(in, s);
    for( j = 1; j <= count; j++ ){
        getline(in, s);
        out << "Case #" << j << ": ";
        for( i = 0; i < s.size(); i++)
            out << g[s[i]];
        out << "\n";
    }
    
    in.close(); out.close(); system("PAUSE");
    return EXIT_SUCCESS;
}
