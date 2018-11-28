#include <string>
#include <cstring>
#include <vector>
#include <cmath> 
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
 
using namespace std;
 
#define REP(a,n) for(int a=0; a<(n); ++a)
#define FOR(a,b,c) for(int a=(b); a<=(c); ++a)
#define INIT(a, v) __typeof(v) a = (v)
#define FOREACH(a, v) for (INIT(a, (v).begin()); a!=(v).end(); ++a)
 
template<class T>
inline int size(const T&t){return t.size();}
 
typedef vector<string> vs;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long LL;

#define INF 1000000000
#define PB push_back
#define MP make_pair
 
//////////////////////////////////////////

int N;
vi sas[400];
int dist[400];
vi pop[400];
vi w_odl[400];
int ile_wsp[400][400];
int wyn[400][400];
set<int> zbior[400];

int res;

void BFS() {
    REP(a, N)
        dist[a] = -INF;
    dist[0] = 0;
    w_odl[0].PB(0);
    queue<int> Q;
    Q.push(0);
    while (!Q.empty()) {
        int x = Q.front(); 
        Q.pop();
        FOREACH(it, sas[x]) {
            int y = *it;
            if (dist[y]<0) {
                dist[y] = dist[x]+1;
                Q.push(y);
                w_odl[dist[y]].PB(y);
            }
        }
    }
    REP(x, N)
        FOREACH(it, sas[x]) {
            int y = *it;
            if (dist[y]==dist[x]-1)
                pop[x].PB(y);
        }
/*    FOR(d, 0, odl[1]-2)
        FOREACH(it, w_odl[d]) {
            int x = *it;
            set<int> nn;
            FEPEACH(it2, sas[x])
                nn.insert(*it2);
            FOREACH(it2, w_odl[d+2]) {
                int y = *it2;
                ile_wsp[x][y] = 0;
                FOREACH(it3, pop[y])
                    if (nn.find(*it3)!=nn.end())
                        ++ile_wsp[x][y];
            }*/
    REP(a, N)
        FOREACH(it, sas[a])
            zbior[a].insert(*it);
        
}


void zbior_dla_pary(int x, int y, set<int> &zb) {
    FOREACH(it2, sas[x])
        if (*it2!=y)
            zb.insert(*it2);
    FOREACH(it2, sas[y])
        if (*it2!=x)
            zb.insert(*it2);
}

int licz() {
    if (dist[1]==1)
        return size(sas[0]);
    FOREACH(it, w_odl[1]) {
    set<int> zbzb;
        zbior_dla_pary(0, *it, zbzb);
        wyn[0][*it] = size(zbzb);//zbior[0])+size(zbior[*it])-2;
    }
    FOR(d, 0, dist[1]-2)
        FOREACH(it2, w_odl[d+2])	
            FOREACH(it1, pop[*it2]) {
//                zbior_dla_pary(*it1, *it2, zbior[*it1][*it2]);
                wyn[*it1][*it2] = -INF;
                FOREACH(it0, pop[*it1]) {
                    int moj_wyn = wyn[*it0][*it1]-1;
                    FOREACH(s, sas[*it2])
                        if (zbior[*it0].find(*s)==zbior[*it0].end() && zbior[*it1].find(*s)==zbior[*it1].end())
                            ++moj_wyn;
                    wyn[*it1][*it2] = max(moj_wyn, wyn[*it1][*it2]);
                }
            }
    int glob = 0;
    FOREACH(it2, pop[1])
        FOREACH(it1, pop[*it2])
            glob = max(glob, wyn[*it1][*it2]);
    return glob;
}

int main() {
    int TT;
    scanf("%d", &TT);
    REP(tt, TT) {
        int ilek;
        scanf("%d%d", &N, &ilek);
        REP(a, ilek) {
        int x,y;
            scanf("%d,%d", &x, &y);
            sas[x].PB(y);
            sas[y].PB(x);
        }
        BFS();
        printf("Case #%d: %d %d\n", (tt+1), dist[1]-1, licz());
        REP(a, N) {
            sas[a].clear();
            pop[a].clear();
            w_odl[a].clear();
            zbior[a].clear();
        }
//        REP(a, N) REP(b, N)
  //          zbior[a][b].clear();
    }
}


