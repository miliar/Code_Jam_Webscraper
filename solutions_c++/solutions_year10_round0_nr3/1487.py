/* Author: Divye Kapoor */
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <bitset>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cctype>
#include <functional>
#include <utility>
#include <iterator>
#include <iomanip>
#include <limits>
#include <cmath>
#include <string>
#include <cstring>

using namespace std;

#define LET(x,a) __typeof(a) x(a)
#define FOR(i,l,u) for(LET(i,l); i != (u); ++i)
#define REP(i,u) FOR(i,0,u)
#define INRANGE(x, l, u) ((x) >= (l) && (x) < (u))
#define SHIFTL(x,n) (1 << n)
#define SHIFTR(x,n) (1 >> n)
#define POW2(n) SHIFTL(1,n)
#define IPRINT(s,e) (copy(s,e,ostream_iterator<__typeof(*s)>(cout, " ")))
#define DBG(x) if(_DEBUG) { x; }
#define PB(x) push_back(x)
#define MP(x,y) make_pair(x,y)
#define SET(a,n) memset(&a, n, sizeof(a))
#define PDBG(x) DBG(cerr << x;)

#define _DEBUG 1

typedef vector<int> v_i;
typedef vector<vector<int> > vv_i;
typedef pair<int,int> p_i;
typedef set<int> s_i;
typedef map<string,int> m_si;
typedef priority_queue<int> pq_i;
typedef queue<int> q_i;

int main() {
    size_t n, T, r, k;
    freopen("q3.in", "r", stdin);
    freopen("q3.out", "w", stdout);

    cin >> T;
    REP(cases, T) {
        cin >> r >> k >> n; // r - runs, k - capacity, n - num groups
        vector<long long> g(n);
        REP(i, n) cin >> g[i];

        map<p_i, size_t> b;
        vector<long long> rcost;
        int i = 0, j = 1;
        while(true) {
            if(rcost.size() > r) break;

            long long gr = g[i]; j = (i+1)%n;
            while(j != i && gr + g[j] <= k) { gr += g[j]; ++j; j %= n; }
            if(b.find(MP(i,j)) == b.end() ) {  b[MP(i,j)] = rcost.size(); rcost.PB(gr); }
            else break;
            i = j;
        }
        //FOR(i,b.begin(),b.end()) cerr << '(' << i->first.first << ',' << i->first.second << ',' << i->second << ')' << endl;
        //FOR(i,rcost.begin(),rcost.end()) cerr << *i << endl;

        //FOR(i, 1, rcost.size()) rcost[i] += rcost[i-1];
        if(b.find(MP(i,j)) == b.end()) {
            long long tot = 0; REP(k, r) tot += rcost[k];
            cout << "Case #" << cases+1 << ": " << tot << endl;
        } else {
            long long loopcost = 0;
            size_t loopindex = b[MP(i,j)];
            FOR(k,loopindex, rcost.size()) loopcost += rcost[k];
            size_t loopsize = rcost.size() - loopindex;
            long long initcost = 0;
            REP(k,loopindex) initcost += rcost[k];

            long long result = 0;
            REP(k, min(r,loopindex)) result += rcost[k];
            r -= min(r,loopindex);
            if(r > 0) {
                result += (loopcost) * (r/loopsize);
                r %= loopsize;
                FOR(k, loopindex, loopindex + r) result += rcost[k];
            }
            cout << "Case #" << cases+1 << ": " << result << endl;
        }

        //long long result = (*rcost.rbegin()) * (r/rcost.size()) + (r%rcost.size() == 0? 0 : rcost[r%rcost.size() - 1]);
        //cerr << result << endl;
        //cout << "Case #" << cases+1 << ": " << result << endl;

        //cerr << endl;
    }


    // system("pause");
    return 0;
}

