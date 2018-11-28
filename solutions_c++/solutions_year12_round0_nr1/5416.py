#include <iostream>
#include <cstdio>
#include <map>
#include <string>

using namespace std;

map<char,char> dict;

int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);

    int t; cin >> t; cin.ignore();

    dict[' '] = ' ';
dict['a'] = 'y';
dict['b'] = 'h';
dict['c'] = 'e';
dict['d'] = 's';
dict['e'] = 'o';
dict['f'] = 'c';
dict['g'] = 'v';
dict['h'] = 'x';
dict['i'] = 'd';
dict['j'] = 'u';
dict['k'] = 'i';
dict['l'] = 'g';
dict['m'] = 'l';
dict['n'] = 'b';
dict['o'] = 'k';
dict['p'] = 'r';
dict['q'] = 'z';
dict['r'] = 't';
dict['s'] = 'n';
dict['t'] = 'w';
dict['u'] = 'j';
dict['v'] = 'p';
dict['w'] = 'f';
dict['x'] = 'm';
dict['y'] = 'a';
dict['z'] = 'q';

    for ( int i = 0 ; i < t ; ++i )
    {
        string s1;
        getline(cin,s1);

        cout << "Case #"<< i+1 << ": ";
        for ( int k = 0 ; k < s1.length() ; ++k )
            cout << dict[s1[k]];
        cout << "\n";
    }

    return 0;
}
