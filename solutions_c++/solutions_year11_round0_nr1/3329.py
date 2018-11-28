#include <cstdio>
#include <cmath>
#include <queue>
using namespace std;

int abs(int f) {
        if (f > 0) return f;
        else return -f;
}


int main() {
        int i;        
        int n, t;
        scanf("%d", &t);
        for (int T = 1; T <= t; T++) {
                int total = 0;
                int pos[255];
                int last[255];
                pos['O'] = pos['B'] = 1;
                last['O'] = last['B'] = 0;
                int b;
                char a;

                scanf("%d", &n);
                for (i = 0; i < n; i++) {
                        scanf(" %c %d", &a, &b);
                        total += max(0, (int)abs(pos[a] - b) - (total - last[a])) + 1;
                        pos[a] = b;
                        last[a] = total;
                }
                printf("Case #%d: %d\n", T, total);
        }
        return 0;
}

