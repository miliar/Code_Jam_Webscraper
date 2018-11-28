/* Author: Divye Kapoor */
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <list>
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
#define PB(x) push_back(x)
#define D(x) if(_DEBUG) { cout << #x ": " << x << endl; }


#define _DEBUG 0

typedef vector<int> v_i;
typedef vector<vector<int> > vv_i;
typedef pair<int,int> p_i;
typedef set<int> s_i;
typedef map<string,int> m_si;
typedef priority_queue<int> pq_i;
typedef queue<int> q_i;

inline int ni() {
    int t;
    scanf(" %d", &t);
    return t;
}

int seqP[101];
char seqR[101];


int sgn(int x) {
    if(x == 0) return 0;
    return x/abs(x);
}

int main() {
    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);
    
    int t = ni();    
    REP(cases, t) {
        int n = ni();
        int o = 1, b = 1;
        list<int> O, B;
        REP(i, n) {
            scanf(" %c", &seqR[i]);
            scanf(" %d", &seqP[i]);
            
            switch(seqR[i]) {
                case 'O':
                    O.PB(seqP[i]);
                    break;
                case 'B':
                    B.PB(seqP[i]);
                    break;
            }
        }
        
        B.PB(101);
        O.PB(101);
        
        int t = 0, pos = 0;
        while(pos < n) {
            int nextEventB = B.front()-b;
            int nextEventO = O.front()-o;
            int deltaT;
            
            D(t);
            D(o);
            D(b);

            switch(seqR[pos]) {
                case 'O':
                    deltaT = abs(nextEventO) + 1;
                    o += nextEventO;
                    b += sgn(nextEventB)*min(deltaT, abs(nextEventB));
                    O.pop_front();
                    break;
                case 'B':
                    deltaT = abs(nextEventB) + 1;
                    b += nextEventB;
                    o += sgn(nextEventO)*min(deltaT, abs(nextEventO));
                    B.pop_front();
                    break;
            }
                      
            t += deltaT;
            ++pos;            
        }
            D(t);
            D(o);
            D(b);
        
        printf("Case #%d: %d\n", cases+1, t);
    }
    
    // system("pause");
    return 0;
}

