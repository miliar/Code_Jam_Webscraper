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
int cnt,a[101][101];

void solve()
{
    if (!cnt)
    {
        cout << 0 << endl;
        return ;
    }
    FOR(t,1,10000)
    {
        DOWN(i,100,1)
        DOWN(j,100,1)
        {
            if (a[i][j] == 1 && a[i-1][j] == 0 && a[i][j-1] == 0)
            a[i][j] = 0,cnt--;
            if (a[i][j] == 0 && a[i-1][j] == 1 && a[i][j-1] == 1)
            a[i][j] = 1,cnt++;
        }
        if (!cnt)
        {
            cout << t << endl;
            return;
        }
    }
}
int main()
{
    freopen("test.inp","r",stdin);
    freopen("test.out","w",stdout);
    int ntest;
    cin >> ntest;
    int R,x1,y1,x2,y2;
    FOR(test,1,ntest)
    {
        cout << "Case #" << test << ": ";
        cin >> R;
        memset(a,0,sizeof(a));
        cnt = 0;
        FOR(i,1,R)
        {
            cin >> y1 >> x1 >> y2 >> x2;
            FOR(j,x1,x2)
            FOR(k,y1,y2) 
            if (!a[j][k])
            {
                a[j][k] = 1;
                cnt++;
            }
        }
        solve();
    }
  //  system("pause");
    return 0;
}
