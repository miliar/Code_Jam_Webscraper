#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define ford(i, n) for(int i = int(n) - 1; i >= 0; --i)
#define fore(i, l, r) for(int i = int(l); i < int(r); ++i)
#define sz(v) int((v).size())
#define X first
#define Y second
#define all(v) (v).begin(), (v).end()
#define mp(q, p) make_pair(q, p)
#define sqr(a) ((a) * (a))
#define pb push_back
#define ensure(a) assert(a)

using namespace std;

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = 1E9 + 7;
const int NMAX = 1E3 + 7;
const ld EPS = 1E-9;


int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int T;
    scanf("%d", &T);
    for1(F, T){
        printf("Case #%d: ", F);
        int P, Q;
        scanf("%d%d", &P, &Q);
        vector<int> qs(Q);
        forn(i, Q) scanf("%d", &qs[i]);
        sort(all(qs));
        vector<int> gr;
        gr.pb(0);
        gr.pb(P + 1);
        int ans = INF;
        vector<int> tmp = gr;
        do{
            gr = tmp;
            int pans = 0;
            forn(i, sz(qs)){
                fore(j, 1, sz(gr)){
                    if(gr[j - 1] < qs[i] && qs[i] < gr[j]){
                        pans += gr[j] - gr[j - 1] - 2;
                        break;
                    }
                }
                gr.pb(qs[i]);
                sort(all(gr));
            }
            ans = min(ans, pans);
        }while(next_permutation(all(qs)));
        cout << ans << endl;
    }
    return 0;
}
