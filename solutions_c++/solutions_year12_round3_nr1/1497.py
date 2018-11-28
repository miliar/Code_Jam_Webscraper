#include <cstdio>
#include <vector>
#include <queue>
using namespace std;

int main() {
    int t, n, m, x, visited[1010];
    vector<int> g[1010];
    queue<int> q;
    bool flag;
    
    scanf("%d", &t);
    for (int k = 1; k <= t; k++) {
        scanf("%d", &n);
        for (int i = 1; i <= n; i++) {
            g[i].clear();
        }
        
        for (int i = 1; i <= n; i++) {
            scanf("%d", &m);
            for (int j = 1; j <= m; j++) {
                scanf("%d", &x);
                g[i].push_back(x);
            }
        }
        
        flag = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                visited[j] = -1;
            }
            
            q.push(i);
            visited[i] = 0;
            while (!q.empty()) {
                x = q.front();
                q.pop();
                for (vector<int>::iterator it = g[x].begin(); it != g[x].end(); it++) {
                    q.push(*it);
                    if (visited[*it] == -1) {
                        visited[*it] = 0;
                    } else if (visited[*it] == 0) {
                        visited[*it] = 1;
                    }
                }
            }
            
            for (int j = 1; j <= n; j++) {
                if (visited[j] == 1) {
                    flag = 1;
                    break;
                }
            }
            if (flag) break;
        }
        
        if (flag) {
            printf("Case #%d: Yes\n", k);
        } else {
            printf("Case #%d: No\n", k);
        }
    }
}
