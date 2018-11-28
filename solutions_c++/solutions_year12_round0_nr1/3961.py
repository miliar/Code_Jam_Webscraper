#include <iostream>
#include <algorithm>
#include <map>
#include <stdio.h>

using namespace std;

int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    int n;
    string s;
    map<char,char> m;
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
    m[' '] = ' ';
    cin >> n;
    getline(cin,s);
    for(int j = 1; j <= n; j++){
        getline(cin,s); 
        cout << "Case #" << j << ": ";
        for(int i = 0 , len = s.length(); i < len; i++) {
            cout << m[s[i]]; 
        }
        cout << endl;
    }

    return 0;

}
