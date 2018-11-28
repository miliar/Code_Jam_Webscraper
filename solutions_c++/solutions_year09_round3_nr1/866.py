#include <cstdio>
#include <cstring>

void solve(){
    char lin[1024];
    int cif[256], val[256];
    memset(val, -1, sizeof(val));
    bool mark[256];
    memset(mark, 0, sizeof(mark));
    scanf("%s\n", lin);
    int n = strlen(lin);
    mark[lin[0]] = true;
    cif[lin[0]] = 1;
    val[1] = lin[0];
    int base = 2;
    for (int i=1; i<n; i++)
        if (!mark[lin[i]]){
            int k = 0;
            while (val[k] != -1)
                k++;
            mark[lin[i]] = true;
            val[k] = lin[i];
            cif[lin[i]] = k;
            if (k + 1 > base)
                base = k + 1;
        }
    long long sol = 0;
    for (int i=0; i<n; i++)
        sol = sol * base + cif[lin[i]];
    printf("%I64d\n", sol);
}

int main(){
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
    int tst;
    scanf("%d\n", &tst);
    for (int i=1; i<=tst; i++){
        printf("Case #%d: ", i);
        solve();
    }
}
