#include <iostream>
#include <algorithm>
#include <cmath>
#include <math.h>
#include <stdio.h>
#include <cstring>
#include <vector>
#include <map>
#include <string>
#include <set>
#include <sstream>
#include <queue>
#include <stack>

#define FOR(i,a,b) for(int i = a; i <= b; i++) 
#define DOWN(i,a,b) for(int i = a; i >= b; i--)
#define FORV(i,a) for(typeof(a.begin()) i = a.begin(); i != a.end(); i++)
#define FR(i,a) for(int i = 0; i < a; i++)
#define DR(i,a) for(int i = a-1; i >= 0; i--)
#define REP(i,a) for(int i = 0; i < a; i++)
#define Rep(i,a) for(int i = 0; i < a; i++)
#define For(i,a,b) for(int i = a; i <= b; i++)

#define sqr(x) (x)*(x)
#define dout debug && cout 
#define ll long long
#define sz size()
#define ull unsigned long long
#define pb push_back
#define oo 1000000002
/* DEBUGGING */
bool debug = false;
/* MAIN PROGRAM */

using namespace std;

/****************************************************************/
/* String-number transformation */
long long convertToNum(string s)
{
    long long val = 0;
    FR(i,s.size()) val = val * 10 + s[i] - '0';
    return val;
}
string convertToString(long long a)
{
    string res = "";
    if (!a) return "0";
    while (a)
    {
        res = (char)(a % 10 + 48) + res;
        a /= 10;
    }
    return res;
}
/*--------------------------------*/
long long GCD(long long x,long long y) 
{
    if (!x) return y;
    if (!y) return x;
    if (x == y) return x;
    if (x < y) return GCD(x,y%x); else return GCD(x%y,y);
}
/****************************************************************/
int res = 0;
int n,d[1000204*2];
int get(int u)
{
    int delta = d[u] / 2;
    res += delta;
    d[u-1] += delta;
    d[u+1] += delta;
    d[u] = d[u] - delta*2;
    if (d[u-1] >= 2) get(u-1);
    if (d[u+1] >= 2) get(u+1);
}
int main()
{
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    int ntest,u,v;
    cin >> ntest;
    FOR(test,1,ntest)
    {
        memset(d,0,sizeof(d));
        cin >> n;
        cout << "Case #" << test << ": ";
        res = 0;
        FOR(i,1,n) 
        {
            cin >> u >> v;
            u += 1000202;
            d[u] += v;
            if (d[u] > 1) get(u);
        }
        cout << res << endl;
    }
//    system("pause");
    return 0;
}
