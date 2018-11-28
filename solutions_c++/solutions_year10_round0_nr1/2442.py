#include <cstdio>
#include <cstdlib>

using namespace std;

int main(int argc, char *argv[]) {
    freopen("A-large.in", "r", stdin);
    freopen("Output.txt", "w", stdout);
    int T, N, K;
    int x;
    scanf("%d", &T);
    for(int i=0; i<T; ++i) {
        scanf("%d %d", &N, &K);
        x = (1 << N) - 1;
        if((x & K) == x) {
            printf("Case #%d: ON\n", i+1);
        }else {
            printf("Case #%d: OFF\n", i+1);
        }
    }
    return EXIT_SUCCESS;
}
