#include <iostream>
#include <cstdio>
#include <algorithm>
#include <queue>
#define INF 999999999
using namespace std;
typedef struct _tt {
    int s_time, e_time;
} TT;
TT tt[100];
int graph[200][200];
int tr, na, nb;
int get_augment_path(int s, int t)
{
    int min1;
    int i, j, k;
    int path[200];
    queue<int> q;
    q.push(s);
    memset(path, -1, sizeof(path));
    while (!q.empty() && path[t] == -1) {
        k = q.front();
        for (i = 0; i <= t; i++) {
            if (path[i] == -1 && graph[k][i] > 0) {
                path[i] = k;
                q.push(i);
            }
        }
        q.pop();
    }
    if (path[t] == -1)
        return 0;
    min1 = INF;
    j = t;
    for (i = path[j]; j != s; i = path[j = i]) {
        if (min1 > graph[i][j])
            min1 = graph[i][j];
    }
    j = t;
    for (i = path[j]; j != s; i = path[j = i]) {
        graph[i][j] -= min1;
        graph[j][i] += min1;
    }
    return min1;
}

int main()
{
    int tc, cn;
    int a, b, c;
    int i, j, k;
    int total;
    char buf[100];
    scanf("%d", &tc);
    for (cn = 1; cn <= tc; cn++) {
        scanf("%d", &tr);
        scanf("%d%d", &na, &nb);
        for (i = 1; i <= na+nb; i++) {
            scanf("%s", buf);
            sscanf(buf, "%d:%d", &a, &b);
            tt[i].s_time = a * 60 + b;
            scanf("%s", buf);
            sscanf(buf, "%d:%d", &a, &b);
            tt[i].e_time = a * 60 + b;
        }
        memset(graph, 0, sizeof(graph));
        for (i = 1; i <= na; i++) {
            for (j = na+1; j <= na+nb; j++) {
                if (tt[i].e_time + tr <= tt[j].s_time) {
                    graph[i][j] = 1;
                }
            }
        }
        for (i = 1; i <= na; i++) {
            graph[0][i] = 1;
        }
        for (i = na+1; i <= na+nb; i++) {
            graph[i][na+nb+1] = 1;
        }
        total = 0;
        while ((c = get_augment_path(0, na+nb+1)) > 0) {
            total += c;
        }
        a = total;
        memset(graph, 0, sizeof(graph));
        for (i = na+1; i <= na+nb; i++) {
            for (j = 1; j <= na; j++) {
                if (tt[i].e_time + tr <= tt[j].s_time) {
                    graph[i][j] = 1;
                }
            }
        }
        for (i = 1; i <= na; i++) {
            graph[i][na+nb+1] = 1;
        }
        for (i = na+1; i <= na+nb; i++) {
            graph[0][i] = 1;
        }
        total = 0;
        while ((c = get_augment_path(0, na+nb+1)) > 0) {
            total += c;
        }
        b = total;
        printf("Case #%d: %d %d\n", cn, na-b, nb-a);
    }
    return 0;
}
