#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <climits>
#include <cfloat>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <numeric>
#include <complex>
#include <utility>
#include <memory>
#include <iomanip>
#include <algorithm>
#include <functional>
#include <sstream>
#include <assert.h>
using namespace std;

const double EPS = 1e-9;
const int INF = 100000000;
const int MOD = 1000000007;

typedef vector<int> vint;
typedef vector<vint> vvint;
typedef vector<string> vst;
typedef pair<int,int> pint;
typedef long long ll;

#define debug(x) cout<<#x<<" = "<<(x)<<" (L"<<__LINE__<<")"<<endl
template<class T1, class T2> ostream& operator<<(ostream &s, pair<T1,T2> P){return s<<'<'<<P.first<<", "<<P.second<<'>';}
template<class T> ostream& operator<<(ostream &s, vector<T> P) {s<<"{ ";for(int i=0;i<P.size();++i){if(i>0)s<<", ";s<<P[i];}return s<<" }"<<endl;}
template<class T> ostream& operator<<(ostream &s, vector<vector<T> > P) {for(int i=0;i<P.size();++i){s<<i<<" : "<<P[i];}return s;}

int N;
int num;
vvint M;

struct Edge {
    int from, to, cost;
    Edge(int f, int t, int c) : from(f), to(t), cost(c) {}
    friend bool operator < (const Edge &e1, const Edge &e2) {return e1.cost < e2.cost;}
    friend ostream& operator << (ostream& s, const Edge& E) {s << E.from << "->" << E.to << '(' << E.cost << ')';return s;}
};

// Graph
const int MAX_V = 1000;
struct Graph {
    static const int MAX_V_ = ::MAX_V;
    int V,E;
    vector<Edge> list[MAX_V_];
    
    Graph(int n = 0) : V(n), E(0) {}
    void init(int n) {V = n; E = 0;}
    inline vector<Edge>& operator [] (int i) {return list[i];}
    friend ostream& operator << (ostream& s, const Graph& G) {for (int i = 0; i < G.V; ++i) {s << i << " : " << G.list[i];}return s;}
};    

void direct(Graph &G, int f, int t, int c) {
    ++G.E;
    G[f].push_back(Edge(f,t,c));
}

int dist[MAX_V][MAX_V];
void WarshallFloyd(Graph G) {
    for (int i = 0; i < G.V; ++i) {
        for (int j = 0; j < G.V; ++j) {
            dist[i][j] = 0;
        }
        for (int j = 0; j < G[i].size(); ++j) {
            dist[i][G[i][j].to] = 1;
        }
    }
    
    for (int k = 0; k < G.V; ++k) {
        for (int i = 0; i < G.V; ++i) {
            for (int j = 0; j < G.V; ++j) {
                    dist[i][j] += dist[i][k] * dist[k][j];
            }
        }
    }
}


string solve() {
    Graph G(N);
    //cout << M;
    for (int i = 0; i < M.size(); ++i) {
        for (int j = 0; j < M[i].size(); ++j) {
            direct(G, i, M[i][j], 1);
        }
    }
    //cout << G;
    WarshallFloyd(G);
    
    //for (int i = 0; i < N; ++i) cout << vint(dist[i],dist[i]+N);
    
    bool ex = false;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (dist[i][j] >= 2) ex = true;
        }
    }
    return ex ? "Yes" : "No";
}

int main() {
    freopen( "/Users/macuser/Downloads/A-large.in", "r", stdin );
    freopen( "/Users/macuser/Downloads/AL.txt", "w", stdout );
    
    int T;
    scanf("%d", &T);
    for (int id = 1; id <= T; ++id) {
        cin >> N;
        M.clear();
        for (int i = 0; i < N; ++i) {
            cin >> num;
            vint temp;
            for (int j = 0; j < num; ++j) {
                int tnum;
                cin >> tnum;
                temp.push_back(tnum-1);
            }
            M.push_back(temp);
        }
        
        printf("Case #%d: ", id);
        cout << solve();
        printf("\n");
    }
    
    return 0;
}