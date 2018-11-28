#define _CRT_SECURE_NO_DEPRECATE
#pragma warning(disable:4530)
#include <string>
#include <vector>
#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <sstream>
#include <set>
#include <cmath>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(it,x) for(typeof((x).begin())it=(x).begin();it!=(x).end();++it)
#define all(x) (x).begin(),(x).end()
#define CLR(x,v) memset(x,v,sizeof(x))
#define pb push_back
#define sz size()
#define exist(c,x) ((c).find(x)!=(c).end())
#define cexist(c,x) (find(all(c),x)!=(c).end())


struct people {
    bool satisfied;
    int want_malted; // -1 if none
    set<int> want_unmalted;
};

people p[10000];
int flavor_malted[10000];
vector<int> backlink[10000];

int N, M;

int eval() {
    set<int> unsatisfied;
    REP(i, N) {
        flavor_malted[i] = 2; // undecided
    }
    REP(i, M) {
        if (p[i].want_unmalted.empty()) {
            unsatisfied.insert(i);
        }
    }
    while (!unsatisfied.empty()) {
        int who = *(unsatisfied.begin());
        unsatisfied.erase(who);
        int flav = p[who].want_malted;
        if (flav == -1) return -1;
        if (flavor_malted[flav] == 1) continue;
        flavor_malted[flav] = 1;
        FORE(it, backlink[flav]) {
            p[*it].want_unmalted.erase(flav);
            if (p[*it].want_unmalted.empty()) {
                unsatisfied.insert(*it);
            }
        }
    }
}

int main(int argc, char *argv[]) {
    freopen(argv[1], "rt", stdin);
    int Tests;
    cin >>Tests;
    FOR(test, 1, Tests+1) {
        printf("Case #%d:", test);
        cin >> N >>M;

        CLR(flavor_malted, 0);
        REP(i, N) {
            backlink[i].clear();
        }

        REP(i, M) {
            int T;
            cin >>T;
            p[i].satisfied = false;
            p[i].want_malted = -1;
            p[i].want_unmalted.clear();
            REP(j, T) {
                int flavor;
                int malted;
                cin >> flavor >>malted;
                flavor--;
                if (malted) {
                    p[i].want_malted = flavor;
                }
                else {
                    p[i].want_unmalted.insert(flavor);
                    backlink[flavor].pb(i);
                }
            }
        }

        int result = eval();
        if (result == -1) 
            printf(" IMPOSSIBLE\n");
        else {
            REP(i, N) {
                if (flavor_malted[i] == 1) {
                    printf( " %d", 1);
                }
                else
                    printf( " %d", 0);
            }
            printf("\n");
        }
    }
    return 0;
}
