#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

int main()
{
    int c;
    string s;
    fin >>c;
    fin.ignore();
    map <char, char> m;
    m['e'] = 'o';
    m['j'] = 'u';
    m['p'] = 'r';
    m['m'] = 'l';
    m['y'] = 'a';
    m['s'] = 'n';
    m['l'] = 'g';
    m['c'] = 'e';
    m['k'] = 'i';
    m['d'] = 's';
    m['x'] = 'm';
    m['v'] = 'p';
    m['n'] = 'b';
    m['r'] = 't';
    m['i'] = 'd';
    m['a'] = 'y';
    m['o'] = 'k';
    m['u'] = 'j';
    m['w'] = 'f';
    m['t'] = 'w';
    m['g'] = 'v';
    m['f'] = 'c';
    m['v'] = 'p';
    m['b'] = 'h';
    m['z'] = 'q';
    m['q'] = 'z';
    m['h'] = 'x';
    m[' '] = ' ';
    for (int k = 0; k < c; k++)
    {
        getline(fin, s);
        fout <<"Case #"<<k+1<<": ";
        for (int i = 0; i < s.size(); i++) fout <<m[s[i]];
        fout <<endl;
    }
    //fin >>c;
}
