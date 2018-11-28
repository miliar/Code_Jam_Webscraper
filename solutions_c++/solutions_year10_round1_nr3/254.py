// autor: Andrzej Pezarski
// GCJ2010
// Number Game

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>

using namespace std;


char tab[100][100];


int main() {
    int T, A1, A2, B1, B2;
    scanf("%d", &T);
    for (int t=1; t<=T; t++) {
        scanf("%d%d%d%d", &A1, &A2, &B1, &B2);
        long long W=0;
        for (int A=A1; A<=A2; A++) {
            long double B = floor(A * ((sqrt(5.0)-1.0)/2.0));
            W += max(0, min(int(B), B2)-B1+1);
        }
        for (int B=B1; B<=B2; B++) {
            long double A = floor(B * ((sqrt(5.0)-1.0)/2.0));
            W += max(0, min(int(A), A2)-A1+1);
        }
        printf("Case #%d: %lld\n", t, W);
    }
    return 0;
}
