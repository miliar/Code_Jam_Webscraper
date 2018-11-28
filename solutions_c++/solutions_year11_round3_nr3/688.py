#include <cstdlib>
#include <cstdio>
#include <set>

using namespace std;
int tab[10001];

bool czyPodzielne(int k, int N) {
    for (int i = 0; i < N; ++i)
        if (tab[i] % k != 0 && k % tab[i] != 0)
            return false;
    return true;
}

int main() {
    int t;
    scanf("%d", &t);

    for (int i = 1; i <= t; ++i) {

        int N, L, H;
        scanf("%d%d%d", &N, &L, &H);

        for (int j = 0; j < N; ++j) {
            scanf("%d", &tab[j]);
        }
        bool pasuje = true;
        int j;
        for (j = L; j <= H; ++j) {
            if (czyPodzielne(j, N) == true) {
                pasuje = true;
                break;
            } else {
                pasuje = false;
            }
        }

        if (pasuje == false)
            printf("Case #%d: NO\n", i);
        else
            printf("Case #%d: %d\n", i, j);
    }
    
    return 0;
}

