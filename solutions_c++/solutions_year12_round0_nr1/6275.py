#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
using namespace std;

#define REP(i,n) for(int i=0;i<n;i++)
#define rep(n) REP(i,n)

const int MAXN=256;
int to[MAXN];

int main()
{
    rep(MAXN) to[i]=i;
    to['a']='y';
    to['b']='h';
    to['c']='e';
    to['d']='s';
    to['e']='o';
    to['f']='c';
    to['g']='v';
    to['h']='x';
    to['i']='d';
    to['j']='u';
    to['k']='i';
    to['l']='g';
    to['m']='l';
    to['n']='b';
    to['o']='k';
    to['p']='r';
    to['q']='z';
    to['r']='t';
    to['s']='n';
    to['t']='w';
    to['u']='j';
    to['v']='p';
    to['w']='f';
    to['x']='m';
    to['y']='a';
    to['z']='q';

    string sn; getline(cin,sn);

    int n=atoi(sn.c_str()); rep(n)
    {
        string s; getline(cin,s); REP(t,s.size())
        {
            s[t]=to[s[t]];
        }

        cout<<"Case #"<<i+1<<": "<<s<<endl;
    }

    return 0;
}

