#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define FOR( i,a,b ) for(int i=a;i<b;i++)
#define VI vector<int>
#define VS vector<string>
#define mp make_pair
#define NS string::npos
using namespace std;
int main()
{
       freopen("a1.txt","r",stdin);
    freopen("aout.txt","w",stdout);

    map <char,char>m;
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
    int n;
    cin>>n;
    cin.ignore();
    int i=1;
    string s;
    while(i<=n)
    {
        getline(cin,s,'\n');
        for(int j=0;j<s.length();j++)
        {
            s[j]=m[s[j]];
        }
        cout<<"Case #"<<i<<": "<<s<<endl;;
        i++;
    }
return 0;
}
