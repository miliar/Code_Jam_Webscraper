#include <cstdio>
#include <queue>
using namespace std;

struct foo {
    int cur, dist, prev;
    foo(int c, int d, int p)
        : cur(c), dist(d), prev(p) { }
};

bool seen[10010][10010];

// GCJ | 2012 | Round 2 | Q1
int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    
    int testCases;
    scanf("%d", &testCases);
    for (int testNum = 1; testNum <= testCases; testNum++) {
        int vines, dist[10010], len[10010], aimDist;
        bool possible = false;
        scanf("%d", &vines);
        for (int i = 0; i < vines; i++)
            scanf("%d%d", &dist[i], &len[i]);
        scanf("%d", &aimDist);

        for (int i = 0; i < 10010; i++)
            for (int j = 0; j < 10010; j++)
                seen[i][j] = false;

        queue<foo> q;
        q.push(foo(0, dist[0], 0));
        while (!q.empty()) {
            foo cur = q.front();
            q.pop();

            if (seen[cur.cur][cur.prev]) continue;
            seen[cur.cur][cur.prev] = true;

            if (dist[cur.cur] + cur.dist >= aimDist) {
                possible = true;
                break;
            }

            for (int i = cur.cur + 1; i < vines && dist[i] <= dist[cur.cur] + cur.dist; i++) {
                if (len[i] < dist[i] - dist[cur.cur]) q.push(foo(i, len[i], cur.cur));
                else q.push(foo(i, dist[i] - dist[cur.cur], cur.cur));
            }
        }

        printf("Case #%d: ", testNum);
        printf("%s", possible ? "YES" : "NO");
        printf("\n");
    }
}

