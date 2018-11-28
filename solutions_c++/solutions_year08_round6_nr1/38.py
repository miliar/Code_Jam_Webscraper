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
#include <map>
#include <cassert>

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

struct measure {
    int h;
    int w;
    bool is_bird;
};

struct prect {
    int hmin, hmax;
    int wmin, wmax;
    bool in (int h, int w) {
        return hmin <= h && h <= hmax &&
               wmin <= w && w <= wmax;
    }
    bool inno (int h, int w) {
        return hmin < h && h < hmax &&
               wmin < w && w < wmax;
    }
};

int main(int argc, char *argv[]) {
    freopen(argv[1], "r", stdin);
    int Tests;
    cin >> Tests;
    FOR(test, 1, Tests+1) {
        int n, m;
        printf("Case #%d:\n", test);
        cin >> n;
        
        vector<measure> vm;
        REP(i, n) {
            measure me;
            string s;
            cin >>me.h >>me.w >>s;
            if (s[0] == 'B') me.is_bird = true; else me.is_bird = false;
            vm.pb(me);
            if (s[0] == 'N') cin >>s;
        }
        int w_min = 1000001, w_max = 0;
        int h_min = 1000001, h_max = 0;

        bool first = true;
        bool all_unknown = false;
        REP(i, n) {
            if (vm[i].is_bird) {
                if (first) {
                    h_min = vm[i].h;
                    h_max = vm[i].h;
                    w_min = vm[i].w;
                    w_max = vm[i].w;
                    first = false;
                }
                else {
                    SMIN(h_min, vm[i].h);
                    SMAX(h_max, vm[i].h);
                    SMIN(w_min, vm[i].w);
                    SMAX(w_max, vm[i].w);
                }
            }
        }
        vector<prect> cand_rect;
        prect bird;
        if (h_min > h_max) {
            all_unknown = true;
        }
        else {
            bird.hmin = h_min;
            bird.hmax = h_max;
            bird.wmin = w_min;
            bird.wmax = w_max;
            cand_rect.pb(bird);

            vector<int> h_cand;
            h_cand.pb(0);
            h_cand.pb(1000001);
            REP(i, n) {
                h_cand.pb(vm[i].h);
            }
            sort(all(h_cand));
            REP(i, h_cand.sz) {
                FOR(j, i, h_cand.sz) {
                    int shmin = h_cand[i];
                    int shmax = h_cand[j];
                    if (shmin <= bird.hmin && shmax >= bird.hmax) {
                        prect cand;
                        cand.hmin = shmin;
                        cand.hmax = shmax;
                        cand.wmin = 0;
                        cand.wmax = 1000001;
                        bool feasible = true;
                        REP(k, n) {
                            if (!vm[k].is_bird) {
                                if (shmin < vm[k].h &&
                                    shmax > vm[k].h) {
                                    //fprintf(stderr, "%d %d\n", vm[k].w, bird.wmax);
                                    if (bird.wmin < vm[k].w  &&
                                        bird.wmax > vm[k].w) {
                                        feasible = false;
                                        break;
                                    }
                                    else if (bird.wmin > vm[k].w) {
                                        SMAX(cand.wmin, vm[k].w);
                                    }
                                    else
                                        SMIN(cand.wmax, vm[k].w);
                                }
                            }
                        }
                        //fprintf(stderr, "H: %d %d\n", shmin, shmax);
                        REP(k, n) {
                            if (vm[k].is_bird && !cand.inno(vm[k].h, vm[k].w)) {
                                feasible = false;
                                break;
                            }
                        }
                        if (!feasible) continue;
                        /*
                        printf("CAND: %d %d %d %d\n",
                                cand.hmin, cand.hmax,
                                cand.wmin, cand.wmax);
                        */
                        if (cand.wmin <= bird.wmin &&
                            bird.wmax <= cand.wmax) {
                            cand_rect.pb(cand);
                            /*
                            fprintf(stderr, "CAND: %d %d %d %d\n",
                                    cand.hmin, cand.hmax,
                                    cand.wmin, cand.wmax);
                            */
                        }
                    }
                }
            }
        }
        cin  >>m;
        REP(i, m) {
            int h, w;
            cin >>h >>w;
            if (all_unknown) { // no bird
                //
                //  TODO: exact matching
                //
                bool is_nobird = false;
                REP(j, n) {
                    if (vm[j].h == h && vm[j].w == w) {
                        is_nobird = true;
                    }
                }
                if (is_nobird) {
                    cout <<"NOT BIRD" <<endl;
                }
                else {
                    cout <<"UNKNOWN" <<endl;
                }
            }
            else {
                if (bird.in(h, w)) {
                    cout <<"BIRD" <<endl;
                }
                else {
                    bool found = false;
                    FORE(it, cand_rect) {
                        if (it->inno(h, w)) {
                            found = true;
                            break;
                        }
                    }
                    if (!found) {
                        cout <<"NOT BIRD" <<endl;
                    }
                    else {
                        cout <<"UNKNOWN" <<endl;
                    }
                }
            }
        }
    }

}

