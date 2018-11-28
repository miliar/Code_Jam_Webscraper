

#include <cassert>
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

using namespace std;

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

int cond = (ll)1;
#define db(x) { if (cond > 0) { cond--; rep (xxx, 1) cerr << __LINE__ << " " << #x << " " << x << endl; cerr.flush(); } }
#define mp make_pair

void solve() {
    int C; int D; int N;
    set <pair<int,int> > rem;
    map <pair<int,int>, int> re;
    scanf("%d", &C);
    rep (i, C) {
    db(C);
        char buf[3];
        scanf(" %c %c %c", &buf[0], &buf[1], &buf[2]);
        re[mp(buf[0],buf[1])] = buf[2];
        re[mp(buf[1],buf[0])] = buf[2];
        db(buf[0]<<" "<<buf[1]<<" "<<buf[2]);
    }

    scanf("%d", &D);
    rep (i, D) {
        char buf[2];
        scanf(" %c %c", &buf[0], &buf[1]);
        rem.insert(mp(buf[0], buf[1]));
        rem.insert(mp(buf[1], buf[0]));
        db(buf[0]<<" "<<buf[1]);
    }

    scanf("%d", &N);
    db(C<<" "<<D<<" "<<N);
    vector <int> result;
    map <int, int> used;
    rep (i, N) {
        used.clear();
        rep (i, result.size()) used[result[i]] = 1;
        char zn;
        scanf(" %c", &zn);
        db(zn);
        result.push_back(zn);
        if (result.size() >= 2)   {
            int fi = result[result.size()-2];
            int se = result[result.size()-1];
            if (re[mp(fi,se)] > 0) {
                used[fi]--;
                result.resize(result.size() - 2);
                result.pb(re[mp(fi,se)]);
            }
            else {
                assert(rem.count(mp(zn, zn)) == 0);
                bool ok = rem.count(mp(zn, zn)) > 0;
                fo (j, 'A', 'Z') if (used[j] > 0) {
                    if (rem.count(mp(j, zn)) > 0) {
                        db((char)j<<" "<<zn);
                        ok = 1;
                    }
                }
                db(ok);

                if (ok) {
                    used.clear();
                    result.clear();
                    continue;
                }
            }
        }
        used[zn]++;
    }
    db("");

    rep (i, (int)result.size()) {
        if (i) printf(", ");
        printf("%c", (char)result[i]);
    }

}

int main(int argc, char ** argv) {
	cond = argc >= 2 && argv[1][0] == 'q' ? 1 << 30 : 0;
    int t;
    scanf("%d", &t);
    rep (i, t) {
        printf("Case #%d: [", i + 1);
        solve();
        printf("]\n");
    }
   	return 0;
}


