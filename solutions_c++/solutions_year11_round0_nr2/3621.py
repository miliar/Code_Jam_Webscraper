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

inline int ni() {
    int t;
    scanf(" %d", &t);
    return t;
}

map<string,char> combine;
set<string> destroy;
vector<char> v;
map<char, int> elems;
void invoke(char c) {
    while(v.size() > 0) {
        LET(it, combine.find(string(1, v.back()) + c));
        if(it == combine.end())
            break;
        else {
            elems[v.back()] -= 1;
            v.pop_back();
            c = it->second;
        }
    }
    
    FOR(it, elems.begin(), elems.end()) {
        if(it->second > 0) {
            LET(dit, destroy.find(string(1, it->first) + c));
            if(dit != destroy.end()) {
                v.clear();
                elems.clear();
                return;
            }
        }
    }
    
    v.push_back(c);
    elems[c] += 1;

}

int main() {
    int n;
    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);
    int T = ni();    
    REP(cases, T) {
        string s;
        int C = ni();
        combine.clear();
        REP(i, C) {
            cin >> s;
            string k = s.substr(0,2);
            combine[k] = s[2];
            reverse(k.begin(), k.end());
            combine[k] = s[2];
        }
        
        int D = ni();
        destroy.clear();
        REP(i, D) {
            cin >> s;        
            destroy.insert(s);
            reverse(s.begin(), s.end());
            destroy.insert(s);
        }
        
        int N = ni();
        elems.clear();
        v.clear();
        cin >> s;
        REP(i, N) {
            invoke(s[i]);
        }
        
        cout << "Case #" << cases+1 << ": [";
        REP(i, v.size()) {
            cout << v[i];
            if(i != v.size()-1)
                cout << ", ";
        }
        cout << "]" << endl;
    }
    
    // system("pause");
    return 0;
}

