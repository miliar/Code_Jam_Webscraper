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

char a[52][52];
char ans[52][52];

int main() {
    
    int tests;
    scanf("%d\n", &tests);
    for (int test = 1; test <= tests; test++) {
        printf("Case #%d:\n", test);
        int n, m;
        scanf("%d%d\n", &n, &m);
        forn(i, n) gets(a[i]);
        memcpy(ans, a, sizeof a);
        bool shit = false;
        forn(i, n) forn(j, m) if (a[i][j] == '#') {
            if (i == n - 1 || j == m - 1 || a[i+1][j] != '#' || a[i][j+1] != '#' || a[i+1][j+1] != '#') {
                shit = true;
                break;
            }
            a[i][j] = a[i+1][j] = a[i][j+1] = a[i+1][j+1] = '.';
            ans[i][j] = ans[i+1][j+1] = '/';
            ans[i+1][j] = ans[i][j+1] = '\\';
        }
        if (shit) {
            printf("Impossible\n");
        } else {
            forn(i, n) {
                forn(j, m) printf("%c", ans[i][j]);
                printf("\n");
            }
        }
    }
    
    return 0;
}
