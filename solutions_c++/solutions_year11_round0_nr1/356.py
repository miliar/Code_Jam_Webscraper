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
vector< pair<bool,int> > list;
int n;
void solve() {
    int now1 = 1, now2 = 1, time1 = 0, time2 = 0;
    int res = 0;
    FR(i,list.size()) {
        if (list[i].first) {
            int dist = abs(now1 - list[i].second);
            int availTime = max(0,time2 - time1);
            int need = max(0,dist - availTime) + 1;
            
            now1 = list[i].second;
            res += need;
            time1 = max(time1,time2) + need;
        } else {
            int dist = abs(now2 - list[i].second);
            int availTime = max(0,time1 - time2);
            int need = max(0,dist - availTime) + 1;
            
            now2 = list[i].second;
            res += need;
            time2 = max(time1,time2) + need;
        }
    }
    cout << res << endl;
}
int T;
int main() {
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    cin >> T;
    FOR(t,1,T) {
        cout << "Case #" << t << ": ";
        cin >> n;
        list.clear();
        char type;
        int x;
        FR(i,n) {
            cin >> type >> x;
            list.push_back( make_pair(type == 'O' ? true:false, x) );
        }
        solve();
    }
    return 0;
}

