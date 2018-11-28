#include <iostream>
#include <map>
#include <string>
using namespace std;
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    map <char,char> m;
    m[' ']=' ';
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
    int t;
    cin>>t;
    char p[200];
    cin.getline(p,200);
    for (int i=1; i<=t; i++)
    {
        char q[200];
        cin.getline(q,200);
        string s=string(q);
        for (int j=0; j<s.size(); j++)
            s[j]=m[s[j]];
        cout<<"Case #"<<i<<": "<<s<<endl;
    }
    return 0;
}
