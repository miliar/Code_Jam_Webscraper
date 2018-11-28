#include<iostream>
#include<vector>
#include<map>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<queue>
#include<fstream>
#include<sstream>
#include<stack>
#include<list>
#include<deque>
#include<bitset>
#include<utility>
#include<climits>
#include<iomanip>
#include<ctime>
#include<complex>
using namespace std;
map<char,char>M;


void pre()
{
M['a']='y';
M['b']='h';
M['c']='e';
M['d']='s';
M['e']='o';
M['f']='c';
M['g']='v';
M['h']='x';
M['i']='d';
M['j']='u';
M['k']='i';
M['l']='g';
M['m']='l';
M['n']='b';
M['o']='k';
M['p']='r';
M['q']='z';
M['r']='t';
M['s']='n';
M['t']='w';
M['u']='j';
M['v']='p';
M['w']='f';
M['x']='m';
M['y']='a';
M['z']='q';
M[' ']=' ';
}

int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("out1.txt","w",stdout);
    pre();
    string s1;
    char C[5];
    int ks,cas,i;
    cin>>ks;
    gets(C);
    for(cas=1;cas<=ks;cas++)
    {
        cout<<"Case #"<<cas<<": ";
        getline(cin,s1);
        for(i=0;i<s1.length();i++)
        {
            cout<<M[s1[i] ];
        }

        cout<<endl;
    }
return 0;
}
