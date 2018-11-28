#include<iostream>
#include<cstdio>
#include<cctype>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<deque>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<utility>
#include<sstream>
#include<cstring>
using namespace std;

typedef long long ll;
typedef unsigned int uint;

#define FOR(I,A,B) for(uint I=(A);I<=(B);I++)
#define REP(I,N) for(uint I=0;I<(N);I++)
#define VAR(V,I) typeof(I) V=(I)
#define FOREACH(I,C) for(VAR(I,(C).begin());I != (C).end(); I++)

#define ALL(X) (X).begin(),(X).end()
#define PB push_back
#define MP make_pair
#define FI first
#define SE second

#define INTPINF  2147483647
#define INTNINF  2147483648
#define UINTINF  4294967295U
#define LLPINF   9223372036854775807LL
#define LLNINF   9223372036854775808LL
#define ULLINF   18446744073709551615ULL
#define INF      6666

#define STATA    0
#define STATB    1

#define ARR      true
#define DEP      false

struct event {
    bool station;
    bool dir;
    uint time;
    
    bool operator<(const event& e) const {
        return time < e.time || (time == e.time && dir);
    }
};

int main() {
    queue<uint> q[2];
    uint        ttime;
    event       ev[400];
    
    uint h, m;
    uint na, nb;
    uint ts;
    scanf("%d", &ts);
    REP(t, ts) {
        uint trains[2];
        trains[0] = trains[1] = 0;
        while(!q[0].empty()) q[0].pop(); 
        while(!q[1].empty()) q[1].pop();
        
        scanf("%d", &ttime);
        scanf("%d %d", &na, &nb);
        REP(i, na) {
            scanf("%d:%d", &h, &m);
            ev[2*i].station   = STATA;
            ev[2*i].dir       = DEP;
            ev[2*i].time      = h*60 + m;
            scanf("%d:%d", &h, &m);
            ev[2*i+1].station   = STATB;
            ev[2*i+1].dir       = ARR;
            ev[2*i+1].time      = h*60 + m;
        }
        for (uint i = 0, j = na; i < nb; i++, j++) {
            scanf("%d:%d", &h, &m);
            ev[2*j].station   = STATB;
            ev[2*j].dir       = DEP;
            ev[2*j].time      = h*60 + m;
            scanf("%d:%d", &h, &m);
            ev[2*j+1].station   = STATA;
            ev[2*j+1].dir       = ARR;
            ev[2*j+1].time      = h*60 + m;
        }
        
        sort(ev, ev+2*(na+nb));
        
        REP(i, 2*(na+nb)) {
            if (ev[i].dir == ARR) {
                q[ev[i].station].push(ev[i].time + ttime);
            } else {
                if (q[ev[i].station].empty() || q[ev[i].station].front() > ev[i].time) {
                    trains[ev[i].station]++;
                } else {
                    q[ev[i].station].pop();
                }
            }
        }
        
        printf("Case #%d: %d %d\n", t+1, trains[0], trains[1]);
    }
    
    return 0;
}
