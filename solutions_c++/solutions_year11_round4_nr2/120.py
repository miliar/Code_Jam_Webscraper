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
#define fi(i,n) for(int (i) = 0, __end = (n); (i) < __end; i++)
#define ft(i,a,b) for(int (i) = (a), __end = (b); (i) <= __end; (i)++)
#define fd(i,a,b) for(int (i) = (a), __end = (b); (i) >= __end; (i)--)
#define fs(i,C) fi(i,SZ(C))
#define ALL(V) (V).begin(), (V).end()
#define SET(T, c) memset(T, c, sizeof(T))
#define VI vector<int>
#define PB push_back
#define PII pair<int, int>
#define SZ(C) ((int)(C).size())
#define SQR(a) ((a)*(a))
#define VII vector<PII>
#define SS stringstream

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

struct PLL {
    LL xMasf, yMassf, mass;
};

PLL _MEM[501][501];
PLL &mem(int i, int j) {
    return _MEM[i+1][j+1];
}

LL ms[500][500];

PLL MP(LL a, LL b, LL c) {
    PLL r;
    r.xMasf = a;
    r.yMassf = b;
    r.mass = c;
    return r;
}

PLL add(const PLL &a, const PLL &b) {
    return MP(a.xMasf + b.xMasf, a.yMassf + b.yMassf, a.mass + b.mass);
}

PLL sub(const PLL &a, const PLL &b) {
    return MP(a.xMasf - b.xMasf, a.yMassf - b.yMassf, a.mass - b.mass);
}

PLL msVec(int x, int y) {
    return MP(ms[y][x] * x, ms[y][x] * y, ms[y][x]);
}

void solve(int caseNo) {
    SET(_MEM, 0);

    int R=ri(), C=ri(), D=ri();
    char row[502];
    fi(y, R) {
        scanf(" %s", row);
        fi(x, C)
            ms[y][x] = D+row[x]-'0';
    }

    fi(y, R)
        fi(x, C)
            mem(x, y) = add(sub(add(mem(x-1, y), mem(x, y-1)), mem(x-1,y-1)), msVec(x, y));

    int maxL = -1;

    ft(y, 0, R-3) {
        ft(x, 0, C-3) {
            for(int l = 3; l + y <= R && l + x <= C; l++) {
                int ex = x + l - 1,
                    ey = y + l - 1;

                PLL mc = add(sub(sub(mem(ex, ey), mem(ex, y-1)), mem(x-1, ey)), mem(x-1,y-1));

                mc = sub(sub(sub(sub(mc, msVec(x, y)), msVec(x, ey)), msVec(ex, y)), msVec(ex, ey));

                mc.xMasf -= x * mc.mass;
                mc.yMassf -= y * mc.mass;

                ///if(x==1 && y == 0 && l == 3) {
                ///    printf("(%lld %lld %lld)\n", mc.xMasf, mc.yMassf, mc.mass);
                ///}

                mc.xMasf *= 2;
                mc.yMassf *= 2;

                if(mc.xMasf % mc.mass != 0 || mc.yMassf % mc.mass != 0)
                    continue;

                mc.xMasf /= mc.mass;
                mc.yMassf /= mc.mass;

                if(mc.xMasf == l-1 && mc.yMassf == l-1) {
                    if(maxL < l)
                        maxL = l;
                }
            }
        }
    }

    printf("Case #%d: ", caseNo);
    if(maxL == -1)
        puts("IMPOSSIBLE");
    else
        printf("%d\n", maxL);
}

int main(){
    fi(t,ri()) solve(t+1);
    return 0;
}

