#include<iostream>
#include<stdio.h>
#include<string>
#include<string.h>
#include<algorithm>
#include<vector>
#include<map>
using namespace std;


int main()
{
    int t;
    cin>>t;
    char m[1000];
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
    string s;
    getline(cin,s);
    for(int tt=1;tt<=t;tt++)
    {
        string s;
        getline(cin,s);
        for(int i=0;i<s.length();i++)
        {
            s[i]=m[s[i]];
        }
        cout<<"Case #"<<tt<<": "<<s<<endl;
    }
    return 0;
}
