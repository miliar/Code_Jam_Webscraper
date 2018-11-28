#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <map>
using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    scanf(" %d", &t);
    for (int i = 0; i < t; i++) {
        int n;
        scanf(" %d", &n);
        map<char, int> prev;
        prev['O'] = 1;
        prev['B'] = 1;
        map<char, int> prevt;
        prevt['O'] = 0;
        prevt['B'] = 0;
        char prev_r = 0;
        int ans = 0;
        for (int j = 0; j < n; j++) {
            char r;
            int p;
            scanf(" %c %d", &r, &p);
            /*if (!j || r == prev_r)
                ans += labs(prev[r] - p) + 1;
            else
                ans = max(ans, (int) labs(prev[r] - p)) + 1;*/
            ans += max(0, (int) labs(prev[r] - p) - (ans - prevt[r])) + 1;
            prev_r = r;
            prevt[r] = ans;
            prev[r] = p;
        }
        printf("Case #%d: %d\n", i + 1, ans);
    }
    return 0;
}