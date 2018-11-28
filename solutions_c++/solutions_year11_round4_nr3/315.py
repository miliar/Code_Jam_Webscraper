#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int prime[1000];
bool isPrime[1001];
int primes;
int best[1001];
int worst[1001];

bool isPrimePower(int what) {
    if (what == 1)
        return true;
    int i;
    for (i = 0; i < primes; i++) {
        if (what%prime[i] == 0) {
            while(what%prime[i] == 0)
                what/=prime[i];
            if (what == 1)
                return true;
            return false;
        }
    }
    return false;
}

int main() {
    int T, TT;
    scanf("%d", &TT);
    int i, j;
    for (i = 2; i < 1000; i++) {
        for (j = 0; j < primes; j++)
            if (i%prime[j] == 0)
                break;
        if (j == primes) {
            prime[j] = i;
            primes++;
            isPrime[i] = true;
        }
    }
    
    for (i = 1; i < 1001; i++) {
        best[i] = best[i-1] + isPrime[i];
    }
    best[1] = 1;
    for (i = 1; i < 1001; i++) {
        worst[i] = worst[i-1] + isPrimePower(i);
    }
    
    for (T = 1; T <= TT; T++) {
        int n;
        scanf("%d", &n);
        
        
        printf("Case #%d: %d\n", T, worst[n] - best[n]);
        
    }
}
