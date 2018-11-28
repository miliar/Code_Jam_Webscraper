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
int n,m;
char s[200][100];
char p[100];
int res = oo;
string kq;
bool dd[300];
bool ok[20000];
vector< string > list;
void visit(int x) {
    string t = string(s[x]);
    FOR(kt,'a','z') dd[kt] = false;
    list.resize(0);
    
    FOR(i,1,n)
    if (strlen(s[i]) == t.size()) list.push_back(string(s[i]));
    
    FR(i,list.size()) 
    FR(j,list[i].size()) dd[list[i][j]] = true;
    
    FR(i,list.size()) ok[i] = true;
    
    int dem = 0;
    FR(i,26) {
        char kt = p[i];
        if (!dd[kt]) continue;
        bool fail = false;
        FR(j,t.size()) {
            if (t[j] == kt) {
                fail = true;
                FR(k,list.size())
                if (ok[k] && list[k][j] != kt) 
                    ok[k] = false;
            } else {
                FR(k,list.size())
                if (ok[k] && list[k][j] == kt) ok[k] = false;
            }
        }
        if (!fail) dem++;
        FOR(kt,'a','z') dd[kt] = false;
        FR(j,list.size())
        if (ok[j])
        FR(k,list[j].size()) dd[list[j][k]] = true;
    }
    if (res < dem) {
        res = dem;
        kq = t;
    }
}
int main() {
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    int ntest;
    cin >> ntest;
    FOR(test,1,ntest) {
        cout << "Case #" << test << ": ";
        cin >> n >> m;
        gets(p);
        FOR(i,1,n) gets(s[i]);
        FOR(i,1,m) {
            gets(p);
            res = -1;
            FOR(j,1,n) visit(j);
            cout << kq;
            if (i != m) cout << " ";
        }
        cout << endl;
    }
    
//    system("pause");
    return 0;
}

