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

int t, na, nb;

int getczas(void){
    char txt[1000];
    scanf("%s", txt);
    txt[2] = 0; txt[5] = 0;
    int a, b;
    sscanf(txt, "%d", &a);
    sscanf(txt+3, "%d", &b);
    return a * 60 + b;
}

VPII va, vb;

int main(){
    int te;
    scanf("%d", &te);
    for (int tt = 1; tt <= te; ++tt){
        scanf("%d %d %d", &t, &na, &nb);
        va.clear(); vb.clear();
        REP(i, na){
            int x = getczas();
            int y = getczas();
            va.PB(MP(x, 1));
            vb.PB(MP(y + t, -1));
        }
        REP(i, nb){
            int x = getczas();
            int y = getczas();
            vb.PB(MP(x, 1));
            va.PB(MP(y + t, -1));
        }
        sort(ALL(va));
        sort(ALL(vb));
        int ia = 0 , ib = 0;
        int wa = 0, wb = 0;
        FOREACH(it, va)
            if (it->ND == -1)
                ia++;
            else if (ia > 0)
                ia--;
            else
                wa++;
        FOREACH(it, vb)
            if (it->ND == -1)
                ib++;
            else if (ib > 0)
                ib--;
            else
                wb++;
        printf("Case #%d: %d %d\n", tt, wa, wb);
    }
    return 0;
}
