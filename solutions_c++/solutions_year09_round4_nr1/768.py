#include <cstdio>
#include <cstring>
#include <climits>
#include <algorithm>

using namespace std;

int t, n, pos[50];
char a[50][50];

void solve();

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i)
        solve();
    return 0;
}

void solve() {
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
        scanf("%s", a[i]);
        pos[i] = 0;
        for (int j = 0; j < n; ++j)
            if (a[i][j] == '1')
                pos[i] = j;
    }
    int ans = 0;
    for (int i = 0; i < n; ++i) {
        if (pos[i] > i) {
            for (int j = i + 1; j < n; ++j)
                if (pos[j] <= i) {
                    for (int k = j; k > i; --k) {
                        swap(pos[k], pos[k - 1]);
                        ++ans;
                    }
                    break;
                }
        }
    }
    printf("Case #%d: %d\n", ++t, ans);
}
