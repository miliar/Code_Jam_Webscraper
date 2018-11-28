#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <numeric>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <complex>

#include <cassert>
using namespace std;

//
#define MP make_pair
#define VI vector<int>
#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define REP(i,n) for(int i=0;i<(n);++i)
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second
#define SIZE(x) (int)x.size()
#define ALL(c) c.begin(),c.end()
//
#define rep(i,b) for(int i=(0);i<(b);++i)
#define fo(i,a,b) for(int i=(a);i<=(b);++i)
#define ford(i,a,b) for(int i=(a);i>=(b);--i)
#define fore(a,b) for(__typeof((b).begin()) a = (b).begin();a!=(b).end();++a)
#define vv vector
#define pb push_back
#define ll long long
#define ld long double
#define ss(a) (int)(a).size()
#define all(x) (x).begin(),(x).end()
#define clr(x,a) memset(x,a,sizeof(x))
#define vi vv<int>
#define vs vv<string>
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}

int cond = (ll)1;
#define db(x) { if (cond > 0) { cond--; rep (xxx, 1) cerr << __LINE__ << " " << #x << " " << x << endl; cerr.flush(); } }

#define pdd pair<ld,ld>

int W, L, U, G;

pair<ld,ld> LL[1011];
pair<ld,ld> UU[1011];
#define pdd pair<ld,ld>
#define x first
#define y second 

ld pole(ld pos) {
    ld sum = 0;
    pair<ld,ld> first[2], last[2];
    rep (g, 2) {
        first[g] = g==0?LL[0]:UU[0];
        last[g] = g==0?LL[L-1]:UU[U-1];

        for (int i = 0; ; i++) {
            if (g==0 && i >= L) break;
            if (g==1 && i >= U) break;

            pdd le = g==0?LL[i]:UU[i];
            if (le.first >= pos) break;
            pdd ri = g==0?LL[i+1]:UU[i+1];
            if (ri.first >= pos) {
                ld x = (pos - le.first) / (ri.first - le.first);
                ri = pdd(le.x * (1-x) + ri.x * x, le.y * (1-x) + ri.y * x);
                last[g] = ri;
            }

            ld cur = le.x * ri.y - le.y*ri.x;
            if (g == 0) sum += cur;
            else sum -= cur;
        }
    }
    sum -= first[0].x * first[1].y - first[1].x * first[0].y;
    sum += last[0].x * last[1].y - last[1].x * last[0].y;
    return abs(sum) / 2;
}

void _main() {
    scanf("%d%d%d%d", &W, &L, &U, &G);
    rep (i, L) {
        scanf("%Lf%Lf", &LL[i].first, &LL[i].second);
    }
    rep (i, U) {
        scanf("%Lf%Lf", &UU[i].first, &UU[i].second);
    }
    assert(LL[0].second < UU[0].second);
    ld cale = pole(W);
    db(LL[L-1].first);
    db(cale);
    fo (i, 1, G - 1) {
        ld from = 0;
        ld to = W;
        rep (j, 70) {
            ld mid = (from + to) / 2;
            db(from<<" "<<to<<" "<<cale*i/G<<" "<<pole(mid));
            if (pole(mid) > cale * i / G) {
                to = mid;
            }
            else 
                from = mid;
        }
        printf("%.6Lf\n", from);
    }
}

int main(int argc, char ** argv) {
    string p = "../gcj/source/" + string("") + argv[0][strlen(argv[0])-1];
//    if (argc >= 2 && strcmp(argv[1], "q") != 0) { freopen(argv[1],"r",stdin);}

    rep (i, argc) if (strcmp(argv[i], "1n") == 0) { freopen("1.in","r",stdin);}
    rep (i, argc) if (strcmp(argv[i], "2n") == 0) { freopen("2.in","r",stdin);}
    rep (i, argc) if (strcmp(argv[i], "3n") == 0) { freopen("3.in","r",stdin);}
    rep (i, argc) if (strcmp(argv[i], "4n") == 0) { freopen("4.in","r",stdin);}
    rep (i, argc) if (strcmp(argv[i], "5n") == 0) { freopen("5.in","r",stdin);}

    rep (i, argc) if (strcmp(argv[i], "s0") == 0) { freopen((p + "-small-0.in").c_str(),"r",stdin);freopen((p + "-small-0.out").c_str(),"w",stdout); }
    rep (i, argc) if (strcmp(argv[i], "s1") == 0) { freopen((p + "-small-1.in").c_str(),"r",stdin);freopen((p + "-small-1.out").c_str(),"w",stdout); }
    rep (i, argc) if (strcmp(argv[i], "s2") == 0) { freopen((p + "-small-2.in").c_str(),"r",stdin);freopen((p + "-small-2.out").c_str(),"w",stdout); }
    rep (i, argc) if (strcmp(argv[i], "l0") == 0) { freopen((p + "-large-0.in").c_str(),"r",stdin);freopen((p + "-large-0.out").c_str(),"w",stdout); }
    rep (i, argc) if (strcmp(argv[i], "q") == 0) cond = 1 << 30;
    db(argc);
    int t;
    scanf("%d", &t);
    fo (i, 1, t) {
        db(i);
        printf("Case #%d:\n", i);
        _main();
        fflush(stdout);
        cerr.flush();
    }
    return 0;
}

