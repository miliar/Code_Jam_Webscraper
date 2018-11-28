#include <cstdio>

using namespace std;

int fact(int num, int prime, int max) {
    int ans = 1;
    while(num % prime == 0 && ans < max)
        ans *= prime, num /= prime;
    return ans;
}

int main() {
    int T;
    scanf("%d", &T);

    for(int z = 1; z <= T; z++) {
        printf("Case #%d: ", z);

        long long N;
        int Pd, Pg;
        scanf("%lld %d %d", &N, &Pd, &Pg);

        if(Pg == 0 || Pg == 100)
            printf(Pg == Pd ? "Possible\n" : "Broken\n");
        else if(4 / fact(Pd, 2, 4) * 25 / fact(Pd, 5, 25) <= N)
            printf("Possible\n");
        else
            printf("Broken\n");
    }
}
