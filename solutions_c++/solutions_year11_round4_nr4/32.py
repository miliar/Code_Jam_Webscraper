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

struct vertex{
    vertex(): d(inf), out() {}
    int d;
    vector<int> out;
    vector<int> fwd;
    vector<int> bck;
    vector<int> st;

};

vector<vertex> G;
int dyn[500][500];
int sgn[500];
void solve(int tcase) {
    printf("Case #%d: ", tcase);
    int n,m;
    G.clear();
    scanf("%d%d", &n, &m);
    G = vector<vertex>(n);
    REP(i, m) {
        int a,b;
        scanf("%d,%d", &a, &b);
        G[a].out.PB(b);
        G[b].out.PB(a);
    }
    queue<int> Q;
    vector<int> ord;
    Q.push(0);
    ord.PB(0);
    G[0].d = 0;
    REP(i, n) sgn[i]=0;
    while(!Q.empty()) {
        int f = Q.front();
        Q.pop();
        FORE(it, G[f].out) {
            if (G[*it].d == inf) {
                G[*it].d = G[f].d+1;
                Q.push(*it);
                ord.PB(*it);
            }
        }
    }
    REP(i, n) {
        int d = G[i].d;
        FORE(it, G[i].out) {
            if (G[*it].d == d) G[i].st.PB(*it);
            if (G[*it].d < d) G[i].bck.PB(*it);
            if (G[*it].d > d) G[i].fwd.PB(*it);
        }
    }
    if (G[1].d == 1) {
        printf("0 %d\n",SIZE(G[0].fwd));
        return;
    }
    REP(i, n) REP(j, n) dyn[i][j] = -1;
    int s = 1;
    FORE(it, G[0].fwd) dyn[*it][0] = 0;
    FORE(ot, ord) {
        int cur = *ot;
        if (G[cur].d < 2) continue;
        if (G[cur].d > G[1].d) break;
        FORE(it, G[cur].bck) {
            if (G[*it].d == G[cur].d - 1) {
                int prev = *it;
                FORE(jt, G[prev].bck) {
                    int res = dyn[prev][*jt];
                 //   printf("%d -> %d -> %d: %d", *jt, prev, cur, res);
                    sgn[prev]=s;
                    FORE(t, G[*jt].fwd) {
                        if (sgn[*t] != s) ++res;
                        sgn[*t]=s;
                    }
                    FORE(t, G[prev].st) {
                        if (sgn[*t] != s) ++res;
                        sgn[*t]=s;
                    }
                    FORE(t, G[cur].bck) {
                        if (sgn[*t] != s) ++res;
                        sgn[*t]=s;
                    }
                    ++s;
                   // printf(": %d\n", res);
                    dyn[cur][prev] = max(dyn[cur][prev], res);
                }

            }
        }
    }
    int rs = -1;
    FORE(it, G[1].bck) {
        int prev = *it;
        FORE(jt,G[prev].bck) {
            int res = dyn[prev][*jt];
            sgn[prev]=s;
            FORE(t, G[*jt].fwd) {
                if (sgn[*t] != s) ++res;
                sgn[*t]=s;
            }
            FORE(t, G[prev].st) {
                if (sgn[*t] != s) ++res;
                sgn[*t]=s;
            }
            res += SIZE(G[prev].fwd);
            ++s;
            rs = max(rs, res);
        }
    }
    printf("%d %d\n", G[1].d-1, rs);


}

int main() {
    int t;
    scanf("%d", &t);
    REP(i, t) solve(i+1);
    return 0;
}
