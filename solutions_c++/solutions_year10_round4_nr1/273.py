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

#define pii complex<int>

char buf[211];
char ary[211][211];
int size[211];

void solve() {
    int k;
    gets(buf);
    sscanf(buf, "%d", &k);

    clr(ary, 0);
    rep (i, 2 * k - 1) gets(ary[i]);

    size[0] = 0;
    size[1] = 1;
    for (int add = 4, i = 2; i < 211; i ++, add += 4) {
        size[i] = size[i-2] + add;
    }
    db(size[2]<<" "<<size[3]<<" "<<size[4]);

    rep (i, 2 * k - 1) rep (j, 2 * k - 1) {
        if (ary[i][j] < ' ') ary[i][j] = ' ';
    }

    int result = (int)210;
    rep (i, 2 * k - 1) rep (j, 2 * k - 1) {
        int nk = k + abs(i - (k-1)) + abs(j - (k-1));
        //if (nk >= result) continue;
        bool ok = 1;
        db(i<<" "<<j);
        rep (i2, 2 * k - 1) {
            rep (j2, 2 * k - 1) {
                // by i
                int i3 = i - (i2 - i);
                int j3 = j - (j2 - j);
                {
                    if (i3 >= 0 && i3 < 2 * k - 1) {
                        ok = ok && (ary[i2][j2] == ary[i3][j2] || ary[i2][j2] == ' ' || ary[i3][j2] == ' ');
                        db((int)ary[i2][j2]<<" "<<(int)ary[i3][j2]<<" "<<ok);
                    }
                }
                {
                    // by j
                    if (j3 >= 0 && j3 < 2 * k - 1) {
                        ok = ok && (ary[i2][j2] == ary[i2][j3] || ary[i2][j2] == ' ' || ary[i2][j3] == ' ');
                        db((int)ary[i2][j2]<<" "<<(int)ary[i2][j3]<<" "<<ok);
                    }
                }
                if (!ok) break;
            }
            if (!ok) break;
        }
        db(i<<" "<<j<<" "<<ok);
        if (ok && nk < result) {
            result = nk;

        }
        // srodek
    }
    printf("%d\n", size[result] - size[k]);
}

int main(int argc, char ** argv) {
    //freopen("1.in","r",stdin); 
    //freopen("2.in","r",stdin); 
    //freopen("3.in","r",stdin); 

    //freopen("../A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
    //freopen("../A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
    //freopen("../A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);

    freopen("../A-large.in","r",stdin); freopen("A-large.out","w",stdout);

    cond = argc >= 2 && argv[1][0] == 'q' ? 1 << 30 : 0;
    int t;
    gets(buf);
    sscanf(buf, "%d", &t);
    fo (i, 1, t) {
        cerr << "i" << " " << i << endl;
        printf("Case #%d: ", i);
        solve();
        fflush(stdout);
        cerr.flush();
    }
    return 0;
}

