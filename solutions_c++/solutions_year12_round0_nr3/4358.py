#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int N = 3000;
int T, a, b, s, d, l;
char c[10], r[10], t;
bool u[2000000+10], v[N+10][N+10];
int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C1.out", "w", stdout);
    scanf("%d", &T);
    for(int o=1; o<=T; o++) {
        s = 0;
        scanf("%d %d", &a, &b);
        for(int i=a; i<=b; i++)
            for(int j=a; j<=b; j++)
                v[i][j] = 0;
        for(int i=a; i<=b; i++) {
            sprintf(r, "%d", i);
            l = strlen(r);
            for(int j=1; j<l; j++) {
                for(int k=j; k<l; k++) c[k] = r[k-j];
                for(int k=0; k<j; k++) c[k] = r[k+l-j];
                c[l] = '\0';
                sscanf(c, "%d", &d);
                if(d != i && a <= d && d <= b && !v[i][d]) {
                    v[i][d] = v[d][i] = 1;
                    s++;
                }
            }
        }
        printf("Case #%d: %d\n", o, s);
    }
    return 0;
}
