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
long long POW(long long x,long long y,long long Base)
{
    if (!y) return 1;
    long long u = POW(x,y/2,Base);
    u = (u * u) % Base;
    if (!(y & 1)) return u;
    else return (u * x) % Base;
}
/****************************************************************/
bool Prime[1000003];
int s[100000],top,d,k,P,a[1000],resx[100003];
void solve(int val)
{
    if (k == 2)
    {
        if (a[1] == a[2]) cout << a[1] << endl;
        else cout << "I don't know." << endl;
        return;
    }
    FOR(i,2,k)
    if (a[i] == a[i-1])
    {
        cout << a[i] << endl;
        return;
    }
    long long valx,valy,P,A,B,cnt =0;
    FOR(i,1,top)
    if (s[i] <= val)
    {
        P = s[i];
        bool fi = true;
        FOR(j,1,k)
        if (a[j] >= P) fi = false;
        if (!fi) continue;
        FOR(j,3,k)
        {
            valx = (a[j] - a[j-1]) % P;
            valy = (a[j-1] - a[j-2]) % P;
            if (valx < 0) valx += P;
            if (valy < 0) valy += P;
            A = (valx * POW(valy,P-2,P)) % P;
            B = (a[j] - A * a[j-1]) %P;
            if (B < 0) B += P;
            bool ok = true;
//            cout << A << " " << B << " " << P << endl;
            FOR(t,2,k)
            if (a[t] != ((a[t-1] * A + B) % P)) ok = false;
            if (!ok) continue;
//            cout << A << " " << B << endl;
            resx[++cnt] = (A * a[k] + B) % P;
            break;
        }
    }
    if (cnt)
    {
        sort(resx+1,resx+cnt+1);
        cnt = unique(resx+1,resx+cnt+1) - resx - 1;
        if (cnt != 1) cout << "I don't know." << endl;
        else cout << resx[1] << endl;
    }
    else cout << "I don't know." << endl;
}
int main()
{
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    memset(Prime,true,sizeof(Prime));
    Prime[1] = false;
    FOR(i,2,1000000)
    if (Prime[i])
    {
        s[++top] = i;
        FOR(j,i,1000000/i) Prime[i*j] = false;
    }
    int ntest;
    cin >> ntest;
    FOR(test,1,ntest)
    {
        cout << "Case #" << test << ": ";
        cin >> d >> k;
        int val = 1;
        FOR(j,1,d) val *= 10;
        FOR(i,1,k) cin >> a[i];
        if (k == 1) cout << "I don't know." << endl;
        else solve(val);
    }
    
//    system("pause");
    return 0;
}
