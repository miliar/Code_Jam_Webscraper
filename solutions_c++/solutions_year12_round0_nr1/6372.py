#include <iostream>
#include <map>
#include <string>
#include <sstream>

using namespace std;

int main() {
    map<char,char> cipher;
    cipher[' '] = ' ';
    cipher['a'] = 'y';
    cipher['A'] = 'Y';
    cipher['b'] = 'h';
    cipher['B'] = 'H';
    cipher['c'] = 'e';
    cipher['C'] = 'E';
    cipher['d'] = 's';
    cipher['D'] = 'S';
    cipher['e'] = 'o';
    cipher['E'] = 'O';
    cipher['f'] = 'c';
    cipher['F'] = 'C';
    cipher['g'] = 'v';
    cipher['G'] = 'V';
    cipher['h'] = 'x';
    cipher['H'] = 'X';
    cipher['i'] = 'd';
    cipher['I'] = 'D';
    cipher['j'] = 'u';
    cipher['J'] = 'U';
    cipher['k'] = 'i';
    cipher['K'] = 'I';
    cipher['l'] = 'g';
    cipher['L'] = 'G';
    cipher['m'] = 'l';
    cipher['M'] = 'L';
    cipher['n'] = 'b';
    cipher['N'] = 'B';
    cipher['o'] = 'k';
    cipher['O'] = 'K';
    cipher['p'] = 'r';
    cipher['P'] = 'R';
    cipher['q'] = 'z';
    cipher['Q'] = 'Z';
    cipher['r'] = 't';
    cipher['R'] = 'T';
    cipher['s'] = 'n';
    cipher['S'] = 'N';
    cipher['t'] = 'w';
    cipher['T'] = 'W';
    cipher['u'] = 'j';
    cipher['U'] = 'J';
    cipher['v'] = 'p';
    cipher['V'] = 'P';
    cipher['w'] = 'f';
    cipher['W'] = 'F';
    cipher['x'] = 'm';
    cipher['X'] = 'M';
    cipher['y'] = 'a';
    cipher['Y'] = 'A';
    cipher['z'] = 'q';
    cipher['Z'] = 'Q';


    string g, inLine;
    int t;
    getline(cin, inLine);
    stringstream(inLine)>>t;

    for(int i = 1; i <= t; ++i) {
        getline(cin, g);

        cout<<"Case #"<<i<<": ";
        for(int j = 0; j < g.length(); ++j) {
            cout<<cipher[g[j]];
        }
        cout<<endl;

    }
    return 0;
}
