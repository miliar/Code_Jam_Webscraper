#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>
#include <queue>
using namespace std;

typedef pair<int, int> Edge;

vector<Edge> E;
int N, M;

vector<int> X;

vector<int> D;


bool EE[2000][2000];


bool existsEdge(int u, int v) {
    //return binary_search(E.begin(), E.end(), Edge(u, v));
    return EE[u][v];
}


int countNeighbours(int u, int v) {
    int res=0;
    for (int i=0; i<N; i++)
        if (i!=u && i!=v && (existsEdge(u, i) || existsEdge(v, i)))
            res++;
    return res;
}


int countNewNeighb(int u, int v, int w) {
    int res=0;
    for (int i=0; i<N; i++)
        if (i!=u && i!=v && i!=w && (existsEdge(i, w) && !existsEdge(i, v) && !existsEdge(i, u)))
            res++;
    return res;
}


int main() {
    int Z; cin>>Z;
    for (int z=1; z<=Z; z++) {
        cin>>N>>M;
        
        for (int i=0; i<N; i++)
            for (int j=0; j<N; j++)
                EE[i][j]=false;
        
        E.clear();
        for (int i=0; i<M; i++) {
            int a, b; char tmp;
            cin>>a>>tmp>>b;
            E.push_back(Edge(a, b));
            E.push_back(Edge(b, a));
            EE[a][b]=true;
            EE[b][a]=true;
        }
        
        sort(E.begin(), E.end());
        
        D.clear();
        D.resize(N, numeric_limits<int>::max());
        D[0] = 0;
        
        X.clear();
        X.resize(E.size(), 0);
        
        
        int resultX = 0;
        
        queue<int> q;
        vector<bool> VIS(E.size(), false);            
        
        for (int i=0; i<int(E.size()); i++)
            if (E[i].first == 0) {
                q.push(i);
                VIS[i]=true;
                
                X[i] = countNeighbours(E[i].first, E[i].second);
                
                D[E[i].second] = 1;
                
                if (E[i].second==1)
                    resultX = countNeighbours(0, 0);
            }
        
        
        if (D[1]!=1) {
            while (!q.empty()) {
                int e0ix = q.front(); q.pop();
                Edge e0 = E[e0ix];
                
                int ix = lower_bound(E.begin(), E.end(), Edge(e0.second, -1)) - E.begin();
                for (; ix<int(E.size()) && E[ix].first == e0.second; ix++) {
                
                    int v = E[ix].second;
                    
                    D[v] = min(D[v], D[e0.second]+1);
                    if (D[v] != D[e0.second]+1)
                        continue;
                    
                    if (v==1)
                        resultX = max(resultX, X[e0ix]);
                    if (!VIS[ix])
                        q.push(ix), VIS[ix]=true;
                    
                    X[ix] = max(X[ix], X[e0ix] + countNewNeighb(e0.first, e0.second, v) - 1);
                }
            }
        }
        
        cout<<"Case #"<<z<<": "<<(D[1]-1)<<" "<<resultX<<endl;
        
    }
    
    return 0;
}
