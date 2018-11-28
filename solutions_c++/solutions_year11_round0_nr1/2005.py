#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;

int t, n, b[101], xx, run, p[2], turn, tot, start;
char s[101][2];

void process(int x, int y) {
    if (abs(p[turn] - b[x]) <= run) {
        p[turn] = b[x];
    }
    else {
        p[turn] = b[x] - (abs(p[turn] - b[x]) - run);
    }
    run = 0;
    for (int i = x; i <= y; i++) {
        tot += abs(p[turn] - b[i]) + 1;
        run += abs(p[turn] - b[i]) + 1;
        p[turn] = b[i];
    }
}

int main() {
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d", &t);
    xx = 1;
    while (t--) {
        scanf("%d", &n);
        for (int i = 0; i < n; i++) {
            scanf("%s%d", s[i], &b[i]);
        }
        tot = 0;
        int i = 0;
        start = 0;
        turn = 0;
        run = 0;
        p[0] = p[1] = 1;
        for (; i < n;) {
            while (i + 1 < n && s[i + 1][0] == s[start][0]) i++;
            process(start, i);
            start = i + 1;
            i = i + 1;
            turn = 1 - turn;
        }
        printf("Case #%d: %d\n", xx++, tot);
    }
    return 0;
}
