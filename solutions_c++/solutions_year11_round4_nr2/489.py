#pragma comment(linker, "/STACK:10000000")

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <bitset>
#include <sstream>

#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>

#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>

using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define ford(i, n) for(int i = int(n) - 1; i >= 0; --i)
#define fore(i, l, r) for(int i = int(l); i < int(r); ++i)
#define sz(v) int((v).size())
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define X first
#define Y second
#define mp make_pair
#define debug(x) {cerr << #x << " = " << x << endl;}
template<typename T> inline T abs(T a){ return ((a < 0) ? -a : a); }
template<typename T> inline T sqr(T a){ return a * a; }

typedef long long li;
typedef long double ld;
//typedef pair<int, int> pt;

const int INF = (int)1E9 + 7;
const ld EPS = 1E-9;
const ld PI = 3.1415926535897932384626433832795;

const string imp = "IMPOSSIBLE";

struct pt{
    ld x, y;
    pt(){}
    pt(ld x, ld y): x(x), y(y){
    }
};

pt operator + (const pt& a, const pt& b){
    return pt(a.x+b.x, a.y+b.y);
}
pt operator - (const pt& a, const pt& b){
    return pt(a.x-b.x, a.y-b.y);
}

int a[600][600];
pt da[600][600];

pt sumd[600][600];
ld suma[600][600];

template<typename T>
inline T S(int i1, int i2, int j1, int j2, T sum[600][600], T zero){
    T s22 = sum[i2][j2],
      s11 = (i1 == 0 || j1 == 0) ? zero : sum[i1-1][j1-1],
      s21 = (j1 == 0) ? zero : sum[i2][j1-1],
      s12 = (i1 == 0) ? zero : sum[i1-1][j2];

    return s22 - s21 - s12 + s11;
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    cout.precision(10); cout << fixed;

    int tcases;
    cin >> tcases;
    forn(ccase, tcases){
        printf("Case #%d: ", ccase+1);
    
        int n, m, d;
        cin >> n >> m >> d;
        forn(i, n)
            forn(j, m){ 
                char c;
                scanf(" %c ", &c);
                a[i][j] = d+int(c-'0');

                da[i][j] = pt((i+0.5) * a[i][j], (j+0.5) * a[i][j]);

                {
                    pt up = i == 0 ? pt(0,0) : sumd[i-1][j], 
                       lf = j == 0 ? pt(0,0) : sumd[i][j-1], 
                       ul = (i == 0 || j == 0) ? pt(0,0) : sumd[i-1][j-1];

                    sumd[i][j] = up + lf - ul + da[i][j];
                }

                {
                    ld up = i == 0 ? 0 : suma[i-1][j], 
                       lf = j == 0 ? 0 : suma[i][j-1], 
                       ul = (i == 0 || j == 0) ? 0 : suma[i-1][j-1];

                    suma[i][j] = up + lf - ul + a[i][j];
                }
            }



        int maxK = -1;

        forn(i, n)
            forn(j, m){
                for(int k = 3; i+k-1 < n && j+k-1 < m; k++){
                    ld x = (i+(i+k)) * 0.5, y = (j+(j+k)) * 0.5;

                    ld sumx = 0.0, sumy = 0.0;

                    /*
                    forn(ti, k)
                        forn(tj, k){
                            if((ti == 0 || ti == k-1) && (tj == 0 || tj == k-1)) continue;

                            ld cx = i+ti+0.5, cy = j+tj+0.5;

                            sumx += (cx-x) * a[i+ti][j+tj];
                            sumy += (cy-y) * a[i+ti][j+tj];

                        }*/

                    pt res = S(i, i+k-1, j, j+k-1, sumd, pt(0,0));
                    ld mul = S(i, i+k-1, j, j+k-1, suma, ld(0.0));

//                    cerr << res.x << " " << res.y << endl;

                    mul = mul - a[i][j];
                    mul = mul - a[i+k-1][j];
                    mul = mul - a[i][j+k-1];
                    mul = mul - a[i+k-1][j+k-1];

                    res = res - da[i][j];
                    res = res - da[i+k-1][j];
                    res = res - da[i][j+k-1];
                    res = res - da[i+k-1][j+k-1];

                    pt tmp(x * mul, y * mul);

                    res = res - tmp;

//                    cerr << i << " " << j << " " <<  k << endl;
//                    cerr << res.x << " " << res.y << endl;
//                    cerr << sumx << " " << sumy << endl;

                    //if(fabs(res.x-sumx) > EPS || fabs(res.y-sumy) > EPS) throw;

                    sumx = res.x, sumy = res.y;

                    if(fabs(sumx) < EPS && fabs(sumy) < EPS)
                        maxK = max(maxK, k);
                }
            }


        if(maxK == -1)
            cout << imp << endl;
        else
            cout << maxK << endl;    
    }

    return 0;
}


