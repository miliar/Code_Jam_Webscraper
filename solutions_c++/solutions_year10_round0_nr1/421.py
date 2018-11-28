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
int n,k;
int main()
{ 
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    int ntest;
    cin >> ntest;
    int test = 0;
    while (ntest--)
    {
        cout << "Case #" << ++test << ": ";
        cin >> n >> k;
        k %= 1 << n;
        bool ok = true;
        FR(i,n)
        {
            if (!(k % 2)) ok = false;
            k /= 2;
        }
        if (ok) cout << "ON" << endl;
        else cout << "OFF" << endl;
    }
    return 0;
}
