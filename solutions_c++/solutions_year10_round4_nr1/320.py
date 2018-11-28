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

int M[100][100];
int k;

void transform(int r, int c, int &x, int &y)  {
    int ox, oy;

    x = -r + c;
    y = r + c - k + 1;
}

void invtransform(int x, int y, int &r, int &c) {
    r = (y - x + k - 1) / 2;
    c = (x + y + k - 1) / 2;
}

int main(int argc, char *argv[]) {
    freopen(argv[1], "r", stdin);
    int Tests;
    string line;
    getline(cin, line);
    Tests = atoi(line.c_str());

    FOR(test, 1, Tests+1) {

        getline(cin, line);
        k = atoi(line.c_str());

        for (int i = 0; i < k*2-1; i++) {
            int linewidth = min(i+1, k*2-1-i);
            getline(cin, line);
            istringstream ri(line);
            int o_r, o_c;

            if (i < k) {
                o_r = i; o_c = 0;
            }
            else {
                o_r = k-1; o_c = i-k+1;
            }

            for (int j = 0; j < linewidth; j++) {
                int value;
                ri >> value;
                int tr, tc;
                tr = o_r - j;
                tc = o_c + j;

                M[tr][tc] = value;
            }
        }

        vector<int> xsymmetry;
        vector<int> ysymmetry;

        for (int s_x = -k+1; s_x <= k-1; s_x++) {
            bool symmetric = true;
            for (int r = 0; r < k; r++) {
                for (int c = 0; c < k; c++) {
                    int x, y;
                    transform(r, c, x, y);
                    x = -(x-s_x) + s_x;
                    int nr, nc;
                    invtransform(x, y, nr, nc);
                    if (0 <= nr && nr < k && 0 <= nc && nc < k) {
                        if (M[r][c] != M[nr][nc]) {
                            symmetric = false;
                        }
                    }
                }
            }
            if (symmetric) {
                xsymmetry.pb(s_x);
            }
        }

        for (int s_y = -k+1; s_y <= k-1; s_y++) {
            bool symmetric = true;
            for (int r = 0; r < k; r++) {
                for (int c = 0; c < k; c++) {
                    int x, y;
                    transform(r, c, x, y);
                    y = -(y-s_y) + s_y;
                    int nr, nc;
                    invtransform(x, y, nr, nc);
                    if (0 <= nr && nr < k && 0 <= nc && nc < k) {
                        if (M[r][c] != M[nr][nc]) {
                            symmetric = false;
                        }
                    }
                }
            }
            if (symmetric) {
                ysymmetry.pb(s_y);
            }
        }

        int minimum = 2147483647;

        FORE(it, xsymmetry) {
            FORE(jt, ysymmetry) {
                int minr=0, minc=0, maxr=k-1, maxc=k-1;
                int r, c, nr, nc;
                int x, y;
                r = 0; c = 0;

                transform(r, c, x, y);
                x = -(x - *it) + *it;
                y = -(y - *jt) + *jt;
                invtransform(x, y, nr, nc);
                minr = min(minr, nr); minc = min(minc, nc);
                maxr = max(maxr, nr); maxc = max(maxc, nc);

                r = 0; c = k-1;
                transform(r, c, x, y);
                x = -(x - *it) + *it;
                y = -(y - *jt) + *jt;
                invtransform(x, y, nr, nc);
                minr = min(minr, nr); minc = min(minc, nc);
                maxr = max(maxr, nr); maxc = max(maxc, nc);

                r = k-1; c = 0;
                transform(r, c, x, y);
                x = -(x - *it) + *it;
                y = -(y - *jt) + *jt;
                invtransform(x, y, nr, nc);
                minr = min(minr, nr); minc = min(minc, nc);
                maxr = max(maxr, nr); maxc = max(maxc, nc);

                r = k-1; c = k-1;
                transform(r, c, x, y);
                x = -(x - *it) + *it;
                y = -(y - *jt) + *jt;
                invtransform(x, y, nr, nc);
                minr = min(minr, nr); minc = min(minc, nc);
                maxr = max(maxr, nr); maxc = max(maxc, nc);

                int size = max(maxr-minr+1, maxc-minc+1);

                int add = size * size - k*k;
                minimum=min(add, minimum);

            }
        }

        printf("Case #%d: %d\n", test, minimum);
    }
    return 0;

}

