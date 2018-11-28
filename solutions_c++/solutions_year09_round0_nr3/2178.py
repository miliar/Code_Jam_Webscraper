#include <cstdio>
#include <cstring>
#define MOD 10000

char msg[] = "welcome to code jam";
char text[1024];
int n, pos[555][30];

void solve(){
    memset(pos, 0, sizeof(pos));
    int sol = 0;
    int m = strlen(msg);
    gets(text);
    n = strlen(text);
    for (int i=0; i<n; i++){
        if (text[i] == msg[0])
            pos[i][0]++;
        for (int j=1; j<m; j++)
            if (text[i] == msg[j])
                for (int k=0; k<i; k++)
                    pos[i][j] = (pos[i][j] + pos[k][j-1]) % MOD;
        sol = (sol + pos[i][m-1]) % MOD;
    }
    printf("%.4d\n", sol);
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
