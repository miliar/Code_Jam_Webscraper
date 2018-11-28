#include<iostream>
#include<cstdio>
#include<vector>
#include<queue>
#include<stack>
#include<cstring>
#include<algorithm>
#include<map>
using namespace std;
#define rep(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=a;i<(b);i++)
#define pb push_back
#define F first
#define S second
#define all(c) c.begin(),c.end()
#define dbg(x) cout<<#x<<" : "<<x<<"\n";
#define v(x) vector<x>
int main()
{
    freopen("a.in","r",stdin);
    freopen("out.out","w",stdout);
    int cas=1;
    int t;
    scanf("%d\n",&t);
    map<char,char> m;
    m['y']='a';m['n']='b';m['f']='c';m['i']='d';
    m['c']='e';m['w']='f';m['l']='g';m['b']='h';m['k']='i';m['u']='j';
    m['o']='k';m['m']='l';m['x']='m';m['s']='n';m['e']='o';m['v']='p';m['z']='q';
    m['p']='r';m['d']='s';m['r']='t';
    m['j']='u';m['g']='v';m['t']='w';m['h']='x';m['a']='y';m['q']='z';m[' ']=' ';
    while(t--)
    {
        string a;
        getline(cin,a);
        for(int i=0;i<a.length();i++)
        {
            a[i]=m[a[i]];
        }
        cout<<"Case #"<<cas <<":"<<" "<<a<<"\n";
        cas++;
    }
}
