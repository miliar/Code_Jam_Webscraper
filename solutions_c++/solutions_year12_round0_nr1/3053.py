#include<iostream>
#include<cstdio>
#include<map>

typedef long long LL;

using namespace std;

int main()
{
    map<char, char> g;
    g['a'] = 'y';
    g['b'] = 'h';
    g['c'] = 'e';
    g['d'] = 's';
    g['e'] = 'o';
    g['f'] = 'c';
    g['g'] = 'v';
    g['h'] = 'x';
    g['i'] = 'd';
    g['j'] = 'u';
    g['k'] = 'i';
    g['l'] = 'g';
    g['m'] = 'l';
    g['n'] = 'b';
    g['o'] = 'k';
    g['p'] = 'r';
    g['q'] = 'z';
    g['r'] = 't';
    g['s'] = 'n';
    g['t'] = 'w';
    g['u'] = 'j';
    g['v'] = 'p';
    g['w'] = 'f';
    g['x'] = 'm';
    g['y'] = 'a';
    g['z'] = 'q';
    g[' '] = ' ';

    LL t;
    string str, ans;

    scanf("%lld", &t);
    cin.ignore();

    for(int i=0; i<t; i++){
        getline(cin, str);
        ans = "";

        for(int j=0;j<str.length();j++){
            ans += g[str[j]];
        }

        cout << "Case #" << i+1 << ": " << ans << endl;
    }

    return 0;
}
