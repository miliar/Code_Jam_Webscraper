// another fine solution by misof
// #includes {{{
#include <algorithm>
#include <numeric>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <stack>

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>
using namespace std;
// }}}

/////////////////// PRE-WRITTEN CODE FOLLOWS, LOOK DOWN FOR THE SOLUTION ////////////////////////////////

// pre-written code {{{
// BEGIN CUT HERE
#define DEBUG(var) { cout << #var << ": " << (var) << endl; }
template <class T> ostream& operator << (ostream &os, const vector<T> &temp) { os << "[ "; for (unsigned int i=0; i<temp.size(); ++i) os << (i?", ":"") << temp[i]; os << " ]"; return os; } // DEBUG
template <class T> ostream& operator << (ostream &os, const set<T> &temp) { os << "{ "; for(__typeof((temp).begin()) it=(temp).begin();it!=(temp).end();++it) os << ((it==(temp).begin())?"":", ") << (*it); os << " }"; return os; } // DEBUG
template <class T> ostream& operator << (ostream &os, const multiset<T> &temp) { os << "{ "; for(__typeof((temp).begin()) it=(temp).begin();it!=(temp).end();++it) os << ((it==(temp).begin())?"":", ") << (*it); os << " }"; return os; } // DEBUG
template <class S, class T> ostream& operator << (ostream &os, const pair<S,T> &a) { os << "(" << a.first << "," << a.second << ")"; return os; } // DEBUG
template <class S, class T> ostream& operator << (ostream &os, const map<S,T> &temp) { os << "{ "; for(__typeof((temp).begin()) it=(temp).begin();it!=(temp).end();++it) os << ((it==(temp).begin())?"":", ") << (it->first) << "->" << it->second; os << " }"; return os; } // DEBUG
// END CUT HERE
#define FOR(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define SIZE(t) ((int)((t).size()))
// }}}

/////////////////// CODE WRITTEN DURING THE COMPETITION FOLLOWS ////////////////////////////////

int N, M;
vector< vector<int> > G;
vector< vector<int> > A;

vector<int> bfs(int start) {
    vector<int> dist(N,987654321);
    dist[start]=0;
    queue<int> Q;
    Q.push(start);
    while (!Q.empty()) {
        int kde = Q.front(); Q.pop();
        REP(i,SIZE(G[kde])) {
            int kam=G[kde][i];
            if (dist[kam] <= dist[kde]+1) continue;
            dist[kam] = dist[kde]+1;
            Q.push(kam);
        }
    }
    return dist;
}

int prida(int odkial, int kde) {
    int answer = -1; // ubudne on sam
    REP(i,SIZE(G[kde])) {
        if (G[kde][i] == odkial) continue;
        if (!A[odkial][ G[kde][i] ]) ++answer;
    }
    return answer;
}

int skus(const vector<int> &cesta) {
    vector<int> sused(N,0);
    REP(i,SIZE(cesta)) REP(j,SIZE(G[cesta[i]])) sused[ G[cesta[i]][j] ] = 1;
    REP(i,SIZE(cesta)) sused[cesta[i]] = 0;
    REP(i,SIZE(cesta)-1) if (!A[cesta[i]][cesta[i+1]]) return -1;
    return accumulate(sused.begin(),sused.end(),0);
}

int main() {
    int T;
    cin >> T;
    FOR(t,1,T) {
        cin >> N >> M;
        G.clear();
        G.resize(N);
        A.clear();
        A.resize(N, vector<int>(N,0));
        REP(m,M) { 
            int x,y; char ch; cin >> x >> ch >> y; 
            G[x].push_back(y);
            G[y].push_back(x);
            A[x][y] = A[y][x] = 1;
        }
        
        vector<int> d0 = bfs(0), d1 = bfs(1);
        
        int D = d0[1];
        vector< vector<int> > layers(D);

        REP(d,D) REP(n,N) if (d0[n]==d && d1[n]==D-d) layers[d].push_back(n);

        DEBUG(layers);

        vector<int> best(N,-987654321);
        best[0] = SIZE(G[0]);

        FOR(d,1,D-1) REP(i,SIZE(layers[d])) {
            int kde = layers[d][i];
            REP(j,SIZE(layers[d-1])) {
                int odkial = layers[d-1][j];
                if (!A[odkial][kde]) continue;
                best[kde] = max( best[kde], best[odkial] + prida(odkial,kde) );
            }
        }

        int answer = 0;
        REP(i,SIZE(layers[D-1])) answer = max( answer, best[ layers[D-1][i] ] );

        int ans2 = 0;
        if (D==2) {
            REP(a1,SIZE(layers[1])) 
            {
                vector<int> C; C.push_back(0); C.push_back(layers[1][a1]); ans2 = max( ans2, skus(C) );
            }
        }
        if (D==3) {
            REP(a1,SIZE(layers[1])) 
            REP(a2,SIZE(layers[2])) 
            {
                vector<int> C; C.push_back(0); C.push_back(layers[1][a1]); C.push_back(layers[2][a2]); ans2 = max( ans2, skus(C) );
                cout << skus(C) << " pre "; DEBUG(C);
            }
        }
        if (D==4) {
            REP(a1,SIZE(layers[1])) 
            REP(a2,SIZE(layers[2])) 
            REP(a3,SIZE(layers[3])) 
            {
                vector<int> C; C.push_back(0); C.push_back(layers[1][a1]); C.push_back(layers[2][a2]); C.push_back(layers[3][a3]); ans2 = max( ans2, skus(C) );
                // cout << skus(C) << " pre "; DEBUG(C);
            }
        }

        // REP(a1,SIZE(layers[1])) REP(a2,SIZE(layers[2])) { int x=layers[1][a1],y=layers[2][a2]; if (A[x][y]) cout << x << " " << y << endl; }

        if (ans2 > 0 && ans2 != answer) cout << "ZLE JE !!!!!!! vyslo " << answer << " malo " << ans2 << " N=" << N << endl;
        // cout << "D " << D << " answer " << answer << " ans2 " << ans2 << endl;
        // if (D==2 || D==3 || D==4) assert(answer == ans2);


        printf("Case #%d: %d %d\n",t,D-1,answer);
    }
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
