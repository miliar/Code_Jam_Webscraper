//#pragma comment(linker, "/STACK:16777216")
#include <iostream>
#include <cstdio>
#include <cmath>
#include <set>
#include <vector>
#include <map>
#include <cstring>
#include <sstream>
#include <algorithm>
#include <string>
#include <queue>
#include <fstream>

#define FOR(i,a,b) for(int i = (a); i <= (b); i++)
#define FR(i,a) for(int i = 0; i < (a); i++)
#define DR(i,a) for(int i = (a)-1; i >=0; i--)
#define DOWN(i,a,b) for(int i = (a); i >= (b); i--)
#define FORD(i,a,b) for(int i = (a), _b = (b); i >= _b; i--)
#define REPD(i,n) for(int i = (n) - 1; i >= 0; i--)
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define RESET(c,x) memset(c,x,sizeof(c))
#define SIZE(c) (c).size()
#define ALL(c) (c).begin(), (c).end()

#define REP(i,a) for(int i = 0; i < (a); i++)

#define sqr(x) ((x)*(x))

using namespace std;
/*************************TEMPLATE**********************************/
long long convertToNum(string s)
{
    long long val = 0; FR(i,s.size()) val = val * 10 + s[i] - '0';
    return val;
}
char bu[50];
string convertToString(int a) {
    sprintf(bu,"%d",a);
    return string(bu);
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

void OPEN() {
    freopen("c11.in","r",stdin);
    freopen("test.out","w",stdout);
}
#define maxn 2500
int n;
int x[maxn];
int res[maxn];
void solve() {
    bool ok = false;
    FR(i,n) res[i] = 50000000;
    FR(iter2,10000) {
        FR(iter,80) {
            bool tm = true;
            FR(i,n-1) {
                //i --> x[i]
                FOR(k,1,x[i]-i-1) {
                    int X = i+k;
                    int now = res[X];
                    double delta = res[i] + (double)k / (x[i]-i) * (res[x[i]] - res[i]);
                    if (abs(delta - ((int)delta)) < 1e-6) {
                        int require_height = (int)delta - 1;
                        if (res[X] > require_height) {
                            tm = false;
    //                        cout << X << " " << require_height << " " << k << endl;
                            res[X] = require_height;
                        }
                    } else {
                        int require_height = (int)delta;
                        if (res[X] > require_height) {
                            tm = false;
                            res[X] = require_height;
                        }
                    }
                }
                if (!tm) break;
                FOR(k,x[i]+1,n-1) {
                    int now = res[k];
                    double delta = res[i] + (double)(k-i) / (x[i] - i) * (res[x[i]] - res[i]);
                    int require_height = (int)delta;
                    if (res[k] > require_height) {
                        tm = false;
                        res[k] = require_height;
                    }
                }
                if (!tm) break;
            }
            bool stop = false;
            FR(i,n) if (res[i] < 0) {
                stop = true;
                break;
            } 
            if (stop) break;
            if (tm) {
                ok = true;
                break;
            }
        }
        if (ok) break;
        FR(i,n) res[i] = rand() % 1000000000;
    }
    if (!ok) cout << " Impossible" << endl;
    else {
        FR(i,n) cout << " " << res[i];
        cout << endl;
    }
}
int main() {
    OPEN();
    int ntest;
    cin >> ntest;
    FOR(test,1,ntest) {
        cout << "Case #" << test << ":";
        cin >> n;
        FR(i,n-1) cin >> x[i];
        FR(i,n-1) x[i]--;
        solve();
    }
    return 0;
}
