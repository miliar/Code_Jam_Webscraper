#include <cstdio>
#include <algorithm>
#include <string>
using namespace std;

#define Fill(A, n) memset(A, n, sizeof(A))
string FILENAME = "A-large";

const int MAX_N = 100;

struct event {
    char w;
    int p, t;
} g[MAX_N + 1];

int main() {
    freopen((FILENAME + ".in").c_str(), "r", stdin);
    freopen((FILENAME + ".out").c_str(), "w", stdout);
    int T;
    scanf("%d", &T);
    for (int t = 0; t < T; t++) {
        int N;
        scanf("%d", &N);
        for (int i = 1; i <= N; i++) {
            while (scanf("%c", &g[i].w), !isalpha(g[i].w));
            scanf("%d", &g[i].p);
        }

        g[0].t = 0;
        g[0].p = 1;
        int LO = 0, LB = 0;
        for (int i = 1; i <= N; i++)
            if (g[i].w == 'O') {
                g[i].t = max(g[i - 1].t, g[LO].t + abs(g[i].p - g[LO].p)) + 1;
                LO = i;
            } else {
                g[i].t = max(g[i - 1].t, g[LB].t + abs(g[i].p - g[LB].p)) + 1;
                LB = i;
            }

        printf("Case #%d: %d\n", t + 1, g[N].t);
    }

}