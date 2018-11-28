#include<stdio.h>
#include<math.h>
#include<string.h>
#include<iostream>
#include<algorithm>
using namespace std;
const int N = 110;
const int M = 2 * 10010;
const int inf = 1000000000;

struct Node
{
    int f, t;
}e[M];

int next[M], point[N], dis[N], q[N], pre[N], ne, s[N], flag;

void init()
{
    memset(point, -1, sizeof(point));
    ne = 0;
}

void add_edge(int f, int t)
{
    e[ne].f = f, e[ne].t = t, next[ne] = point[f], point[f] = ne++;
}

void dfs(int x, int fa){
    s[x]++;
    if(s[x] >= 2){
        flag = 1;
        return;
    }
    for(int i = point[x]; i != -1; i = next[i]){
        if(e[i].t == fa) continue;
        dfs(e[i].t, e[i].f);
    }
}

int main()
{
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int _, tt = 0;
    scanf("%d", &_);
    while(_--){
        tt++;
        int l = 0;
        int m, n, k;
        init();
        scanf("%d", &n);
        for(int i = 1; i <= n; i++){
            scanf("%d", &m);
            for(int j = 0; j < m; j++){
                scanf("%d", &k);
                add_edge(i, k);
            }
        }
        for(int i = 1; i <= n; i++){
            memset(s, 0, sizeof(s));
            flag = 0;
            dfs(i, -1);
//            for(int i = 1; i <= n; i++) printf("%d ", s[i]);
//            printf("\n");
            if(flag == 1) l = 1;
        }
        if(l == 1) printf("Case #%d: Yes\n", tt);
        else printf("Case #%d: No\n", tt);
    }

    return 0;
}
