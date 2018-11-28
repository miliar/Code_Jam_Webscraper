#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

int dv[1000001];
vector<long long> primes;
int set[1000001];

int findset(int x) {
    if (set[x] != x) {
        set[x] = findset(set[x]);
    }
    return set[x];
}

int main() {
    memset(dv, sizeof(dv), 0);
    for (int i = 2; i < 1000000; i ++) {
        if (dv[i] == 0) {
            primes.push_back(i);
            for (int j = i; j <= 1000000; j += i) {
                dv[j] += 1;
            }
        }
    }
    int C;
    scanf ("%d", &C);
    for (int c = 1; c <= C; c ++) {
        long long A, B, P;
        scanf("%I64d %I64d %I64d", &A, &B, &P);
        for (int i = 0; i <= B - A; i ++) {
            set[i] = i;
        }
        int res = B - A + 1;
        for (int i = 0; i < primes.size(); i ++) {
            long long p = primes[i];
            if (p >= P) {
                long long beg = A - 1 - ((A - 1) % p) + p;
                for (long long x = beg + p; x <= B; x += p) {
                    int s1 = findset(beg - A);
                    int s2 = findset(x - A);
                    if (s1 != s2) {
                        set[s2] = s1;
                        res -= 1;
                    } else {
                    }
                }
            }
        }
        printf("Case #%d: %d\n", c, res);
    }
    return 0;
}
