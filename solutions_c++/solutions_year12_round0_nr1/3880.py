#include <map>
#include <iostream>

using namespace std;

map<char,char> mapping;
int main() {

    mapping[' '] = ' ';
    mapping['a'] = 'y';
    mapping['b'] = 'h';
    mapping['c'] = 'e';
    mapping['d'] = 's';
    mapping['e'] = 'o';
    mapping['f'] = 'c';
    mapping['g'] = 'v';
    mapping['h'] = 'x';
    mapping['i'] = 'd';
    mapping['j'] = 'u';
    mapping['k'] = 'i';
    mapping['l'] = 'g';
    mapping['m'] = 'l';
    mapping['n'] = 'b';
    mapping['o'] = 'k';
    mapping['p'] = 'r';
    mapping['q'] = 'z';
    mapping['r'] = 't';
    mapping['s'] = 'n';
    mapping['t'] = 'w';
    mapping['u'] = 'j';
    mapping['v'] = 'p';
    mapping['w'] = 'f';
    mapping['x'] = 'm';
    mapping['y'] = 'a';
    mapping['z'] = 'q';

    int n;
    cin>>n;
    int t=1;
    string s;
    getline(cin, s);
    while (n--) {
        getline(cin, s);
        cout << "Case #" << t << ": ";
        for (int i=0;i<s.size();++i) {
            cout << mapping[s[i]];
        }
        cout << endl;
        ++t;
    }
}
