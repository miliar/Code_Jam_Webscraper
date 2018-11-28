#include <iostream>
using namespace std;

char trans[256];

int main()
{
    trans['a'] = 'y';
    trans['b'] = 'h';
    trans['c'] = 'e';
    trans['d'] = 's';
    trans['e'] = 'o';
    trans['f'] = 'c';
    trans['g'] = 'v';
    trans['h'] = 'x';
    trans['i'] = 'd';
    trans['j'] = 'u'; 
    trans['k'] = 'i';
    trans['l'] = 'g';
    trans['m'] = 'l';
    trans['n'] = 'b';
    trans['o'] = 'k';
    trans['p'] = 'r';
    trans['q'] = 'z';
    trans['r'] = 't';
    trans['s'] = 'n';
    trans['t'] = 'w';
    trans['u'] = 'j';
    trans['v'] = 'p';
    trans['w'] = 'f';
    trans['x'] = 'm';
    trans['y'] = 'a';
    trans['z'] = 'q';
    
    int n;
    cin >> n;
    string a;
    getline(cin, a);
    for (int i = 0; i < n; i++)
    {
        string line;
        getline(cin, line);
        for (int j = 0; j < line.length(); j++) if (line[j] != ' ')
        {
            line[j] = trans[line[j]];
        }
        cout << "Case #" << i+1 << ": " << line << endl;
    }
}
