/*
 * C. Theme Park
 */ 
#include <iostream>
#include <algorithm>
using namespace std;

#define MAXN 1000

long long C[MAXN];
int       L[MAXN];
int       g[MAXN];

long long T, R, N, k;

int main() {
    cin >> T;
    for (int t = 0; t < T; ++t) {
        cin >> R >> k >> N;
        for (int i = 0; i < N; ++i)
            cin >> g[i];

        fill(C, C + N, 0);
        fill(L, L + N, 0);

        bool crap = false, start = true;
        int  u = 0, v = 0;
        long long total = 0;

        while (R > 0) {
            if (start && L[v] != 0) {
                break;
            }

            if (C[u] + g[v] <= k && L[u] < N) {
                C[u] += g[v];
                L[u] += 1;

                total += g[v];
                v = (v+1)%N;
                start = false;
            } else {
                --R;

                u = v;
                start = true;
            }

            if (g[v] > k) {
                crap = true;
                break;
            }
        }

        if (!crap && R > 0) {
            long long value = 0;
            int len = 0;
            for (int i = 0, u = v; i == 0 || u != v; i++, u = (u+L[u])%N)
                value += C[u], len++;

            total += (R / len) * value;
            R = R % len;

            for (int i = 0, u = v; i < R; i++, u = (u+L[u])%N)
                total += C[u];
        }

        cout << "Case #" << t+1 << ": " << total << endl;
    }

    return 0;
}
