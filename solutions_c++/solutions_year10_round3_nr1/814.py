#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

inline int get(void) {
    int x;
    scanf("%d\n", &x);
    return x;
}

const int MAXN = 1000+3;

typedef pair<int, int> line;

void solve(int t) {
    int n = get();
    line lines[MAXN];
    for (int i = 0; i < n; i++) {
        lines[i].first = get();
        lines[i].second = get();
    }

    int res = 0;

    for (int i = 0; i < n; i++) {
        // count all the lines with a higher first and lower second or
        // higher second and lower first
        for (int j = 0; j < n; j++) {
            if ( (lines[j].first > lines[i].first && lines[j].second < lines[i].second) ||
                 (lines[j].first < lines[i].first && lines[j].second > lines[i].second) ) {
                res++;
            }
        }
    }
///    sort(lines, lines + n);

    printf("Case #%d: ", t);
    // each will be double counted
    printf("%d", res/2);
    printf("\n");
}

int main(void) {
    int tests = get();
    for (int t = 1; t <= tests; t++) {
        solve(t);
    }
    return 0;
}
