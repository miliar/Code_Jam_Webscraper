#include <iostream>
#include <fstream>
#include <map>

using namespace std;

main()
{
    ifstream fin("A-small-attempt1.in");
    ofstream fout("gcj out.txt");
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
    m[' '] = ' ';
    int x;
    string s;
    fin >> x;
    getline(fin, s);
    for (int c = 1; c <= x; ++c)
    {
        fout << "Case #" << c << ": ";
        getline(fin, s);
        for (int i = 0; i < s.size(); ++i)
            fout << m[s[i]];
        fout << endl;
    }
}
