#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <bitset>
#include <functional>
#include <utility>//pair
#include <iomanip>
using namespace std;

map <char,char> p;
string s,ans;

int main()
{
    freopen("A-small-attempt3.in","r",stdin);
    freopen("A-small-attempt3.out","w",stdout);
    int n,i,j,k;
    p[' '] = ' ';
    p['a'] = 'y';
    p['b'] = 'h';
    p['c'] = 'e'; 
    p['d'] = 's'; 
    p['e'] = 'o';
    p['f'] = 'c'; 
    p['g'] = 'v'; 
    p['h'] = 'x'; 
    p['i'] = 'd'; 
    p['j'] = 'u'; 
    p['k'] = 'i'; 
    p['l'] = 'g'; 
    p['m'] = 'l'; 
    p['n'] = 'b'; 
    p['o'] = 'k'; 
    p['p'] = 'r'; 
    p['q'] = 'z'; 
    p['r'] = 't'; 
    p['s'] = 'n'; 
    p['t'] = 'w'; 
    p['u'] = 'j'; 
    p['v'] = 'p'; 
    p['w'] = 'f'; 
    p['x'] = 'm'; 
    p['y'] = 'a'; 
    p['z'] = 'q';
    scanf("%d",&n);
    getchar();
    j = 1;
    while(n--)
    {
        ans.clear();
        getline(cin,s);
        printf("Case #%d: ",j++);
        for( i = 0; i < s.size(); ++i)
        {
            ans += p[s[i]];
        }
        for( i = ans.size() - 1; i >= 0; --i) if(ans[i] != ' ') break;
        for( k = 0; k <= i; ++k) cout << ans[k];
        puts("");
    }
    return 0;
}













