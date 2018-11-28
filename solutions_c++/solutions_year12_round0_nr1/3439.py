#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <set>
#include <cstdio>
#define INT_MAX 2147483647
#define INT_MIN -2147483648
#define pi acos(-1.0)
#define N 1000000
#define long long LL

using namespace std;

int main()
{
    map<char,char> m;
    m['f'] =  'c';
    m['g'] =  'v';
    m['d'] =  's';
    m['e'] =  'o';
    m['b'] =  'h';
    m['c'] =  'e';
    m['a'] =  'y';
    m['n'] =  'b';
    m['o'] =  'k';
    m['l'] =  'g';
    m['m'] =  'l';
    m['j'] =  'u';
    m['k'] =  'i';
    m['h'] =  'x';
    m['i'] =  'd';
    m['w'] =  'f';
    m['v'] =  'p';
    m['u'] =  'j';
    m['t'] =  'w';
    m['s'] =  'n';
    m['r'] =  't';
    m['p'] =  'r';
    m['y'] =  'a';
    m['x'] =  'm';
    m['z'] =  'q';
    m['q'] =  'z';
    freopen("A-small-attempt0.in","r",stdin);
    freopen("salida.out","w",stdout);
    char x[110];
    int t,c=1;
    gets(x);
    t=atoi(x);
    while(t-->0)
    {
        gets(x);
        for(int i=0; x[i]!='\0'; i++)
            if(x[i]>='a'&& x[i]<='z')
                x[i]=m[x[i]];
            else if(x[i]>='A'&& x[i]<='Z')
                x[i]=(char)((m[x[i]+32])-32);
        cout<<"Case #"<<c++<<": "<<x<<endl;
    }
    return 0;
}
