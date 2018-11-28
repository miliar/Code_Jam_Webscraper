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
typedef pair<int, int> pt;

const int INF = (int)1E9 + 7;
const ld EPS = 1E-9;
const ld PI = 3.1415926535897932384626433832795;

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int tcases;
    cin >> tcases;
    cout.precision(10); cout << fixed;

    forn(ccase, tcases){
        printf("Case #%d: ", ccase+1);
        
        int S, R, n, leng;
        ld t;
        cin >> leng >> S >> R >> t >> n;

        vector<int> w(n), lf(n), rg(n);
        map<int, int> L; int rem = leng;
        forn(i, n){
            scanf("%d%d%d", &lf[i], &rg[i], &w[i]);
            L[S+w[i]] += (rg[i]-lf[i]);
            rem -= (rg[i]-lf[i]);
        }

        L[S] += rem;

        vector<pair<int, int> > v(all(L));
        sort(all(v));

        ld ans = 0;

        forn(i, sz(v)){
            int L = v[i].Y, sp = v[i].X;
            ld curTime = ld(L) / ld(sp-S+R);
            if(curTime <= t + EPS){
                t -= curTime;
                ans += curTime;

//                cerr << i << "-" << L << " " << curTime << endl;

            }else{
                ld cL = t * (sp-S+R), rL = L-cL;
                //cerr << i << "+" << cL << " " << rL << " " << sp << " " << t << " " << (rL / sp) << endl;
                ans += t + (rL / ld(sp));                

                t = 0.0;
            }

//            cerr << ans << endl; 
        }

        cout << ans << endl;
    }

    return 0;
}


