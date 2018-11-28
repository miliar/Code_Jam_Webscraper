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
map<string,char> Combine;
map<string,bool> Oppose;
int n;
string res;
string s;
void solve() {
    res.clear();
    FR(i,s.size()) {
        res.push_back(s[i]);
        while (res.size() >= 2) {
            string p = res.substr(res.size()-2,2);
            if (Combine.find(p) != Combine.end()) {
                res.erase(res.size()-2,2);
                res.push_back(Combine[p]);
            } else break;
        }
        bool stop = false;
        FR(j,res.size()) {
            FR(t,res.size()) {
                string p = "";
                p.push_back(res[j]);
                p.push_back(res[t]);
                if (Oppose[p]) {
                    stop = true;
                    break;
                }
            }
            if (stop) break;
        }
        if (stop) res.clear();
    }
    if (!res.size()) cout << "[]" << endl;
    else {
        cout << "[" << res[0];
        FOR(i,1,res.size()-1) cout << ", " << res[i];
        cout << "]" << endl;
    }
}
int main() {
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    int ntest;
    cin >> ntest;
    int m;
    FOR(test,1,ntest) {
        cout << "Case #" << test << ": ";
        cin >> m;
        Combine.clear();
        FR(i,m) {
            cin >> s;
            string p = s.substr(0,2);
            Combine[p] = s[2];
            reverse(p.begin(),p.end());
            Combine[p] = s[2];
        }
        cin >> m;
        Oppose.clear();
        string p;
        FR(i,m) {
            cin >> p;
            Oppose[p] = true;
            reverse(p.begin(),p.end());
            Oppose[p] = true;
        }
        cin >> n >> s;
        solve();
    }
    return 0;
}

