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

bool can(const vector<int>& a, int idx, ld yi){
    ld remx = 0;
    forn(i, sz(a))
        remx += a[i];

    ld curv = a[idx] + remx * yi;
    remx = (1.0 - yi) * remx;

    vector<ld> b(all(a));
    b[idx] = 1000000000;

    while(abs(remx) > EPS){
        ld curmin = (*min_element(all(b))), nextmin = 1e100;
        int cntmin = 0;
        forn(i, sz(b)){
            if(abs(b[i] - curmin) < EPS){
                cntmin++;
            }else{
                nextmin = min(nextmin, b[i]);
            }
        }

        ld have = min(remx, (nextmin - curmin) * cntmin);
        forn(i, sz(b))
            if(abs(b[i] - curmin) < EPS)
                b[i] += have / cntmin;
        remx -= have;
    }

    return (*min_element(all(b))) <= curv;
}

int main() {
    #ifdef myproject
    freopen("input.txt", "rt", stdin);
    //freopen("output.txt", "wt", stdout);
    #endif

    int testCount = 0;
    scanf("%d", &testCount); char testBuf[10]; gets(testBuf);
    for1(currentTest, testCount){
        printf("Case #%d: ", currentTest);
        //solution

        int n;
        cin >> n;
        vector<int> a(n);
        forn(i, n)
            cin >> a[i];

        vector<ld> ans(n);
        forn(i, n){
            ld lf = 0.0, rg = 1.0;

            forn(step, 200){
                ld mid = (lf + rg) / 2;

                if(can(a, i, mid)){
                    rg = mid;
                }else
                    lf = mid;
            }
            
            ans[i] = lf;
        }

        forn(i, sz(ans))
            printf("%.10lf ", double(ans[i])*100);
        fprintf(stderr, "Test #%d: %d\n", currentTest, (int)clock());
        puts("");
    }

    return 0;
}


