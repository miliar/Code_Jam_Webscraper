#include <cstdio>
#include <iostream>
#include <cstring>
#include <queue>
#include <algorithm>

using namespace std;

int main() {
    int t;
    scanf("%d", &t);

    for(int z = 1; z <= t; z++) {
        printf("Case #%d: ", z);

        int n;
        scanf("%d", &n);

        int d[n+1], l[n+1], D;
        for(int i = 0; i < n; i++)
            scanf("%d %d", &d[i], &l[i]);
        scanf("%d", &D);
        d[n] = D; l[n] = 0; n++;

        int best_height[n], visited[n];
        memset(best_height, -1, sizeof best_height);
        memset(visited, 0, sizeof visited);

        priority_queue<pair<int, int> > q;
        q.push(make_pair(best_height[0] = d[0], 0));

        while(!q.empty()) {
            int v = q.top().second; q.pop();
            if(visited[v]) continue; visited[v] = true;
            if(v == n-1) break;

            for(int i = 0; i < n; i++)
                if(best_height[v] >= abs(d[v] - d[i])) {
                    int height = min(l[i], abs(d[v] - d[i]));
                    if(height > best_height[i])
                        q.push(make_pair(best_height[i] = height, i));
                }
        }

        if(best_height[n-1] != -1)
            printf("YES\n");
        else
            printf("NO\n");
    }
}
