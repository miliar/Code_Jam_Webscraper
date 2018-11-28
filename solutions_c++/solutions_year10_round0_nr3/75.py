#include <cstdio>
#include <iostream>

using namespace std;

int g[1005];
int Next[1005];
int Hash[1005];
long long Ride[1005];
long long Take[10005];
long long Ans, Total;

int main() {
    freopen("C-large.in", "r", stdin);
    int T, R, k, N, cnt;
    int test = 1;

    for(scanf("%d", &T); T; T --) {
        scanf("%d%d%d", &R, &k, &N);
        for(int i = 0; i < N; i ++)
            scanf("%d", &g[i]);
        for(int i = 0; i < N; i ++) {
            Total = 0;
            for(int j = i; ; j = (j + 1) % N) {
                Total += g[j];
                if(Total + g[(j + 1) % N] > (long long)k || (j + 1) % N == i) {
                    Next[i] = j;
                    break;
                }
            }
            Ride[i] = Total;
        }
        Ans = 0;
        memset(Hash, -1, sizeof(Hash));
        int x = 0;
        for(cnt = 0; Hash[x] == -1; cnt ++) {
            Hash[x] = cnt;
            Take[cnt] = Ride[x];
            x = (Next[x] + 1) % N;
        }
        int len = cnt - Hash[x];
        for(int i = 0; i < Hash[x] && R > 0; i ++, R --)
            Ans += Take[i];
        if(R) {
            Total = 0;
            for(int i = Hash[x]; i < cnt; i ++)
                Total += Take[i];
            Ans += Total * (R / len);
            R %= len;
            for(int i = Hash[x], j = 0; j < R; i ++, j ++)
                Ans += Take[i];
        }
        cout << "Case #" << test ++ << ": " << Ans << endl;
    }
    return 0;
}

