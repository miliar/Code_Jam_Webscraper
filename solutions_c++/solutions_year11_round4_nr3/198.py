#include <algorithm>
#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

int main() {
    int t;
    scanf("%d", &t);
    for(int z = 1; z <= t; z++) {
        int n;
        scanf("%d", &n);

        if(n == 1) {
            printf("Case #%d: 0\n", z);
            continue;
        }

        vector<int> primes;
        for(int i = 2; i <= n; i++) {
            bool ok = true;
            for(int j = 2; j < i; j++)
                if(i % j == 0) {
                    ok = false;
                    break;
                }

            if(ok)
                primes.push_back(i);
        }

        int mini = primes.size(), maxi = 1;
        for(unsigned int i = 0; i < primes.size(); i++) {
            int pow = 1;
            while(pow <= n/primes[i]) { maxi++; pow *= primes[i]; }
        }

        printf("Case #%d: %d\n", z, maxi - mini);
    }
}
