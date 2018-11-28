#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

long potencia[30];

long power(int n) {
    if (potencia[n] == 0) {
        potencia[n] = (power(n-1) << 1) | 1;
    }
    return potencia[n];
}

int main () {
    int t, N;
    long k;
    string res;

    scanf("%d", &t);
    memset(potencia, 0, sizeof(potencia));
    potencia[0] = 1;

    for (int i = 0; i < t; i++) {
        scanf("%d %ld", &N, &k);
        if ( k & 1 ) {
            if (power(N-1) <= k && k % (potencia[N-1] + 1) == potencia[N-1]) {
                res = "ON";
            }
            else {
                res = "OFF";
            }
        }
        else {
            res = "OFF";
        }
        printf("Case #%d: %s\n", i+1, res.c_str());
    }
    
}
