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
#define SMIN(a, b) a = min((a),(b))
#define SMAX(a, b) a = max((a),(b))

typedef long long ll;

typedef pair<int,int> pt; // x, y

vector<pt> walks;
ll orig_area;

int d[4][2] = {
    {0, -1},
    {1, 0},
    {0, 1},
    {-1, 0}
};

ll width(pair<int, int> p) {
    return p.second - p.first;
}

void eval() {
    int x, y;
    pt here = make_pair(0, 0);
    int dir = 0;
    walks.clear();
    orig_area = 0ll;

    int L;
    cin >> L;

    REP(i, L) {
        string inst;
        int rep;
        cin >> inst >> rep;
        REP(reps, rep) {
            REP(j, inst.sz) {
                switch(inst[j]) {
                    case 'F':   {
                        pt next;
                        next.first = here.first + d[dir][0];
                        next.second = here.second + d[dir][1];
                        orig_area = orig_area 
                            + (next.second + here.second) * 
                              (next.first - here.first) / 2;
                        walks.pb(next);
                        here = next;
                        break;
                    }
                    case 'L':
                        dir = (dir + 3) % 4;
                        break;
                    case 'R':
                        dir = (dir + 1) % 4;
                        break;
                        
                }
            }
        }
    }
    if (orig_area < 0) orig_area = -orig_area;
    //cout << orig_area << endl;

    vector< pair<int, pair<int, int> > > left_block;
    vector< pair<int, pair<int, int> > > right_block;


    //
    //  left convey 
    //

    {
        sort(walks.begin(), walks.end());
        bool first = true;
        int x = 0;
        int ylow=0, yhigh=0;

        long long lcarea = 0;

        FORE(it, walks) {
            if (first) {
                x = it->first;
                ylow = it->second;
                yhigh = it->second;
                first = false;
            }
            else {
                int lx = x;
                int bylow = ylow;
                int byhigh = yhigh;
                x = it->first;
                SMIN(ylow, it->second);
                SMAX(yhigh, it->second);
                if (lx != x) {
                    left_block.pb( make_pair( lx, make_pair(bylow, byhigh) ) );
                }
            }
        }
        left_block.pb(make_pair(x, make_pair(ylow, yhigh)));
    }

    //
    //  right convey 
    //
    {
        sort(walks.rbegin(), walks.rend());
        bool first = true;
        int x = 0;
        int ylow=0, yhigh=0;

        long long lcarea = 0;

        FORE(it, walks) {
            if (first) {
                x = it->first;
                ylow = it->second;
                yhigh = it->second;
                first = false;
            }
            else {
                int lx = x;
                int bylow = ylow;
                int byhigh = yhigh;
                x = it->first;
                SMIN(ylow, it->second);
                SMAX(yhigh, it->second);
                if (lx != x) {
                    right_block.pb( make_pair( lx, make_pair(bylow, byhigh) ) );
                }
            }
        }
        right_block.pb(make_pair(x, make_pair(ylow, yhigh)));
    }

    /*
    FORE(it, left_block) {
        cout <<it->first <<",(" << it->second.first <<"," << it->second.second <<")"<<endl;
    }
    cout <<"---" <<endl;

    FORE(it, right_block) {
        cout <<it->first <<",(" << it->second.first <<"," << it->second.second <<")"<<endl;
    }
    cout <<"---" <<endl;
    */
    ll convex = 0ll;
    FOR(i, 0, left_block.sz) {
        ll tarea;
        if (i == 0) {
            tarea = (10000-left_block[i].first) * width(left_block[i].second);
        }
        else {
            tarea = (10000-left_block[i].first) * 
                (width(left_block[i].second) - width(left_block[i-1].second));
        }
        convex += tarea;
    }

    FOR(i, 0, right_block.sz) {
        ll tarea;
        if (i == 0) {
            tarea = (10000-right_block[i].first) * width(right_block[i].second);
        }
        else {
            tarea = (10000-right_block[i].first) * 
                (width(right_block[i].second) - width(right_block[i-1].second));
        }
        convex -= tarea;
    }
    if (convex < 0) convex = -convex;
    printf("%lld\n", convex - orig_area);



}


int main(int argc, char *argv[]) {
    freopen(argv[1], "r", stdin);
    int Tests;
    cin >> Tests;
    FOR(test, 1, Tests+1) {
        printf("Case #%d: ", test);
        eval();
    }
    return 0;
}
