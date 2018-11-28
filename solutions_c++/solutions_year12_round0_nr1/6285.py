#include<iostream>
#include<string>
#include<algorithm>
#include <map>
using namespace std;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-out.txt","w",stdout);
    string code;
    string de;
    int T;
    map <char,char> key;
    key['a']='y';
    key['b']='h';
    key['c']='e';
    key['d']='s';
    key['e']='o';
    key['f']='c';
    key['g']='v';
    key['h']='x';
    key['i']='d';
    key['j']='u';
    key['k']='i';
    key['l']='g';
    key['m']='l';
    key['n']='b';
    key['o']='k';
    key['p']='r';
    key['q']='z';
    key['r']='t';
    key['s']='n';
    key['t']='w';
    key['u']='j';
    key['v']='p';
    key['w']='f';
    key['x']='m';
    key['y']='a';
    key['z']='q';
    cin>>T;
    for(int t=0;t<=T;t++)
    {
        getline(cin,code);
        if(t==0) continue;
        cout<<"Case #"<<t<<": ";
        for(int i=0;i<code.size();i++)
        {
            if(code[i]!=' ')
            cout<<key[code[i]];
            else
            cout<<" ";
        }
        cout<<endl;
    }
    return 0;
}
