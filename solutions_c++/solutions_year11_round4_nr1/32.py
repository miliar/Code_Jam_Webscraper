#include<algorithm>
#include<cassert>
#include<complex>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<sstream>
#include<stack>
#include<string>
#include<vector>
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define REP(i,n) for(int i=0;i<(n);++i)
#define fup FOR
#define fdo FORD
#define VAR(v,i) __typeof(i) v=(i)
#define FORE(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define ALL(x) (x).begin(),(x).end()
#define SIZE(x) ((int)(x).size())
#define siz SIZE
#define CLR memset((x),0,sizeof (x))
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
#define SQR(a) ((a)*(a))

#define DEBUG 1
#define debug(x) {if(DEBUG) cerr << #x << " = " << x << endl;}
#define debugv(x) {if(DEBUG) {cerr << #x << " = "; FORE(it,(x)) cerr << *it << " . "; cerr  <<endl;}}

using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef VI vi;
typedef LL lli;

const int inf = 1000000000;

struct wlk{
    int b,e, v;
    bool operator < (const wlk & a) const {
        return v < a.v;
    }
    int l(){
        return e-b;
    }
};

void solve(int tcase) {
    printf("Case #%d: ", tcase);
    int x, s, r, t, n;
    scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
    int rem = x;
    vector<wlk> V;
    REP(i, n) {
        wlk cur;
        scanf("%d%d%d", &cur.b, &cur.e, &cur.v);
        rem -= (cur.e - cur.b);
        V.PB(cur);
    }
    wlk rest;
    rest.b = 0;
    rest.e = rem;
    rest.v = 0;
    V.PB(rest);
    sort(ALL(V));
    double T = t;
    double res = 0;
    FORE(it, V) {
       
        if (T > 0) {
            double curt = (double) (it->l())/(it->v + r);
            if (curt <= T) {
                T -= curt;
                res += curt;
            } else {
                res += T;
                double len = T*(it->v + r);
                T = 0;
                //debug(len);
                res += (double) (it->l() - len)/ (it->v + s);
            }
        } else {
            res += (double) (it->l())/(it->v + s);
        }
        //printf("after %d v %d: %lf\n",it->l(), it->v, res); 
    }
    printf("%.9lf\n", res);



}

int main() {
    int t;
    scanf("%d", &t);
    REP(i, t) solve(i+1);
    return 0;
}
