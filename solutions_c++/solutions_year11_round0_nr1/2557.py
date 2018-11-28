#include <stdio.h>
#include <queue>

using namespace std;

int main() {
    int tests;
    scanf("%d", &tests);
    for (int test = 1; test <= tests; test++) {
        int n;
        scanf("%d", &n);
        queue <int> Q[2];
        int N[n];
        for (int i = 0; i < n; i++) {
            char c;
            scanf(" %c", &c);
            c = (c == 'O' ? 0 : 1);
            int d;
            scanf("%d", &d);
            Q[c].push(d-1);
            N[i] = c;
        }
        int t = 0;
        int p[2] = { 0, 0 };
        for (int got = 0; got < n; t++) {
            int go = 0;
            for (int g = 0; g < 2; g++) {
                if (!Q[g].empty()) {
                    int next = Q[g].front();
                    if (next > p[g]) {
                        p[g]++;
                    } else if (next < p[g]) {
                        p[g]--;
                    } else if (N[got] == g) {
                        Q[g].pop();
                        go = 1;
                    }
                }
            }
            if (go) {
                got++;
            }
        }
        printf("Case #%d: %d\n", test, t);
    }
    return 0;
}

