#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;


int main() {
    int t;
    scanf("%d", &t);
    for (int ti = 0; ti < t; ti++) {
        int n, s, p;
        scanf("%d%d%d", &n, &s, &p);
        int sure = 0, optional = 0;
        for (int i = 0; i < n; i++) {
            int total;
            scanf("%d", &total);
            int x = total / 3;
            if (x >= p) {
                sure++;
            }
            else if (x + 1 >= p) {
                if (total % 3 != 0) {
                    sure++;
                }
                else if (x > 0) {
                    optional++;
                }
            }
            else if (x + 2 >= p) {
                if (total % 3 == 2) {
                    optional++;
                }
            }
        }
        
        printf("Case #%d: %d\n", ti + 1, sure + min(s, optional));
    }
}