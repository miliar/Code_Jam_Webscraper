/* Author: Divye Kapoor */
#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
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
#define DMP(s,e) (copy(s,e,ostream_iterator<__typeof(*s)>(cout, " ")))
#define DUMP(v) { cout << #v ": "; DMP(v.begin(), v.end()); cout << endl; }
#define DBG(x) if(_DEBUG) { x; }
#define PB(x) push_back(x)
#define MP(x,y) make_pair(x,y)
#define SET(a,n) memset(&a, n, sizeof(a))
#define PDBG(x) DBG(cerr << x;)
#define D(x) { cout << #x ": " << x << endl; }

#define _DEBUG 1

typedef vector<int> v_i;
typedef vector<vector<int> > vv_i;
typedef pair<int,int> p_i;
typedef set<int> s_i;
typedef map<string,int> m_si;
typedef priority_queue<int> pq_i;
typedef queue<int> q_i;
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int ui;

inline int ni() {
    int t;
    scanf(" %d", &t);
    return t;
}

inline ll nll() {
    ll t;
    scanf(" %lld", &t);
    return t;
}

inline ull null_() {
    ull t;
    scanf(" %llu", &t);
    return t;
}

int main() {
    int t = ni();
    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);
    REP(cases, t) {
        ull N = null_(), L = null_(), H = null_();
        vector<ull> v(N);
        REP(i, N) {
            v[i] = null_();
        }
        sort(v.begin(), v.end());

        printf("Case #%d: ", cases+1);
        FOR(i, L, H+1) {
            REP(j, N) {
                if(i%v[j] != 0 && v[j]%i != 0) goto next;
            }
            printf("%llu\n", i);
            goto done;
            
            next:
            ;
        }
        
        printf("NO\n");
        done:
        ;
    }
    
    
    // system("pause");
    return 0;
}

