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
/* DEBUGGING */
bool debug = false;
/* MAIN PROGRAM */

using namespace std;
int D,I,M,n,a[103];
long long F[103][300];
void solve()
{
    long long result = oo,res;
//    FOR(i,1,n)
  //  {
        int i = 1;
        res = (i-1) * D;
        FOR(j,0,255) F[i][j] = abs(j-a[i]);
        FOR(j,i+1,n)
        FOR(k,0,255)
        {
            F[j][k] = (j-1) * D + abs(a[j] - k);
           // F[j][k] = oo;
            FOR(t,0,255)
            {
                //Deleting
                if (t == k) F[j][k] = min(F[j][k],F[j-1][t] + D);
                //Insert
                int len;
                if (M) len = abs(t-k) / M + 1; else len = oo;
                if (M) if (!(abs(t-k) % M)) len--;
                if (M && len)
                F[j][k] = min(F[j][k],F[j-1][t] + I * (len - 1) + abs(k-a[j]) );
                //Change value
                if (abs(t-k) <= M) F[j][k] = min(F[j][k],F[j-1][t] + abs(a[j] - k));
            }
        }
        long long res2 = oo;        
        
        FOR(j,0,255) res2 = min(res2,F[n][j]);
        result = min(result,res+res2);
   // }
    cout << result << endl;
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
        cin >> D >> I >> M >> n;
        FOR(i,1,n) cin >> a[i];
        solve();
    }
    return 0;
}
