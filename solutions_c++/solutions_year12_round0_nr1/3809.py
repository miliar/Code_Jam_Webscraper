#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <fstream>
using namespace std;

int main() {
    ifstream fin;
    ofstream fout;
    fin.open("A1.in");
    fout.open("A1.out");
    map <char,char> m;
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
    int n;
    fin >> n;
    fin.ignore();
    for (int i = 1; i <= n; ++i) {
        fout << "Case #" << i << ": ";
        string s;
        getline(fin,s);
        for (int j = 0; j < s.size(); ++j) fout << m[s[j]];
        fout << endl;
    }
    fin.close();
    fout.close();
    system ("pause");
}
