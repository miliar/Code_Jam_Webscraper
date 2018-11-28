
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <vector>
#define MAXN 1000008

using namespace std;

bool composite[MAXN];

void init() {
    for(int i = 2; i < MAXN; i++) {
        if(composite[i])
            continue;
        for(int j = 2 * i; j < MAXN; j += i)
            composite[j] = true;
    }
    /*
    for(int i = 2; i < 100; i++)
        if(!composite[i])
            printf("%d\n", i);
    */
}

long long solve() {
    long long N;
    cin >> N;

    if(N == 1)
        return 0;

    long long total = 0;
    for(long long i = 2; i * i <= N; i++) {
        if(composite[i])
            continue;

        long long prod = i * i;
        while(prod <= N) {
            prod *= i;
            total++;
            //cout << i << " " << total << endl;
        }
    }

    return total + 1;
}

int main() {
    init();

    int T;
    scanf("%d", &T);
    for(int i = 1; i <= T; i++) {
        cout << "Case #" << i << ": " << solve() << endl;
    }
}
