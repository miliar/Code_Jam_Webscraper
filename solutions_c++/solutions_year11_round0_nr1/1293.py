#include <cstdio>
#include <algorithm>

using namespace std;

int main() {
    int T;
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
    
    scanf("%d", &T);
    for(int t = 1; t <= T; ++t) {
        int n, t1 = 0, c1 = 1, c2 = 1, t2 = 0, time = 0, x;
        char s[2];
        scanf("%d", &n);
        for(int i = 0; i < n; ++i) {
            scanf("%s%d", s, &x);
            if(s[0] == 'O') {
                t1 += abs(c1 - x) + 1;
                c1 = x;
                if(t1 <= time) {
                    t1 = ++time;
                } else {
                    time = t1;
                }
            } else {
                t2 += abs(c2 - x) + 1;
                c2 = x;
                if(t2 <= time) {
                    t2 = ++time;
                } else{
                    time = t2;
                }
            }
        }
        printf("Case #%d: %d\n", t, time);
    }
}

