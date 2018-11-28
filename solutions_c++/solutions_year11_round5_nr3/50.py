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
const int m = 1000003;

struct vertex{
    vertex(): d(0), out(), ok(true) {}
    int d;
    vector<int> out;
    bool ok;
};

vector<vertex> L;
vector<vertex> R;
int n;
int r,c;
int num(int x, int y) {
    return c*((x+r)%r)+(y+c)%c;
}

bool solve(int tcase) {
    printf("Case #%d: ", tcase);

    scanf("%d%d", &r, &c);
    n = r*c;
    L = vector<vertex>(n);
    R = vector<vertex>(n);
    char ch = getchar();
    REP(i, r) {
        while( ch != '-' && ch != '/' && ch!='\\' && ch != '|') ch = getchar();
        REP(j, c) {
            if (ch == '-') {
                L[num(i,j)].out.PB(num(i,j+1));
                L[num(i,j)].out.PB(num(i,j-1));
            } else if (ch == '|') {
                L[num(i,j)].out.PB(num(i-1,j));
                L[num(i,j)].out.PB(num(i+1,j));
            } else if (ch == '\\') {
                L[num(i,j)].out.PB(num(i-1,j-1));
                L[num(i,j)].out.PB(num(i+1,j+1));
            } else if (ch == '/') {
                L[num(i,j)].out.PB(num(i-1,j+1));
                L[num(i,j)].out.PB(num(i+1,j-1));
            } else assert(false);
            ch = getchar();
        }
    }
    REP(i, n) {
        FORE(it, L[i].out) {
            R[*it].out.PB(i);
        }
    }
    queue<int> Q;
    REP(i, n) {
        R[i].d = SIZE(R[i].out);
        if (R[i].d == 0) return false;
        else if (R[i].d == 1) Q.push(i);
    }
    while(!Q.empty()) {
        int r = Q.front();
        Q.pop();
        int l = -1;
        FORE(it, R[r].out) {
            if (L[*it].ok) l = *it;
        }
        assert(l>=0);
        L[l].ok = false;
        R[r].ok = false;
        FORE(it, L[l].out) {
            if (*it != r) {
                --R[*it].d;
                if (R[*it].d == 0) return false;
                else if (R[*it].d == 1) Q.push(*it);
            }
        }
    }
    int res = 1;
    REP(i, n) {
        if (L[i].ok) {
            res = (res*2)%m;
            int r = L[i].out[0];
            int l = i;
            while(true) {
                L[l].ok = false;
                R[r].ok = false;
                l = -1;
                FORE(it, R[r].out) {
                    if (L[*it].ok) l = *it;
                }
                if (l == -1) break;
                FORE(it, L[l].out) {
                    if (R[*it].ok) r = *it;
                }
            }
        }
    }
    printf("%d\n", res);
    return true;


}

int main() {
    int t;
    scanf("%d", &t);
    REP(i, t) {
        if (!solve(i+1)) {
            printf("0\n");
        }
    }
    return 0;
}
