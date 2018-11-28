// Fruit of Light
// FoL CC
// Orange Strawberry
// Som mudra, pekna a sikovna
// Sikovnejsia ako vcera

#include <algorithm>
#include <cstdio>
#include <iostream>
#include <cstring>
#include <map>
#include <queue>
#include <set>
#include <tr1/unordered_set>
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

int numdigits(int N) {
    char buf[4247]; sprintf(buf, "%d", N); return strlen(buf);
}
int numzeroes(int N) {
    int cnt = 0;
    char buf[4247]; sprintf(buf, "%d", N);
    FORRANGE(i, strlen(buf)) cnt += ( buf[i] == '0' ? 1 : 0 );
    return cnt;
}

void bufrotate(char* buf) {
    int len = strlen(buf);
    char last = *(buf+len-1);
    for (int i = len-1; i > 0; i--) buf[i] = buf[i-1];
    buf[0] = last;
}

int main() {
    int T; scanf("%d", &T); FORRANGE1(t, T) {
        int A, B; scanf("%d%d", &A, &B);
        set<pair<int, int> > S;
        for (int n = A; n <= B; n++) {
            DEBUG(n);
            char buf[4247]; sprintf(buf, "%d", n);
            for (int i = 1; i < numdigits(n); i++) {
                bufrotate(buf);
                DPRINTF(" - %s\t", buf);
                if (buf[0] == '0') { DPRINTF(" leading 0\n"); continue; }
                int x; sscanf(buf, "%d", &x);
                if (x < A || x > B) { DPRINTF(" out of range\n"); continue; }
                if (x == n) { DPRINTF(" same\n"); continue; }
                DPRINTF("\n");

                S.insert( n > x ? make_pair(x,n) : make_pair(n,x) );
            }
        }

        printf("Case #%d: ", t);
        printf("%d", S.size());
        printf("\n");
    }

    return 0;
}
