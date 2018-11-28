#include <iostream>
using namespace std;

char decode[256];

int main()
{
    decode['a'] = 'y';
    decode['b'] = 'h';
    decode['c'] = 'e';
    decode['d'] = 's';
    decode['e'] = 'o';
    decode['f'] = 'c';
    decode['g'] = 'v';
    decode['h'] = 'x';
    decode['i'] = 'd';
    decode['j'] = 'u';
    decode['k'] = 'i';
    decode['l'] = 'g';
    decode['m'] = 'l';
    decode['n'] = 'b';
    decode['o'] = 'k';
    decode['p'] = 'r';
    decode['q'] = 'z';
    decode['r'] = 't';
    decode['s'] = 'n';
    decode['t'] = 'w';
    decode['u'] = 'j';
    decode['v'] = 'p';
    decode['w'] = 'f';
    decode['x'] = 'm';
    decode['y'] = 'a';
    decode['z'] = 'q';
    decode[' '] = ' ';
    
    int t,l;
    char str[1024];
    cin>>t; cin.get();
    for(int ti = 1; ti <= t; ti++)
    {
        cout<<"Case #"<<ti<<": ";
        cin.getline(str, 1024);
        l = strlen(str);
        for(int i = 0; i < l; i++)
        {
            str[i] = decode[str[i]];
        }
        cout<<str<<endl;
    }
    return 0;
}
