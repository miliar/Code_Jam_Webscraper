//#pragma comment(linker, "/STACK:16777216")
#include <iostream>
#include <iomanip>
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
#define FOR(i,a,b) for(int i = (a); i <= (b); i++) 
#define DOWN(i,a,b) for(int i = (a); i >= (b); i--)
#define FORV(i,a) for(typeof(a.begin()) i = a.begin(); i != a.end(); i++)
#define FR(i,a) for(int i = 0; i < (a); i++)
#define DR(i,a) for(int i = (a)-1; i >= 0; i--)
#define REP(i,a) for(int i = 0; i < (a); i++)
#define Rep(i,a) for(int i = 0; i < (a); i++)
#define For(i,a,b) for(int i = (a); i <= (b); i++)

#define sqr(x) ((x)*(x))
#define dout debug && cout 
#define ll long long
#define sz size()
#define ull unsigned long long
#define pb push_back
#define oo 1000000009
/* DEBUGGING */
bool debug = false;
/* MAIN PROGRAM */

using namespace std;

/*************************TEMPLATE**********************************/
long long convertToNum(string s)
{
    long long val = 0; FR(i,s.size()) val = val * 10 + s[i] - '0';
    return val;
}
string convertToString(long long a) {
    string res = ""; if (!a) return "0";
    while (a) { res = (char)(a % 10 + 48) + res;  a /= 10; }
    return res;
}
long long GCD(long long x,long long y)  {
    if (!x) return y; if (!y) return x;
    if (x == y) return x; if (x < y) return GCD(x,y%x); else return GCD(x%y,y);
}
long long POW(long long x,long long y,long long Base){
    if (!y) return 1; long long u = POW(x,y/2,Base);
    u = (u * u) % Base;
    if (y & 1) return (u * x) % Base; else return u;
}

//newstate = (newstate-1) & oldstate
/**************************CODE HERE*****************************/
#define maxn 1010

struct pt {
    int len, speed;
};
bool cmp(pt A, pt B) {
    return A.speed < B.speed;
}
int n;
double R,S,T,L;
pt p[maxn];

void solve() {
    sort(p+1,p+n+2,cmp);
    double res = 0;
    FOR(i,1,n+1) {
        double speed = p[i].speed;
        double delta = p[i].len / (speed + R);
        if (delta < T) {
            T -= delta;
            res += delta;
        } else {
            res += T;
            double len = p[i].len - T * (speed + R);
            
            T = 0;
            res += len / (speed + S);
        }
    }
    printf("%.7lf\n",res);
}
int main() {
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    int ntest = 0;
    cin >> ntest;
    FOR(test,1,ntest) {
        cout << "Case #" << test << ": ";
        cin >> L >> S >> R >> T >> n;
        int u,v;
        int sum = 0;
        FOR(i,1,n) {
            cin >> u >> v >> p[i].speed;
            p[i].len = v - u;
            sum += v - u;
        }
        p[n+1].len = L - sum;
        p[n+1].speed = 0;
        solve();
    }
    return 0;
}

