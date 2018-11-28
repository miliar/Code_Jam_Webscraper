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
int a[104],n;
long long L,f[1000001];
long long oo= 1000000000;
void solve()
{
    sort(a+1,a+n+1);
    long long res = 0;
    if (L >= 100000)
    {
        long long delta = L - 100000;
        res = delta/a[n];
        L -= res * a[n];
    }
    while (L >= 100000)
    {
        L-=a[n];
        res++;
    }
    FOR(i,1,L) f[i] = oo;
    f[0] = 0;
    FOR(i,1,n)
    FOR(j,0,L) 
    if (j >= a[i]) f[j] <?= f[j-a[i]] + 1;
    if (f[L] == oo) cout  << "IMPOSSIBLE" << endl;
    else
    cout << f[L] + res << endl;
}
int main()
{
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    int ntest;
    cin >> ntest;
    oo *= oo;
    FOR(test,1,ntest)
    {
        cout << "Case #" << test << ": ";
        cin >> L >> n;
        FOR(i,1,n) cin >> a[i];
        solve();
    }
//    system("pause");
    return 0;
}
