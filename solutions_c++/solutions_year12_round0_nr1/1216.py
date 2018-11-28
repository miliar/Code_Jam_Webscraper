#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>

using namespace std;
const int maxn=100000;

char c[300];
string str1;
string str2;
int main ()
{
    int cas;
    c['a']='y';
    c['b']='h';
    c['c']='e';
    c['d']='s';
    c['e']='o';
    c['f']='c';
    c['g']='v';
    c['h']='x';
    c['i']='d';
    c['j']='u';
    c['k']='i';
    c['l']='g';
    c['m']='l';
    c['n']='b';
    c['o']='k';
    c['p']='r';
    c['q']='z';
    c['r']='t';
    c['s']='n';
    c['t']='w';
    c['u']='j';
    c['v']='p';
    c['w']='f';
    c['x']='m';
    c['y']='a';
    c['z']='q';
    c[' ']=' ';
    freopen("1.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &cas);
    getchar();
    for (int I=1; I<=cas; ++I)
    {
        getline(cin,str1);
        int l1=str1.size();
        for(int i=0; i<l1; ++i)
        {
            str1[i]=c[str1[i]];
        }
        cout << "Case #" << I << ": " << str1 << endl;
    }
    return 0;
}
