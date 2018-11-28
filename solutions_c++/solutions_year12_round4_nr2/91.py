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
    freopen("b_to.in","r",stdin);
    freopen("test.out","w",stdout);
}
#define maxn 1020
int n;
pair<double,double> res[maxn];
double r[maxn];
double W,L;
bool le(double x, double y) {
    return abs(x-y) > 1e-9 && x < y;
}
bool giao(int i, int j) {
    double Ax1 = res[i].first - r[i];
    double Ax2 = res[i].first + r[i];
    double Ay1 = res[i].second - r[i];
    double Ay2 = res[i].second + r[i];
    
    
    double Bx1 = res[j].first - r[j];
    double Bx2 = res[j].first + r[j];
    double By1 = res[j].second - r[j];
    double By2 = res[j].second + r[j];
    
    if (le(max(Ax1,Bx1),min(Ax2,Bx2)) && 
        le(max(Ay1,By1),min(Ay2,By2))) return true;
    return false;
}
int cs[maxn];
pair<double, double> res2[maxn];
double save_r[maxn];
void solve() {
    
    FR(i,n) cs[i] = i;
    FR(i,n) save_r[i] = r[i];
    for(int i = 0; i < n; i++)
    for(int j = i+1; j < n; j++) 
    if (r[i] > r[j]) {
        swap(r[i], r[j]);
        swap(cs[i], cs[j]);
    }
    res[0] = make_pair(0,0);
    double lastX = r[0];
    for(int i = 1; i <= n-1; i++) {
        if (lastX + r[i] > W) {
            lastX = -r[i];
        }
        res[i].first = lastX + r[i];
        res[i].second = 0;
        
        for(int j = 0; j < i; j++) 
        if (giao(i,j)) {
            res[i].second = max(res[i].second, res[j].second + r[j] + r[i]);
        }
//        printf(" %.3lf %.3lf",res[i].first,res[i].second);
        lastX = res[i].first + r[i];
    }
    FR(i,n) res2[cs[i]] = res[i];
    FR(i,n) res[i] = res2[i];
    FR(i,n) r[i] = save_r[i];
    
    FR(i,n) printf(" %.3lf %.3lf",res[i].first,res[i].second);
    cout << endl;
    bool ok = false;
    FR(i,n)
    FR(j,n) if (i != j) if (giao(i,j)) cout << "1NO" << i << " " << j << endl;
    FR(i,n) if (res[i].first > W || res[i].second > L) cout <<"2NO" << endl;
}
int main() {
    OPEN();
    int ntest;
    cin >> ntest;
    FOR(test,1,ntest) {
        cout << "Case #" << test << ":";
        cin >> n >> W >> L;
        FR(i,n) cin >> r[i];
        solve();
    }
    return 0;
}
