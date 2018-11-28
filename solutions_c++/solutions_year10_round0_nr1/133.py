#include <iostream>
using namespace std;

int main() {
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; ++i) {
        unsigned int n, k;
        scanf("%u%u", &n,&k);
        bool flag = (k & ((1 << n) - 1)) == (1 << n) - 1;
        printf("Case #%d: %s\n", i+1,  flag? "ON" : "OFF");
    }
    return 0;
}
