#include <map>
#include <string>
#include <iostream>
#include <fstream>

using namespace std;

int main (){
    map <char, char> m;
    m[' '] = ' ';
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
    ifstream fin ("A-small.in");
    ofstream fout ("A-small.out");
    int t;
    fin >>t;
    fin.ignore();
    for (int o = 1; o <= t; o++){
        string h;
        getline (fin, h);
        fout <<"Case #"<<o<<": ";
        for (int i = 0; i< h.size(); i++) fout <<m[h[i]];
        fout <<endl;
    }
}
