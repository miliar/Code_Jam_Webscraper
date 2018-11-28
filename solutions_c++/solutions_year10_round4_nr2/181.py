/* All includes and defines required by the templates
 * Just add it at the beginning and all will work OOB */
#include<iostream>
#include<set>
#include<iomanip>
#include<sstream>
#include<fstream>
#include<stack>
#include<cstdio>
#include<cmath>
#include<cassert>
#include<queue>
#include<vector>
#include<list>
#include<algorithm>
#include<map>
#include<cstring>
#include<cctype>


using namespace std;
#define fe(e,C) for(__typeof((C).begin()) e = (C).begin(); e != (C).end(); e++)
#define fi(i,n) for(int i = 0, i##end = (n); i < i##end; i++)
#define ft(i,a,b) for(int i = (a), i##end = (b); i <= i##end; i++)
#define fd(i,a,b) for(int i = (a), i##end = (b); i >= i##end; i--)
#define fs(i,C) fi(i,SZ(C))
#define ALL(V) (V).begin(), (V).end()
#define SET(T, c) memset(T, c, sizeof(T))
#define VI vector<int>
#define PB push_back
#define PII pair<int, int>
#define SEC second
#define FST first
#define MP make_pair
#define SZ(C) ((int)(C).size())
#define SQR(a) ((a)*(a))
#define VII vector<PII>

typedef unsigned long long ULL;
typedef long long LL;

int ri() { int n; scanf(" %d", &n); return n; }
void pi(int n) { printf("%d\n", n); }
string rs() { char buf[10000]; buf[9999]=-1; scanf(" %s ", buf); assert(buf[9999]==-1); return buf; }
void ps(const string &s) { printf("%s\n", s.c_str()); }
template<class R, class T>
R conv(const T &t) { stringstream ss; ss << t; R r; ss >> r; return r; }
LL gcd(LL a, LL b) { if(b == 0) return a; else return gcd(b, a % b); }
struct pt { int x, y; pt(int x, int y):x(x), y(y) {} };

vector<int> cst;
int p;
LL mem[1<<12][11];

const LL INF = (LL)1e15;

LL getMinCost(int r, int missedGames, int depth) {
    if(mem[r][missedGames] != -3141592)
        return mem[r][missedGames];

    if(depth == p) {
        if(missedGames > cst[r])
            return INF;
        else
            return 0;
    }
    else {
        // watch
        LL best = 
               getMinCost(2*r, missedGames, depth+1) +
               getMinCost(2*r+1, missedGames, depth+1) +
               cst[r];
        // miss
        LL oth = getMinCost(2*r, missedGames+1, depth+1)+
                 getMinCost(2*r+1, missedGames+1, depth+1);

        return mem[r][missedGames] = min(best, oth);
    }
}

void solve(int t) {
    p = ri();
    cst.clear();
    fi(i, (1<<(p+1))-1)
        cst.PB(ri());
    reverse(ALL(cst));
    cst.insert(cst.begin(), 0);

    fs(i, cst)
        fi(j,11)
            mem[i][j]=-3141592;

    printf("Case #%d: %lld\n", t, getMinCost(1, 0, 0));
}

int main(){
    fi(t,ri()) solve(t+1);
    return 0;
}

