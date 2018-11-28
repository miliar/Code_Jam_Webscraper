#include <iostream>
#include <cstdio>
#include <map>

using namespace std;

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    map<char, char> m;
    m['a']= 'y';
    m['b']= 'h';
    m['c']= 'e';
    m['d']= 's';
    m['e']= 'o';
    m['f']= 'c';
    m['g']= 'v';
    m['h']= 'x';
    m['i']= 'd';
    m['j']= 'u';
    m['k']= 'i';
    m['l']= 'g';
    m['m']= 'l';
    m['n']= 'b';
    m['o']= 'k';
    m['p']= 'r';
    m['q']= 'z';
    m['r']= 't';
    m['s']= 'n';
    m['t']= 'w';
    m['u']= 'j';
    m['v']= 'p';
    m['w']= 'f';
    m['x']= 'm';
    m['y']= 'a';
    m['z']= 'q';

    int tt;
    string s;
    cin >> tt;
    getline(cin, s);
    for (int t = 1; t <= tt; ++t)
    {
        getline(cin, s);
        int n = s.size();
        for (int i = 0; i != n; ++i)
        {
            if (s[i] >= 'a' && s[i] <= 'z')
            {
                s[i] = m[s[i]];
            }
        }
        cout << "Case #" << t << ": " << s << endl;
    }
    return 0;
}
