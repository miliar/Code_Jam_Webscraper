#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <numeric>
#include <cmath>
using namespace std;

typedef vector <int > VI;
typedef vector < VI > VVI;
typedef long long LL;
typedef vector < LL > VLL;
typedef vector < double > VD;
typedef vector < string > VS;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef istringstream ISS;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for (int i=0; i<(n); ++i)
#define FOR(var,pocz,koniec) for (int var=(pocz); var<=(koniec); ++var)
#define FORD(var,pocz,koniec) for (int var=(pocz); var>=(koniec); --var)
#define FOREACH(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define SIZE(x) (int)x.size()

typedef long double LD;
struct POINT{
    LD x, y;
    POINT(){}
    POINT(LD wx, LD wy) : x(wx), y(wy) {}
};

const LD EPS = 1E-10;
inline bool iszero(LD x) { return x >= -EPS && x <= EPS; }
LD pi;

LD czapa(LD r, LD x){
    if (x >= r) return (LD)0;
    if (x < (LD)0)
        return pi * r * r - czapa(r, -x);
    LD k = acosl(x / r);
    LD y = sqrtl(r * r - x * x);
    return k * r * r - y * x;
}

LD dziob(LD r, LD x, LD y){
    if (x < (LD)0){
        return pi * r * r - czapa(r, -y) - dziob(r, -x, y);
    }
    if (y < (LD)0){
        return pi * r * r - czapa(r, -x) - dziob(r, x, -y);
    }
    if (x * x + y * y >= r * r - EPS)
        return (LD)0;
    return ((LD)2 * czapa(r, x) + (LD)2 * czapa(r, y) + (LD)4 * x * y - pi * r * r) / (LD)4;
}

inline LD ciecie(LD r, LD x, LD y, LD d){
    return dziob(r, x, y) + dziob(r, x+d, y+d) - dziob(r, x+d, y) - dziob(r, x, y+d);
}

LD f, R, t, r, g;
int main(){
    int te;
    pi = (LD)4 * atanl((LD)1);
    scanf("%d", &te);
    FOR(tt, 1, te){
        printf("Case #%d: ", tt);
        fprintf(stderr, "Case %d....\n", tt);
        scanf("%Lf%Lf%Lf%Lf%Lf", &f, &R, &t, &r, &g);
        LD akum = (LD)0;
        LD bok = g - f - f;
        if (bok > (LD)0){
            LD krok = g + r + r;
            int ile = (int)floorl(R / krok) + 4;
            FOR(i, -ile, ile)
                FOR(j, -ile, ile)
                    akum += ciecie(R-t-f, krok * i + r + f, krok * j + r + f, bok);
        }
        LD pole = pi * R * R;
        printf("%.09Lf\n", (pole - akum) / pole);
        fprintf(stderr, "done\n");
    }
    return 0;
}
