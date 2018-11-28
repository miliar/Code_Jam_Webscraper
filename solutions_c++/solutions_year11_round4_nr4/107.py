#include <iostream>
#include <vector>
#include <map>
#include <list>
#include <algorithm>
#include <string>
#include <cmath>

#define D(x) x

using namespace std;

template<typename T>
ostream& operator <<(ostream& os, vector<T> v) {
    os << "[";
    for (int i = 0; i < v.size(); i++) {
        if (i > 0) os << ", ";
        os << v[i];
    }
    os << "]";
    return os;
}

typedef unsigned long long uint64_t;

int dfs(int node, const vector<vector<int> >& adj, int depth, vector<bool>& visited, uint64_t threatened) {
    if (depth == 0) {
        if (node == 1) {
            int count = 0;
            for (int i = 1; i < adj.size(); i++) {
                if (threatened & (1LLU << i)) count++;
            }
//            for (int i = 0; i < depth; i++) cout << "  ";
//            cout << count << endl;
            return count;
        } else return -1;
    }

//    for (int i = 0; i < depth; i++) cout << "  ";
//    cout << node << endl;

    if (visited[node]) return -1;
    visited[node] = true;

    for (int i = 0; i < adj[node].size(); i++) {
        threatened |= (1LLU << adj[node][i]);
    }

    int best = -1;
    for (int i = 0; i < adj[node].size(); i++) {
        int result = dfs(adj[node][i], adj, depth-1, visited, threatened);
        best = max(result, best);
    }
    visited[node] = false;

    return best;    
}

int main() {
    int T;

    cin >> T;
    for (int testCase = 1; testCase <= T; testCase++) {
        int P, W;
        cin >> P >> W;

        vector<vector<int> > adj(P);
        for (int i = 0; i < W; i++) {
            int xi, yi;
            char comma;
            cin >> xi >> comma >> yi;
            adj[xi].push_back(yi);
            adj[yi].push_back(xi);
        }

        // BFS to find path length
        const int start=0, end=1;

        int depth = 0;
        vector<int> current, next;
        current.push_back(0);
        vector<bool> visited(P);
        bool found = false;

        while (!current.empty()) {
            for (int i = 0; i < current.size(); i++) {
                int c = current[i];
                if (c == 1) {
                    found = true;
                    break;
                }

                for (int j = 0; j < adj[c].size(); j++) {
                    int d = adj[c][j];
                    if (visited[d]) continue;
                    visited[d] = true;
                    next.push_back(d);
                }
            }
            if (found) break;

            depth++;
            swap(current, next);
            next.clear();
        }
        depth--;

        visited = vector<bool>(P);
        int max = dfs(0, adj, depth+1, visited, 0);


        cout << "Case #" << testCase << ": " << depth << " " << max-depth << endl;
    }
}

