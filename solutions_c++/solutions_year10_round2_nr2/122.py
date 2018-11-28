#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>

#include <iostream>
#include <algorithm>
#include <memory>
#include <string>
#include <vector>
#include <map>
#include <iostream>

#define TASK "b"
#define PB(x) push_back(x)
#define MP(x, y) make_pair(x, y)
#define CLR(x) memset(x, 0, sizeof(x))
#define forn(i, n) for (int i = 0; i < n; i++)

using namespace std;

typedef long long int64;
typedef long double ldouble;
typedef pair<int, int> pii;
typedef vector<int> vi;

const int INF = 0x3f3f3f3f;
const int64 INF64 = (int64)INF * (int64)INF;

const int MAXN = 100;

int n, k, b, t;
int x[MAXN], v[MAXN];

bool ok(int index) {
    return (int64) t * (int64) v[index] + x[index] >= (int64)b;
}

void sw(int i, int j) {
    swap(x[i], x[j]);
    swap(v[i], v[j]);
}

int main() {
    freopen(TASK ".in", "rt", stdin);
    freopen(TASK ".out", "wt", stdout);
    int C;
    scanf("%d", &C);
    forn(c, C) {
        scanf("%d%d%d%d", &n, &k, &b, &t);
        forn(i, n) scanf("%d", &x[i]);
        forn(i, n) scanf("%d", &v[i]);

        int done = 0, answer = 0;

        for (int i = 0; i < k; i++) {
            int index = n - 1 - i;
            while (index >= 0 && !ok(index)) index--;
            if (index == -1) break;
            for (int j = index; j + 1 <= n - 1 - i; j++) {
                sw(j, j + 1);
                answer++;
            }
            done++;
        }

        printf("Case #%d: ", c + 1);
        if (done < k) printf("IMPOSSIBLE\n");
        else printf("%d\n", answer);
    }

    return 0;
}
