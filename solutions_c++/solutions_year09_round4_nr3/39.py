/* Problema:
 * Fonte:
 * Palavra-chave: */

#include <set>
#include <map>
#include <list>
#include <queue>
#include <cmath>
#include <cstdio>
#include <vector>
#include <string>
#include <cctype>
#include <cassert>
#include <cstring>
#include <algorithm>
#include <functional>

#define rep(i, N) for(int i=0;i<(N);++i)
#define repd(i, N) for(int i=(N)-1;i>=0;--i)
#define rep3(i, j, N) for(int i=(j);i<(N);++i)
#define repd3(i, j, N) for(int i=(N)-1;i>=(j);--i)

using namespace std;

int T, N, K;

typedef long long ll;

struct stock_t {
    int price[100];
    bool operator<(const stock_t& s) const {
        return price[0] < s.price[0];
    }
};

#define MAX_VERTICES 300
#define MAX_EDGES 300

int grafo[MAX_VERTICES][MAX_EDGES];
int grau[MAX_VERTICES];
int match[MAX_VERTICES];
int visited[MAX_VERTICES];
int mark;

inline void clear_grafo() {
    memset(grau, 0, sizeof(grau));
}

inline void insert_edge(int u, int v) {
    grafo[u][grau[u]++] = v;
    grafo[v][grau[v]++] = u;
}

bool dfs(int v) {
    if(visited[v] == mark) return false;
    visited[v] = mark;
    for(int i=0;i<grau[v];++i) {
        int u = grafo[v][i];
        if(match[u]==-1 or dfs(match[u])) {
            match[v] = u;
            match[u] = v;
            return true;
        }
    }
    return false;
}

int max_matching(int N) {
    memset(visited, 0, sizeof(visited[0])*N);
    memset(match, -1, sizeof(match[0])*N);
    mark = 1;
    int total = 0;
    for(int i=0;i<N;++i) if(match[i] == -1) {
        if(dfs(i)) {
            ++total;
            ++mark;
        }
    }
    return total;
}


stock_t stocks[200];
int table[200];


int main(void) {

    scanf("%d", &T);
    for(int t=0;t<T;++t) {
        scanf("%d%d", &N, &K);
        for(int i=0;i<N;++i) {
            for(int j=0;j<K;++j) scanf("%d", stocks[i].price + j);
        }
        sort(stocks, stocks+N);
        memset(table, -1, sizeof(table));

        clear_grafo();
        for(int i=0;i<N;++i) {
            for(int j=i+1;j<N;++j) {
                bool fail = false;
                for(int k=0;k<K;++k) {
                    if(stocks[i].price[k] >= stocks[j].price[k]) {
                        fail =true;
                        break;
                    }
                }
                if(not fail) {
                    insert_edge(i*2, j*2+1);
                }
            }
        }

        int m = max_matching(N*2);

        int resp = N - m;
        printf("Case #%d: %d\n", t+1, resp);



    }


    return 0;
}
