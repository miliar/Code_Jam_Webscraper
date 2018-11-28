#include <stdio.h>
#include <vector>

using namespace std;

vector<int> primes;

struct Factorization {
    vector<int> times;
};

vector<Factorization> factors;

int count (int num, int prime) {
    int ret = 0;
    while (num % prime == 0) {
        ++ret;
        num /= prime;
    }
    return ret;
}

int sieve() {
    bool isPrime[1000];
    for (int i = 0; i < 1000; ++i) isPrime[i] = true;
    for (int i = 2; i < 1000; ++i) {
        if (!isPrime[i]) continue;
        primes.push_back(i);
        for (int j = i; j <= 1000; ++j) {
            if (j % i == 0) {
                factors[j].times.push_back(count(j, i));
                isPrime[j] = false;
            } else {
                factors[j].times.push_back(0);
            }
        }
    }
}

int main(void) {
    factors.push_back(Factorization());
    for (int i = 1; i <= 1000; ++i) {
        factors.push_back(Factorization());
    }

    sieve();

    int nC;
    scanf("%d", &nC);
    for (int cC = 0; cC < nC; ++cC) {
        int N;
        scanf("%d", &N);

        int ans = 0;
        if (N != 1) {
            int badCount = 1;
            int inRoom[primes.size()];

            vector<bool> outside;
            outside.resize(N + 1, true);
            for (int i = 0; i < primes.size(); ++i) inRoom[i] = 0;
            for (int i = 2; i <= N; ++i) {
                int minIncr = 10000000;
                int minN = -1;
                for (int j = 2; j <= N; ++j) {
                    if (!outside[j]) continue;
                    int diff = 0;
                    for (int primeC = 0; primeC < primes.size(); ++primeC) {
                        if (primeC < factors[j].times.size() &&
                            inRoom[primeC] < factors[j].times[primeC]) {
                            diff += factors[j].times[primeC] - inRoom[primeC];
                            break;
                        }
                    }
                    if (!diff) outside[j] = false;
                    else if (diff < minIncr) {
                        minIncr = diff;
                        minN = j;
                    }
                }
                if (minN == -1) break;
                badCount++;
                //printf("%d ", minN);
                for (int primeC = 0; primeC < primes.size(); ++primeC) {
                    if (primeC < factors[minN].times.size() &&
                        inRoom[primeC] < factors[minN].times[primeC])
                        inRoom[primeC] = factors[minN].times[primeC];
                }
                outside[minN] = false;
            }
            //printf("\n");

            int bestCount = 0;
            for (int i = 0; i <= N; ++i) outside[i] = true;
            for (int i = 0; i < primes.size(); ++i) inRoom[i] = 0;
            for (int i = 2; i <= N; ++i) {
                int maxIncr = 0;
                int maxN = -1;
                for (int j = 2; j <= N; ++j) {
                    if (!outside[j]) continue;
                    int diff = 0;
                    for (int primeC = 0; primeC < primes.size(); ++primeC) {
                        if (primeC < factors[j].times.size() &&
                            inRoom[primeC] < factors[j].times[primeC]) {
                            diff += factors[j].times[primeC] - inRoom[primeC];
                            break;
                        }
                    }
                    if (!diff) outside[j] = false;
                    else if (diff > maxIncr) {
                        maxIncr = diff;
                        maxN = j;
                    }
                }
                if (maxN == -1) break;
                bestCount++;
                //printf("%d ", maxN);
                for (int primeC = 0; primeC < primes.size(); ++primeC) {
                    if (primeC < factors[maxN].times.size() &&
                        inRoom[primeC] < factors[maxN].times[primeC])
                        inRoom[primeC] = factors[maxN].times[primeC];
                }
                outside[maxN] = false;
            }
            ans = badCount - bestCount;
            //printf("\n%d %d %d\n", N, badCount, bestCount);
        }
        printf("Case #%d: %d\n", cC + 1, ans);
    }
    return 0;
}
