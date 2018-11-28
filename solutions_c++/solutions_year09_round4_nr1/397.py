#include <stdio.h>

const int maxn = 40 + 10;

int ord[maxn], lst[maxn], res, N;
char mxt[maxn][maxn];

void get_lst()
{
    for (int i = 1; i <= N; ++i) {
        lst[i] = N;
        while (lst[i]>0 && mxt[i][lst[i]]=='0') --lst[i];
    }
}

void p_swap(int x, int y)
{
    for (int i = y; i > x; --i) {
        int t = ord[i];
        ord[i] = ord[i-1];
        ord[i-1] = t;
    }       
}

void s_swap(int x, int y)
{
    for (int i = x; i < y; ++i) {
        int t = ord[i];
        ord[i] = ord[i+1];
        ord[i+1] = t;
    }
}

void search(int dep, int step)
{
    if (res!=-1 && res<=step) return;
    
    if (dep == N+1) {
        if (res==-1 || res>step) res = step;
        return;
    }
    
    for (int k = dep; k <= N; ++k)
        if (lst[ord[k]] <= dep) {
            p_swap(dep, k);
            search(dep+1, step+k-dep);
            s_swap(dep, k);
            return;
        }
}

int main(void)
{
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
    
    int tot;
    scanf("%d", &tot);
    for (int cas = 1; cas <= tot; ++cas) {
        printf("Case #%d: ", cas);
        scanf("%d", &N);
        for (int i = 1; i <= N; ++i) {
            scanf("%s", &mxt[i][1]);
            ord[i] = i;
        }
        get_lst();
        res = -1;
        search(1, 0);
        printf("%d\n", res);
    }
    return 0;
}
