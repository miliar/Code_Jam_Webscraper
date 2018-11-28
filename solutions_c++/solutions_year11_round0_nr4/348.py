

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

const int sz = 1011;

ld popr[sz+11][sz+11];

ld dw[sz+11][sz+11];
ld sol[sz+11];
ld sil[sz+11];

void solve() {
    int n;
    scanf("%d", &n);

    int cnt = 0;
    fo (i, 1, n) { int x; scanf("%d", &x); if (x != i) { cnt++; } }

    printf("%.6Lf", sol[cnt]);
}

int main(int argc, char ** argv) {
	cond = argc >= 2 && argv[1][0] == 'q' ? 1 << 30 : 0;
    dw[0][0] = 1;
    rep (i,sz) rep(j, sz) {
        if (i&&j) dw[i][j] += dw[i-1][j-1];
        if (i) dw[i][j] += dw[i-1][j];
    }

    db(dw[5][2]);

    sil[0] = 1;
    fo (i, 1, sz) sil[i] = sil[i-1] * i;
    db(sil[3]);

    popr[1][1] = 1;
    fo (a, 1, sz) fo (b, 0, sz) {
        ld cur = popr[a][b];
        popr[a+1][b+1] += cur; // 1 poprawny dodaje
        if (b)  popr[a+1][b-1] += b * cur;
        popr[a+1][b] += (a-b) * cur;
    }
        cerr << endl;
    fo (a, 1, 3) {
        fo (b, 0, 3) {
            cerr << popr[a][b] <<  " ";

        }
        cerr << endl;
    }
        cerr << endl;

    fo (len, 2, sz) {
        ld sum = 0;
        ld praw = 0;
        ld expect = 0;
        ford (p, len, 1) {
            ld xx = popr[len][p];

            praw += (xx / sil[len]);
            expect +=  (sol[len - p]) * (xx / sil[len]);
            if (len <= 5) db(len<<" "<<p<<" "<<" "<<xx<<" "<<sum<<" "<<sil[len]<<" "<<sol[len-p]<<" !! " << dw[len][p]<<" "<<sil[len-p]);
        }
        if (len <= 5) db(expect<<" "<<praw);
        sol[len] = (1 + expect) / (1 - popr[len][0] / sil[len]);
    }


    int t;
    scanf("%d", &t);
    rep (i, t) {
        printf("Case #%d: ",  i + 1);
        solve();
        printf("\n");
    }
   	return 0;
}


