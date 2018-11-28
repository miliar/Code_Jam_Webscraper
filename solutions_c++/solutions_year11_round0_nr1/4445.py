#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <map>
#include <set>
#include <string>
#include <vector>

using namespace std;

#define sz(a) ((int)((a).size()))
#define forn(i, n) for (int i = 0; i < (n); i++)
#define foreach(i, a) for (typeof((a).begin()) i = (a).begin(); i != (a).end(); ++i)
#define eprintf(...) {fprintf(stderr,__VA_ARGS__);fflush(stderr);}
typedef pair<int, int> ii;
typedef long long LL;

int a[102400], b[102400];
char tmp[102400];

int main() {
    int tests;
    scanf("%d", &tests);
    forn(test, tests) {
        int n;
        scanf("%d", &n);
        forn(i, n) {
            int x;
            scanf("%s %d", tmp, &x);
            a[i] = tmp[0] == 'B';
            b[i] = x;
        }
        int pos[] = {1, 1};
        int cur = a[0];
        int saved = 0;
        int ans = 0;
        for (int i = 0; i < n;) {
            int j = i + 1;
            while (j < n && a[j] == a[i]) j++;
            int move = abs(pos[cur] - b[i]) + 1;
            for (int k = i + 1; k < j; k++) {
                move += abs(b[k] - b[k - 1]) + 1;
            }
            move = max(move - min(saved, abs(pos[cur] - b[i])), 0);
            ans += move;
            saved = move;
            pos[cur] = b[j - 1];
            i = j;
            cur = !cur;
        }
        printf("Case #%d: %d\n", test + 1, ans);
    }
    return 0;
}
