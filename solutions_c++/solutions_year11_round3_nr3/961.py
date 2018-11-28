#include <stdio.h>

typedef long long ll;

int T;
int N, L, H;
ll freqs[10000];

void solve(int caseno) {
    for (int i = L; i <= H; ++i) {
        bool win = true;
        for (int j = 0; j < N; ++j) {
            if (!((i%freqs[j] == 0) || (freqs[j]%i) == 0)) {
                win = false;
                break;
            }
        }
        if (win) {
            printf("Case #%d: %d\n",caseno,i);
            return;
        }
    }

    printf("Case #%d: NO\n",caseno);
}

int main() {
    scanf("%d",&T);
    for (int i = 0; i < T; ++i) {
        scanf("%d%d%d",&N,&L,&H);
        for (int j = 0; j < N; ++j) {
            scanf("%lld",freqs+j);
        }

        solve(i+1);
    }
    return 0;
}
