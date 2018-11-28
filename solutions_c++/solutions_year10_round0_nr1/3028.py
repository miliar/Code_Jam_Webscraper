#include <cstdio>
#include <cstring>
#define maxn 30

int state[maxn];

void print_state(int n) {
    for (int i = 0; i < n; ++i) {
        printf("%d", state[i]);
    }
    puts("");
}

int main() {
    int t;
    scanf("%d", &t);
    for (int kase = 1; kase <= t; ++kase) {
        printf("Case #%d: ", kase);
        int n, k;
        scanf("%d%d", &n, &k);
        
        memset(state, 0, sizeof(state));
        int power = 0;
 //       print_state(n);
        for (int j = 0; j < k; ++j) {
            for (int i = 0; i < n; ++i) {
                if (i <= power) {
                    state[i] = 1 - state[i];
                }
            }
            power = -1;
            for (int i = 0; i < n; ++i) {
                if (state[i] == 0) {
                    power = i;
                    break;
                }
            }
            if (power == -1) {
                power = n - 1;
            }
//            print_state(n);
            //print_power(n);
        }
        if (power == n - 1 && state[n - 1]) puts("ON");
        else puts("OFF");

    }
    return 0;
}
