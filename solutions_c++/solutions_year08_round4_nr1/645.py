#include <iostream>
using namespace std;
#define out(x) printf("%s: %I64d\n", #x, (long long)(x))
const int maxint=0x7FFFFFFF;
template <class T> void get_max(T& a, const T &b) {b > a? a = b:1;}
template <class T> void get_min(T& a, const T &b) {b < a? a = b:1;}

int node[10010][2];
int tre[10010][2];
int n, v;

int dfs(int now){
    if (now > n / 2){
        tre[now][node[now][0]] = 0;
        return 0;
    }
    int l = now * 2;
    int r = now * 2 + 1;
    dfs(l);
    dfs(r);
    int v0, v1, v2, v3;
    v0 = min(min(tre[l][1] + tre[r][0], tre[l][0] + tre[r][1]) , tre[l][0] + tre[r][0]);
    v1 = tre[l][1] + tre[r][1];
    v2 = tre[l][0] + tre[r][0];
    v3 = min(min(tre[l][0] + tre[r][1], tre[l][1] + tre[r][0]) , tre[l][1] + tre[r][1]);
    if (node[now][0] == 1){
        tre[now][0] = v0;
        tre[now][1] = v1;
    }
    else{
        tre[now][0] = v2;
        tre[now][1] = v3;
    }
    if (node[now][1] == 1){
        if (node[now][0] == 1){
            get_min(tre[now][0], v2 + 1);
            get_min(tre[now][1], v3 + 1);
        }
        else{
            get_min(tre[now][0], v0 + 1);
            get_min(tre[now][1], v1 + 1);
        }
    }
    return 0;
}

int main() {
    int kase;
    freopen("a.out","w",stdout);
    scanf("%d", &kase);
    int cnt = 1;
    while(kase--){
        printf("Case #%d: ", cnt);
        cnt++;
        scanf("%d%d", &n, &v);
        for (int i = 1; i <= n / 2; ++i){
            scanf("%d%d", &node[i][0], &node[i][1]);
        }
        for (int i = n / 2 + 1; i <= n; ++i){
            scanf("%d", &node[i][0]);
        }
        for (int i = 1; i <= n; ++i){
            tre[i][0] = 10010;
            tre[i][1] = 10010;
        }
        dfs(1);
        if (tre[1][v] <= n)
            printf("%d\n", tre[1][v]);
        else
            printf("IMPOSSIBLE\n");
    }
    return 0;
}

