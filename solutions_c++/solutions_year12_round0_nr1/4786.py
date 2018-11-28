#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string>
#include <memory.h>

using namespace std;

char m[128];
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    string str;
    m['y']='a';
    m['n']='b';
    m['f']='c';
    m['i']='d';
    m['c']='e';
    m['w']='f';
    m['l']='g';
    m['b']='h';
    m['k']='i';
    m['u']='j';
    m['o']='k';
    m['m']='l';
    m['x']='m';
    m['s']='n';
    m['e']='o';
    m['v']='p';
    m['z']='q';
    m['p']='r';
    m['d']='s';
    m['r']='t';
    m['j']='u';
    m['g']='v';
    m['t']='w';
    m['h']='x';
    m['a']='y';
    m['q']='z';
    m[' ']=' ';
    cin >> T;
    getline(cin,str);
    for (int times=1;times<=T;times++)
    {
        getline(cin,str);
        for (int i=0;i<str.length();i++)
            str[i]=m[str[i]];
        cout << "Case #" <<  times << ": " << str << endl;
    }
}
