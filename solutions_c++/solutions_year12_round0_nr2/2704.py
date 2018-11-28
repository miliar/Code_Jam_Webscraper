// Fruit of Light
// FoL CC
// Orange Strawberry
// Som mudra, pekna a sikovna
// Sikovnejsia ako vcera

#include <algorithm>
#include <cstdio>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>

using namespace std;

#ifdef EBUG
#define DEBUG(x) cerr << "DEBUG (F " << __FUNCTION__ << ", L" << __LINE__ << "): " << #x << ": " << x << endl;
#define DPRINTF(args...) fprintf(stderr, "DEBUG: " args) // :P
#define DBG if (1)
#else 
#define DEBUG(x)
#define DPRINTF(args...)
#define DBG if (0)
#endif

#define FORRANGE(i, ma) for (int i = 0; i < (ma); i++)
#define FORRANGE1(i, ma) for (typeof(ma) i = 1; i <= (ma); i++)
#define FOREACH(it, data) for (typeof((data).begin()) it = (data).begin(); it != (data).end(); ++it)

typedef long long ll;

// ============================================================================

int main() {
    int T; scanf("%d", &T); FORRANGE1(t, T) {

        int N, S, p; scanf("%d%d%d", &N, &S, &p);

        int cnt = 0;
        FORRANGE(n, N) {
            int score; scanf("%d", &score);
            int bestns = score/3 + ( score%3 ? 1 : 0 );
            DEBUG(bestns);
            if (bestns >= p) cnt++;
            else if (S) {
                DPRINTF("trying S\n");
                score -= p; // assume he just made it
                if (score > 0 && score >= 2*(p-2)) { // the other 2 fit into the allowed
                    DPRINTF("  yep\n");
                    S--;
                    cnt++;
                }
            }
        }

        printf("Case #%d: ", t);
        printf("%d", cnt);
        printf("\n");
    }

    return 0;
}
