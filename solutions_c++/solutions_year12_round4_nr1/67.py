#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<string>
#include<cctype>
#include<climits>
#include<algorithm>
#include<complex>
#include<vector>
#include<queue>
#include<set>
#include<map>

using namespace std;

typedef long long LL;

const int MaxN = 10000 + 5;

int T, N;
int d[MaxN], l[MaxN], low[MaxN], FIN;

int main() {

    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);

    scanf("%d", &T);
    for (int te = 1; te <= T; ++te) {
        bool flag = false;
        scanf("%d", &N); 
        for (int i = 0; i < N; ++i) scanf("%d%d", d + i, l + i);
        scanf("%d", &FIN);
        memset(low, -1, sizeof(low));
        low[0] = d[0];
        for (int i = 0; i < N; ++i) if (low[i] != -1) {
            for (int j = i + 1; j < N; ++j) {
                if (d[i] + low[i] >= d[j]) {
                    if (l[j] >= d[j] - d[i]) low[j] = max(low[j], d[j] - d[i]);
                    else low[j] = max(low[j], l[j]);
                }
            }
            if (d[i] + low[i] >= FIN) {flag = true; break;}
        }
        printf("Case #%d: ", te);
        if (flag) puts("YES"); else puts("NO");
    }

    return 0;

}

