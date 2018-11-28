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

const int NMAX = 110;
const int PMAX = 100;

int n;
int type[NMAX], x[NMAX];
int d[NMAX][NMAX][NMAX];

struct state{
    int v, lf, rg;
    state(){}
    state(int v, int lf, int rg): v(v), lf(lf), rg(rg){};
};

#define pos(a) a.v][a.lf][a.rg

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int testCount;
    cin >> testCount;
    forn(curTest, testCount){
        printf("Case #%d: ", curTest+1);

        //Place solution here
        cin >> n;

        forn(i, n){
            char ct;
            scanf(" %c %d ", &ct, &x[i]);
            type[i] = int(ct == 'B');
            x[i]--;
        }

        memset(d, 63, sizeof d);
        queue<state> q;
        state start(0, 0, 0);
        d[pos(start)] = 0, q.push(start);

        int ans = INF;
        while(!q.empty()){
            state s = q.front(); q.pop();
            
            if(s.v == n){
                ans = min(ans, d[pos(s)]);
                continue;
            }

            for(int d1 = -1; d1 <= 1; d1++)
                for(int d2 = -1; d2 <= 1; d2++){

                    int nlf = s.lf + d1, nrg = s.rg + d2;

                    if(0 <= nlf && nlf < PMAX && 0 <= nrg && nrg < PMAX){
                        state ns(s.v + int(type[s.v] == 0 && d1 == 0 && s.lf == x[s.v]) + int(type[s.v] == 1 && d2 == 0 && s.rg == x[s.v]), 
                                 nlf, nrg);
                        if(d[pos(ns)] > d[pos(s)] + 1){
                            d[pos(ns)] = d[pos(s)] + 1;
                            q.push(ns);
                        }
                    } 

                }
        }        
        cout << ans << endl;
    }
    
    return 0;
}



