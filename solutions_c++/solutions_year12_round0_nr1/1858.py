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
#include <string>
#include <string.h>
using namespace std;
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out1.txt","w",stdout);
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
    
    int t;cin>>t;
    scanf("\n");
    for(int ca=1;ca<=t;ca++)
    {
        string s;
        getline(cin,s);
        string ret = "";
        for(int i=0;i<s.length();i++)
        {
            if(m[s[i]])
                ret+=m[s[i]];
            else 
                ret+=s[i];
        }
        cout<<"Case #"<<ca<<": "<<ret<<endl;
    }
   // while(1);
}
