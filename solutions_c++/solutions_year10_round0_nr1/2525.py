
#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);freopen("A-large.out", "w", stdout);
    long T;
    long N, K;
    long cnt = 0;
    long L;

    scanf("%ld", &T);
    while (T--) {
        scanf("%ld %ld", &N, &K);
        printf("Case #%ld: ", ++cnt);
        if (K%2) {
            L=(1<<N)-1;
            K &= L;
            if (K == L) puts("ON");
            else puts("OFF");
        } else
            puts("OFF");
    }

    return 0;
}
