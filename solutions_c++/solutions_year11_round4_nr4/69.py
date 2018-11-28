#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <complex> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <ctime> 
#include <cassert> 
using namespace std;

int getint()
{
    int ch, ret = 0;
    while (!isdigit(ch = getchar()));
    do {
        ret = ret * 10 + ch - '0';
    } while(isdigit(ch = getchar()));
    return ret;
}

vector<int> adj[512];

int n, m;

void bfs(int src, int dist[])
{
    for (int i = 0; i < n; i++)
        dist[i] = -1;
    dist[src] = 0;
    queue<int> Q;
    Q.push(src);
    while (!Q.empty()) {
        int p = Q.front();
        Q.pop();
        for (int i = 0; i < adj[p].size(); i++) {
            int q = adj[p][i];
            if (dist[q] == -1) {
                dist[q] = dist[p] + 1;
                Q.push(q);
            }
        }
    }
}

int d0[512], d1[512];

bool vis[512];

int len;
int ans;

void dfs(int p) 
{
    if (p == 1) {
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (!vis[i]) {
                bool found = false;
                for (int j = 0; j < adj[i].size(); j++) {
                    if (vis[adj[i][j]]) {
                        found = true;
                        break;
                    }
                }
                if (found)
                    count++;
            }
        }
        ans = max(ans, count);
    } else {
        vis[p] = true;
        for (int i = 0; i < adj[p].size(); i++) {
            int q = adj[p][i];
            if (d0[q] + d1[q] == len && d0[q] == d0[p] + 1) {
                dfs(q);
            }
        }
        vis[p] = false;
    }
}

int main()
{
    int T, cas = 0;
    T = getint();
    while (T--) {
        n = getint();
        m = getint();
        for (int i = 0; i < n; i++)
            adj[i].clear();
        for (int i = 0; i < m; i++) {
            int a = getint(), b = getint();
            adj[a].push_back(b);
            adj[b].push_back(a);
        }
        bfs(0, d0);
        bfs(1, d1);
        memset(vis, false, sizeof(vis));
        len = d1[0];
        ans = 0;
        dfs(0);
        printf("Case #%d: %d %d\n", ++cas, len - 1, ans);
    }
}
