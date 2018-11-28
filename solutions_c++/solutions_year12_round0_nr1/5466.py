#include <iostream>
#include <map>
using namespace std;

map<char, char> m;
void init();
int main()
{
    init();
    int n;
    cin >> n;
    string s;
    int cases = 1;
    getline(cin, s);
    for (int j = 0; j < n; j++)
    {
        getline(cin, s);
        for (size_t i = 0; i < s.size(); i++)
        {
            if (s[i] >= 'a' && s[i] <= 'z')
                s[i] = m[s[i]];
        }
        cout<<"Case #"<<cases++<<": "<<s<<endl;
    }
    return 0;
}

void init()
{
    m['y'] = 'a';
    m['n'] = 'b';
    m['f'] = 'c';
    m['i'] = 'd';
    m['c'] = 'e';
    m['w'] = 'f';
    m['l'] = 'g';
    m['b'] = 'h';
    m['k'] = 'i';
    m['u'] = 'j';
    m['o'] = 'k';
    m['m'] = 'l';
    m['x'] = 'm';
    m['s'] = 'n';
    m['e'] = 'o';
    m['v'] = 'p';
    m['z'] = 'q';
    m['p'] = 'r';
    m['d'] = 's';
    m['r'] = 't';
    m['j'] = 'u';
    m['g'] = 'v';
    m['t'] = 'w';
    m['h'] = 'x';
    m['a'] = 'y';
    m['q'] = 'z';
    
}
