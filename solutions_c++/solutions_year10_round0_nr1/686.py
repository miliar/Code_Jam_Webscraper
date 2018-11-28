#include <cstdio>
#include <cstring>

#define bint long long int

using namespace std;

bint T, n, k, C = 1;

int main() {

    scanf("%lld",&T);
    while (T--) {
        scanf("%lld %lld",&n,&k);
        printf("Case #%lld: %s\n",C++,((k+1) % (1ll << n)) == 0 ? "ON" : "OFF");
    }

    return 0;
}
