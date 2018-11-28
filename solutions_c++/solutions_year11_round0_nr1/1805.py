#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;
int n;
char s[10];
int main() {
    int cas;
    freopen("a.in", "r", stdin);
    freopen("b.txt", "w", stdout);
    scanf("%d" ,&cas);
    int o, b;
    int freeo, freeb;
    for (int ccas = 1; ccas <= cas; ++ccas) {
        o = 1, b = 1;
        freeo = 0, freeb = 0;
        scanf("%d", &n);
        int sum = 0;
        int pos;
        for (int j = 0; j < n; ++j) {
            scanf("%s", s);
            scanf("%d", &pos);
            if (s[0] == 'O') {
                int need = abs(pos - o) - freeo;
                if (need < 0) need = 0;
                ++need;
                sum += need;
                freeb += need;
                freeo = 0;    
                o = pos;
            } else {
                int need = abs(pos - b) - freeb;
                if (need < 0) need = 0;
                ++need;
                sum += need;
                freeo += need;
                freeb = 0;                
                b = pos;
            }
        }
        printf("Case #%d: %d\n", ccas, sum);
    }
    return 0;
}    
