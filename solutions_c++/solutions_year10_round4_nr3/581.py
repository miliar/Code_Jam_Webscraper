#include <algorithm>
#include <complex>
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
using namespace std;
#define x first
#define y second

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

#define pii pair<int,int>

set<pii>cells;
set<pii>inter[2];

void dodaj1(int krok, int i, int j) {
    inter[krok%2].insert(pii(i,j));
}

void dodaj2(int krok, int i, int j) {
    inter[krok%2].insert(pii(i+1,j));
    inter[krok%2].insert(pii(i,j+1));
}

void solve() {
    cells.clear();
    int R;
    scanf("%d", &R);
    int krok = 0;
    rep (iii, R) {
        int x1,y1,x2,y2;
        scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
        fo (i, x1, x2) fo (j, y1, y2) {
            cells.insert(pii(i,j));
            if (x1 == i || j == y1) {
                dodaj1(krok,i,j);
            }
            if (x2 == i || j == y2) {
                dodaj2(krok,i,j);
            }
        }
    }
    while (cells.size() > 0) {
        inter[(krok+1)%2].clear();
        vector<pii>usun,dodaj;
        fore (it, inter[krok%2]) {
            pii cur = *it;
            if (cells.count(pii(cur.x-1,cur.y)) == 0 &&
                cells.count(pii(cur.x,cur.y-1)) == 0 && 
                cells.count(cur) == 1) {
                usun.pb(cur);
                dodaj2(krok+1,cur.x,cur.y);
            }
            if (cells.count(pii(cur.x-1,cur.y)) == 1 &&
                cells.count(pii(cur.x,cur.y-1)) == 1 &&
                cells.count(cur) == 0) {
                dodaj.pb(cur);
                dodaj2(krok+1,cur.x,cur.y);
            }
        }
        fore (it, usun) cells.erase(*it);
        fore (it, dodaj) cells.insert(*it);
        krok++;
    }


    printf("%d\n", krok);
}

int main(int argc, char ** argv) {
    //freopen("1.in","r",stdin); 
    //freopen("2.in","r",stdin); 
    //freopen("3.in","r",stdin); 

    freopen("../C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
    //freopen("../C-small-attempt1.in","r",stdin);freopen("C-small-attempt1.out","w",stdout);
    //freopen("../C-small-attempt2.in","r",stdin);freopen("C-small-attempt2.out","w",stdout);

    //freopen("../C-large.in","r",stdin); freopen("C-large.out","w",stdout);

    cond = argc >= 2 && argv[1][0] == 'q' ? 1 << 30 : 0;
    int t;
    scanf("%d", &t);
    fo (i, 1, t) {
        cerr << "i" << " " << i << endl;
        printf("Case #%d: ", i);
        solve();
        fflush(stdout);
        cerr.flush();
    }
	return 0;
}

