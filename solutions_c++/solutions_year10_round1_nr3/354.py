#include <cstdio>
#include <cstring>
#include <cstdio>
#include <map>

#if 0
#define D(x...) fprintf(stderr, x)
#else
#define D(x...)
#endif

using namespace std;

typedef long long ll;

typedef pair<pair<int, int>, bool> state;

map<state, bool> winning_pos;

bool can_win(int A, int B, bool anna) {
    if (A == B) {
        return !anna;
    }
    if (A <= 0 || B <= 0) {
        return anna;
    }

    if (A > B) {
        int tmp = A;
        A = B;
        B = tmp;
    }

    /* A < B */
    if (B % A == 0) {
        return anna;
    }

    if (2*A > B) {
        return can_win(B-A, A, !anna);
    }

    return anna;
}

ll solve() {
    int A1, A2, B1, B2;
    scanf("%d%d%d%d", &A1, &A2, &B1, &B2);
    ll num_pos = 0;
    for (int ra = A1; ra <= A2; ra++) {
        for (int rb = B1; rb <= B2; rb++) {
            int a = ra;
            int b = rb;
            if (a > b) {
                int tmp = a;
                a = b;
                b = tmp;
            }
            num_pos += can_win(a, b, true) ? 1 : 0;
        }
    }
    // printf("%d %d => %s\n", A1, B1, num_pos ? "YES" : "NO");
    return num_pos;
}

int main() {
    int T;

    scanf("%d", &T);
    for (int i = 0; i < T; i++) {
        // solve();
        printf("Case #%d: %lld\n", i+1, solve());
        fflush(stdout);
    }
}
