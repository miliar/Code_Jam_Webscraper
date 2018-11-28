#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <queue>

using namespace std;

int P[256];
int V[256];

int C, D;



bool sprawdz(long long S) {
    long long last=-10000000000000ll;
    for (int i=0; i<C; i++) {
        last=max(last, P[i]-S);
        last+=(long long int)(D)*V[i];
        if (last-D>S+P[i]) return false;
    }
    return true;
}




int main() {
    int T;
    scanf("%d", &T);
    for (int t=1; t<=T; t++) {
        scanf("%d%d", &C, &D);
        D*=2;
        for (int i=0; i<C; i++) {
            scanf("%d%d", P+i, V+i);
            P[i]*=2;
        }
        long long int l=0, r=10000000000000ll;
        while (l!=r) {
            long long int s=(l+r)/2;
            if (!sprawdz(s)) l=s+1;
            else r=s;
        }
        
        printf("Case #%d: %lld.%lld\n", t, l/2, 5*(l%2));
    }
    return 0;
}
