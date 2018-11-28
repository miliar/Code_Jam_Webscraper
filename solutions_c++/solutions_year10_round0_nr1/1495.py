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
    int n;
    freopen("input.txt", "r", stdin);
    freopen("output1.txt", "w", stdout);
    char *op[] = { "OFF", "ON" };

    unsigned int T, k;
    cin >> T;
    REP(cases, T) {
        cin >> n >> k;
        //cerr << hex << k << endl;
        unsigned int mask = (1 << (n))-1;
        k &= mask;
        //cerr << hex << k << endl;
        bool result = (k&((k+1)&mask) == 0);
        //cerr << boolalpha << result;
        printf("Case #%d: %s\n", cases+1, op[result]);
    }

    // system("pause");
    return 0;
}

