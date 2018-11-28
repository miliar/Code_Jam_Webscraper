#include <iostream>
#include <cstdio>
#include <map>
#include <cstring>
using namespace std;

map<char,char> h;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    h['a'] = 'y';
    h['b'] = 'h';
    h['c'] = 'e';
    h['d'] = 's';
    h['e'] = 'o';
    h['f'] = 'c';
    h['g'] = 'v';
    h['h'] = 'x';
    h['i'] = 'd';
    h['j'] = 'u';
    h['k'] = 'i';
    h['l'] = 'g';
    h['m'] = 'l';
    h['n'] = 'b';
    h['o'] = 'k';
    h['p'] = 'r';
    h['q'] = 'z';
    h['r'] = 't';
    h['s'] = 'n';
    h['t'] = 'w';
    h['u'] = 'j';
    h['v'] = 'p';
    h['w'] = 'f';
    h['x'] = 'm';
    h['y'] = 'a';
    h['z'] = 'q';
    h[' '] = ' ';

    int T;
    char sir[128];
    cin>>T;
    cin.getline(sir, 128);
    for(int i = 1; i <= T; i++)
    {
        cin.getline(sir, 128);
        for(int j = 0; j < strlen(sir); j++)
        {
            sir[j] = h[sir[j]];
        }
        cout<<"Case #"<<i<<": "<<sir<<endl;
    }

    return 0;
}
