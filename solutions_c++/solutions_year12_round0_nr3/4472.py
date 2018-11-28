#include <cstdio>
#include <cmath>

using namespace std;

int rotr10(int n, int pot10);
int nlen(int n);

bool isrecycled(int n, int m) {
    int l = nlen(n);
    int pot10 = pow((double)10, l-1);
    for(int i = 0; i < l-1; ++i) {
        n = rotr10(n, pot10);
        if( n == m ) return true;
    }
    return false;
}
int rotr10(int n, int pot10) {
    int d = n % 10;
    n /= 10;
    n += d * pot10;
    return n;
}
int nlen(int n) {
    int sol = 0;
    while(n > 0) {
        ++sol;
        n /= 10;
    }
    return sol;
}

int main() {
    int t;
    scanf("%d", &t);
    for(int test = 0; test < t; ++test) {
        int A, B;
        scanf("%d %d", &A, &B);
        int sol = 0;
        for(int n = A; n < B; ++n) {
            for(int m = n+1; m <= B; ++m) {
                if(isrecycled(n, m)) ++sol;
            }
        }
        printf("Case #%d: %d\n", test+1, sol);
    }
    return 0;
}
