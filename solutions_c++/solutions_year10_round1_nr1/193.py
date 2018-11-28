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
char a[100][100],b[100][100];
int m,n,k;
void solve()
{
    bool Red = false, Blue = false;
    //Ngang
    FOR(i,1,n)
    {
        FOR(j,1,n-k+1)
        {
            bool flag = true;
            FOR(t,j,j+k-1)
            if (a[i][t] != 'R') flag = false;
            if (flag) Red = true;
            
            flag = true;
            FOR(t,j,j+k-1)
            if (a[i][t] != 'B') flag = false;
            if (flag) Blue = true;
        }
    }
    // Doc
    FOR(j,1,n)
    {
        FOR(i,1,n-k+1)
        {
            bool flag = true;
            FOR(t,i,i+k-1)
            if (a[t][j] != 'R') flag = false;
            if (flag) Red = true;
            
            flag = true;
            FOR(t,i,i+k-1)
            if (a[t][j] != 'B') flag = false;
            if (flag) Blue = true;
        }
    }
    // Cheo chinh
    FOR(i,1,n-k+1)
    FOR(j,1,n-k+1)
    {
        bool flag = true;
        FOR(t,0,k-1)
        if (a[i+t][j+t] != 'R') flag = false;
        if (flag) Red = true;
        
        flag = true;
        FOR(t,0,k-1)
        if (a[i+t][j+t] != 'B') flag = false;
        if (flag) Blue = true;
    }
    
    // Cheo phu
    
    FOR(i,k,n)
    FOR(j,1,n-k+1)
    {
        bool flag = true;
        FOR(t,0,k-1)
        if (a[i-t][j+t] != 'R') flag = false;
        if (flag) Red = true;
        
        flag = true;
        FOR(t,0,k-1)
        if (a[i-t][j+t] != 'B') flag = false;
        if (flag) Blue = true;
    }
    
    if (Red && Blue) cout << "Both" << endl;
    else if (!Red && !Blue) cout << "Neither" << endl;
    else if (Red) cout << "Red" << endl;
    else cout << "Blue" << endl;
}

int main()
{ 
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    int ntest;
    cin >> ntest;
    FOR(test,1,ntest)
    {
        cout << "Case #" << test << ": " ;
        cin >> n >> k;
        FOR(i,1,n)
        FOR(j,1,n) cin >> a[i][j];
        FOR(i,1,n)
        {
            int j2 = n + 1;
            DOWN(j,n,1)
            if (a[i][j] != '.')
            b[i][--j2] = a[i][j];
            DOWN(j,j2-1,1) b[i][j] = '.';
        }
        FOR(i,1,n) FOR(j,1,n) a[i][j] = b[i][j];
        solve();
    }
    return 0;
}
