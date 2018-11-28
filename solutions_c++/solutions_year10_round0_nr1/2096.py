// autor: Andrzej Pezarski
// GCJ2010
// Snapper Chain

#include <cstdio>
#include <cstdlib>

using namespace std;


int main() {
    int T, N, K;
    scanf("%d", &T);
    for (int t=1; t<=T; t++) {
        scanf("%d%d", &N, &K);
        printf("Case #%d: %s\n", t, (((1<<N)-1)&(K+1))?"OFF":"ON");
    }
    return 0;
}
