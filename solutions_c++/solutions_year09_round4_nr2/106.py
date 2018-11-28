#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <set>

#define REP(i, n) for ( int i = 0; i < (n); i++ ) 
#define FOR(i, a, b) for ( int i = (a); i < (b); i++ ) 

using namespace std;

const int MAX_R = 10;
const int MAX_C = 6;

int r, c, f;
vector<char> data[MAX_R+1];

struct el {
    int pos;
    int cost;
    vector<char> cur;
    vector<char> next;

    el(int a, int z, vector<char> b, vector<char> c) : pos(a), cost(z), cur(b), next(c) {}

    bool operator<(const el& x) const {
        if ( cost != x.cost ) return cost < x.cost;
        if ( pos != x.pos ) return pos < x.pos;
        if ( cur != x.cur ) return cur < x.cur;
        return next < x.next;
    }
};

struct ee {
    int pos;
    vector<char> cur;
    vector<char> next;

    ee(el a) {
        cur = a.cur;
        next = a.next;
        pos = a.pos;
    }

    bool operator<(const ee& x) const {
        if ( pos != x.pos ) return pos < x.pos;
        if ( cur != x.cur ) return cur < x.cur;
        return next < x.next;
    }
};

void fun(int cs) {
    scanf("%d %d %d", &r, &c, &f);
    REP(i, r+1) data[i].clear();
    REP(i, r+1) data[i].resize(c, '#');
    REP(i, r) REP(j, c) scanf(" %c", &data[i][j]);

    set<el> Q[MAX_R];
    Q[0].insert( el(0, 0, data[0], data[1]) );

    REP(poziom, r-1) {
        set<ee> used;

        while ( Q[poziom].size() > 0 ) {
            el A = *(Q[poziom].begin());
            Q[poziom].erase(Q[poziom].begin());
            
            if ( used.find(ee(A)) != used.end() ) continue;
            used.insert(ee(A));
            
            if ( A.pos > 0 and A.cur[A.pos-1] == '.' ) {
                int npos = A.pos-1;
                if ( A.next[npos] == '#' ) {
                    el B(npos, A.cost, A.cur, A.next);
//                    if ( used.find(ee(B)) == used.end() ) {
                    Q[poziom].insert(B);
//                        used.insert(ee(B));
//                    }
                } else {
                    // spadam
                    int dl = 1;
                    while ( true ) {
                        if ( data[poziom+dl+1][npos] == '.' ) dl++;
                        else break;
                    }
                    
                    if ( dl <= f ) { // FIXME: dobrze?
                        int nr = poziom + dl;
                        if ( dl == 1 ) {
                            Q[poziom+dl].insert( el(npos, A.cost, A.next, data[nr+1]) );
                        } else {
                            Q[poziom+dl].insert( el(npos, A.cost, data[nr], data[nr+1]) );
                        }
                    }
                }

                if ( A.next[npos] == '#' ) {
                    vector<char> tt = A.next;
                    tt[npos] = '.';
                    el C(A.pos, A.cost+1, A.cur, tt);
                    Q[poziom].insert(C);
                }
            }

            if ( A.pos+1 < c and A.cur[A.pos+1] == '.' ) {
                int npos = A.pos+1;
                if ( A.next[npos] == '#' ) {
                    el B(npos, A.cost, A.cur, A.next);
//                    if ( used.find(ee(B)) == used.end() ) {
                    Q[poziom].insert(B);
//                        used.insert(ee(B));
//                    }
                } else {
                    // spadam
                    int dl = 1;
                    while ( true ) {
                        if ( data[poziom+dl+1][npos] == '.' ) dl++;
                        else break;
                    }
                    
                    if ( dl <= f ) { // FIXME: dobrze?
                        int nr = poziom + dl;
                        if ( dl == 1 ) {
                            Q[poziom+dl].insert( el(npos, A.cost, A.next, data[nr+1]) );
                        } else {
                            Q[poziom+dl].insert( el(npos, A.cost, data[nr], data[nr+1]) );
                        }
                    }
                }

                if ( A.next[npos] == '#' ) {
                    vector<char> tt = A.next;
                    tt[npos] = '.';
                    el C(A.pos, A.cost+1, A.cur, tt);
                    Q[poziom].insert(C);
                }
            }
        }
    }

    printf("Case #%d: ", cs);
    if ( Q[r-1].size() == 0 ) {
        printf("No\n");
    } else {
        printf("Yes %d\n", (*Q[r-1].begin()).cost);
    }
}

int main() {
    int T;
    scanf("%d", &T);
    REP(i, T) fun(i+1);

    return 0;
}
