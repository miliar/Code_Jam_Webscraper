#include <cstdio>
#include <set>

using namespace std;

int main () {
    int T, L, t, N, C;
    int tab[100000];
    multiset<int> ms;
    multiset<int>::iterator it;
    long long time, result;
    
    scanf ("%d", &T);
    for (int st = 1; st <= T; ++st) {
        ms.clear ();
        result = 0;
        printf ("Case #%d: ", st);
        scanf ("%d %d %d %d", &L, &t, &N, &C);
        for (int c = 0; c < C; ++c) {
            scanf ("%d", tab + c);
            int k = 0;
            while (k * C + c < N) {
                tab[k * C + c] = tab[c];
                ++k;
                ms.insert (tab[c]);
            }
        }
        time = 0;
        int n;
        for (n = 0; n < N; ++n) {
            ms.erase (ms.find (tab[n]));
            if (time + tab[n] * 2 <= t) {
                time += tab[n] * 2;
            } else {
                tab[n] -= (t - time) / 2;
                ms.insert (tab[n]);
                time = t;
                break;
            }
        }
        for (; n < N; ++n) {
            time += tab[n] * 2;
        }
        while (L--) {
            it = --ms.end ();
            time -= *it;
            ms.erase (it);
        }
        printf ("%lld\n", time);
    }
    return 0;
}
