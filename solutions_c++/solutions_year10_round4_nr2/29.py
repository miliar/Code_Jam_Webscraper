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

int n,Price[2000],F[12][2500],M[2500],Round[12][2500],p,deg[12];

void setPrice(int node,int round)
{
    if (round == 0) return;
    Price[node] = Round[round][++deg[round]];
    setPrice(node*2,round-1);
    setPrice(node*2+1,round-1);
}
void visit(int node,int sx,int sy)
{
    if (sx + 1 == sy)
    {
        F[min(M[sx],M[sy])][node] = Price[node];
        
        if (M[sx] && M[sy])
        F[min(M[sx],M[sy])-1][node] =0 ;
        return;
    }
    int mid = (sx + sy)/2;
    visit(node*2,sx,mid);
    visit(node*2+1,mid+1,sy);
    FOR(i,0,p)
    FOR(j,0,p)
    {
        F[min(i,j)][node] <?= F[i][node*2]+F[j][node*2+1] + Price[node];
        if (i && j)
        F[min(i,j)-1][node] <?= F[i][node*2]+F[j][node*2+1];
    }
}
void solve()
{
    FOR(i,0,p)
    FR(j,1<<p) F[i][j] = oo;
    memset(deg,0,sizeof(deg));
    setPrice(1,p);
    visit(1,0,(1<<p)-1);
    int res = oo;
    FOR(i,0,p) res = min(res,F[i][1]);
    cout << res << endl;
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
        cin >> p;
        FR(i,1 << p) cin >> M[i];
        FOR(i,1,p)
        FOR(j,1,1<<(p-i)) cin >> Round[i][j];
        
        solve();
    }
  //  system("pause");
    return 0;
}
