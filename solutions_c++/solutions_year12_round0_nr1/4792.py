#include<iostream>
#include<map>

using namespace std;

int main() {
    map<char,char> mapa;
    mapa['a'] = 'y';    mapa['b'] = 'h';    mapa['c'] = 'e';    mapa['d'] = 's';
    mapa['e'] = 'o';    mapa['f'] = 'c';    mapa['g'] = 'v';    mapa['h'] = 'x';
    mapa['i'] = 'd';    mapa['j'] = 'u';    mapa['k'] = 'i';    mapa['l'] = 'g';
    mapa['m'] = 'l';    mapa['n'] = 'b';    mapa['o'] = 'k';    mapa['p'] = 'r';
    mapa['q'] = 'z';    mapa['r'] = 't';    mapa['s'] = 'n';    mapa['t'] = 'w';
    mapa['u'] = 'j';    mapa['v'] = 'p';    mapa['w'] = 'f';    mapa['y'] = 'a';
    mapa['x'] = 'm';    mapa['z'] = 'q';
    int n;
    cin >> n;
    string s;
    getline(cin,s);
    for (int k=1;k<=n;k++) {
        getline(cin,s);
        for (unsigned int l=0;l<s.size();l++)
            if (s[l] != ' ')
               s[l] = mapa[ s[l] ];
        cout << "Case #" << k << ": " << s << endl;
    }
    return 0;
}
