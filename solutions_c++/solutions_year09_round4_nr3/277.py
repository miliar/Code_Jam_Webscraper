#include <cmath>
#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;

const int INF = 1000000000;

struct MinCostMaxFlow {
    int N;
    VVI cap, flow, cost;
    VI found, dad, dist, pi;  
    
    bool search(int source, int sink) {
        fill(found.begin(), found.end(), false);
        fill(dist.begin(), dist.end(), INF);
        dist[source] = 0;
        
        while (source != N) {
            int best = N;
            found[source] = true;
            for (int k = 0; k < N; k++) {
                if (found[k]) continue;
                if (flow[k][source]) {
                    int val = dist[source] + pi[source] - pi[k] - cost[k][source];
                    if (dist[k] > val) {
                        dist[k] = val;
                        dad[k] = source;
                    }
                }
                if (flow[source][k] < cap[source][k]) {
                    int val = dist[source] + pi[source] - pi[k] + cost[source][k];
                    if (dist[k] > val) {
                        dist[k] = val;
                        dad[k] = source;
                    }
                }
                
                if (dist[k] < dist[best]) best = k;
            }
            source = best;
        }
        for (int k = 0; k < N; k++)
            pi[k] = min(pi[k] + dist[k], INF);
        return found[sink];
    }
    
    pair<int,int> getMaxFlow(const VVI &cap, const VVI &cost, int source, int sink) {
        this->cap = cap;
        this->cost = cost;
        
        N = cap.size();
        found = VI(N);
        flow = VVI(N,VI(N));
        dist = VI(N+1);
        dad = VI(N);
        pi = VI(N);
        
        int totflow = 0, totcost = 0;
        while (search(source, sink)) {
            int amt = INF;
            for (int x = sink; x != source; x = dad[x])
                amt = min(amt, flow[x][dad[x]] ? flow[x][dad[x]] :
                          cap[dad[x]][x] - flow[dad[x]][x]);
            for (int x = sink; x != source; x = dad[x]) {
                if (flow[x][dad[x]]) {
                    flow[x][dad[x]] -= amt;
                    totcost -= amt * cost[x][dad[x]];
                } else {
                    flow[dad[x]][x] += amt;
                    totcost += amt * cost[dad[x]][x];
                }
            }
            totflow += amt;
        }
        
        return make_pair(totflow, totcost);
    }
};

int main() {
  int numcases;
  cin >> numcases;
  for (int caseno = 1; caseno <= numcases; caseno++) {
    int n, k;
    cin >> n >> k;
    VVI v(n, VI(k));
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < k; j++) {
	cin >> v[i][j];
      }
    }
    sort(v.begin(), v.end());

    VVI cost(2*n+4, VI(2*n+4));
    VVI cap(2*n+4, VI(2*n+4));
    const int s = 2*n;
    const int t = 2*n+1;
    const int S = 2*n+2;
    const int T = 2*n+3;

    for (int i = 0; i < n; i++) {
      cap[2*i][2*i+1] = 1;
      for (int j = 0; j < n; j++) {
	cap[2*i+1][2*j] = 1;
	for (int p = 0; cap[2*i+1][2*j] && p < k; p++)
	  if (v[i][p] >= v[j][p]) cap[2*i+1][2*j] = 0;
      }
      cap[s][2*i] = 1;
      cap[2*i+1][t] = 1;
    }
    cap[t][s] = INF;
    cost[t][s] = 1;
    
    int demand = 0;
    for (int i = 0; i < n; i++) {
      cap[S][2*i+1] += 1;
      cap[2*i][T] += 1;
      cap[2*i][2*i+1] -= 1;
      demand += 1;
    }

    MinCostMaxFlow mcmf;
    pair<int,int> res = mcmf.getMaxFlow(cap, cost, S, T);
    
    cout << "Case #" << caseno << ": " << res.second << endl;
  }
}
