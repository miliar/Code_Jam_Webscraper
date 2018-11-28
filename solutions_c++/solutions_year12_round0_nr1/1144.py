#include <iostream>
#include <cstdio>
#include <string>
#include <map>
using namespace std;

map<char, char> dict;

void initMap()
{
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
}

char translate(char ch)
{
    return dict[ch]; 
}

string solve(string inp)
{
    string res = "";   
       
    for (int i = 0; i < inp.size(); i++)
    {
        char ch = inp[i];
        if (ch == ' ') { res += ch; continue; }
        
        res += translate(ch);
    }
       
    return res;   
}

int main()
{
    initMap();
    
    int T; cin >> T;
    cin.ignore();
    
    for (int t = 1; t <= T; t++)
    {
        string inp; getline(cin, inp);
        
        string result = solve(inp);
        printf("Case #%d: %s\n", t, result.c_str());
    }
    
    return 0;
}
