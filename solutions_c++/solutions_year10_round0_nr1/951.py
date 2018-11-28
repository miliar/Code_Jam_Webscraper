#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int t, n, k;
    freopen("/home/isilme/A-large.in", "r", stdin);
    freopen("/home/isilme/A.out", "w", stdout);
    while(cin >> t) {
        for(int i = 1; i <= t; i++) {
            cin >> n >> k;
            k %= 1 << n;
                printf("Case #%d: ", i);
            if(k + 1 == 1 << n) {
                printf("ON\n");
            } else {
                printf("OFF\n");
            }
        }
    }
    return 0;
}
