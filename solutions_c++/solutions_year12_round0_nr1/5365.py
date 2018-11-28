#include <iostream>
#include <string>
#include <map>
#include <cstdio>

using namespace std;

map<char,char> m;
int main()
{

    m['a']='y';
    m['b']='h';
    m['c']='e';
    m['d']='s';
    m['e']='o';
    m['f']='c';
    m['g']='v';
    m['h']='x';
    m['i']='d';
    m['j']='u';
    m['k']='i';
    m['l']='g';
    m['m']='l';
    m['n']='b';
    m['o']='k';
    m['p']='r';
    m['q']='z';
    m['r']='t';
    m['s']='n';
    m['t']='w';
    m['u']='j';
    m['v']='p';
    m['w']='f';
    m['x']='m';
    m['y']='a';
    m['z']='q';
    m[' ']=' ';
    m['\n'] = '\n';

    string s;
    int i,j;
    int n;

    cin >> n;
    getchar();
    for(i = 0; i < n; i++)
    {
        getline(cin, s);

        string t;
        for(j = 0; j < (int)s.size(); j++)
            t+=m[s[j]];
        cout << "Case #"<< i+1 << ": " << t << "\n";
    }
    
    return 0;
}
