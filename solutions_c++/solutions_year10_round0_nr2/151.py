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

#define FOR(i,a,b) for(int i = a; i <= b; i++) 
#define DOWN(i,a,b) for(int i = a; i >= b; i--)
#define FORV(i,a) for(typeof(a.begin()) i = a.begin(); i != a.end(); i++)
#define FR(i,a) for(int i = 0; i < a; i++)
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
#define maxn 1003
/* DEBUGGING */
bool debug = false;
/* MAIN PROGRAM */

using namespace std;
long long a[2000],b[2000],S;
int n;
long long GCD(long long x,long long y)
{
    if (!x) return y;
    if (!y) return x;
    if (x == y) return x;
    if (x < y) return GCD(x,y % x);
    else return GCD(x % y,y);
}
int main()
{ 
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    int ntest;
    cin >> ntest;
    FOR(test,1,ntest)
    {
        cout << "Case #" << test << ": ";
        cin >> n;
        FOR(i,1,n) cin >> a[i];
        FOR(i,1,n-1) b[i] = abs(a[i+1] - a[i]);
        S = b[1];
        FOR(i,2,n-1) S = GCD(S,b[i]);
        long long u = a[1] % S;
        if (!u) cout << "0" << endl;
        else cout << S - u << endl;
    }
    return 0;
}
