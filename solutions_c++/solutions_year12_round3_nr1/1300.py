#include <cstdio>
#include <vector>
using namespace std;

int n;
vector<int> graph[1010];
int count[1010];
bool found;

void visit(int v) {
    count[v]++;
    if (count[v] == 2) {
        found = 1;
        return;
    }
    vector<int>::iterator it;
    for (it = graph[v].begin(); !found && it != graph[v].end(); it++) {
        visit(*it);
    }
}

void dfs() {
    for (int i = 1; !found && i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            count[j] = 0;
        }
        visit(i);
    }
}

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d", &n);
        for (int i = 1; i <= n; i++) {
            graph[i].clear();
            count[i] = 0;
        }
        for (int i = 1; i <= n; i++) {
            int m;
            scanf("%d", &m);
            for (int j = 0; j < m; j++) {
                int x;
                scanf("%d", &x);
                //graph[i].push_back(x);
                graph[x].push_back(i);
            }
        }
        found = 0;
        dfs();
        if (found)
            printf("Case #%d: Yes\n", t);
        else
            printf("Case #%d: No\n", t);
    }
}
