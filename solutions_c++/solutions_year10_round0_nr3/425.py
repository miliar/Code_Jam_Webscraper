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
int R,k,n;
int a[1004];
long long result;
long long F[1004],G[1004];

void solve()
{
    long long S = 0,delta;
    FOR(i,1,n) S += a[i];
    k <?= S;
    memset(F,-1,sizeof(F));
    int cnt = 0, cur = 1,len ;
    result = 0;
    while (R)
    {
        R--;
        cnt++;
        int i = cur;
        long long sum = 0;
        while (true)
        {
            if (sum + a[i] > k) break;
            sum += a[i];
            i++;
            if (i > n) i = 1; 
        }
        result += sum;
        if (F[cur] != -1)
        {
            delta = result - G[cur];
            len = cnt - F[cur];
            result += delta * (R / len);
            R %= len;
        } else 
        {
            F[cur] = cnt;
            G[cur] = result;
        }
        cur = i;
    }
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
        cin >> R >> k >> n;
        FOR(i,1,n) cin >> a[i];
        solve();        
    }
    return 0;
}
