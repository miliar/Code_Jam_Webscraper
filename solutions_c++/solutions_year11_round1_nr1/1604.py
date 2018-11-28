#include<stdio.h>
#include<stdlib.h>
#include<string.h>
using namespace std;

int gcd(int x, int y) {
    return (!y)?x:gcd(y, x%y);
}

int t;
int n,d,g;
int main() {
    scanf(" %d", &t);
    for(int i=1;i<=t;i++) {
        scanf(" %d %d %d", &n, &d, &g);
        if(d>100 || g>100 || (d!=100 && g==100) || (d!=0 && g==0)) {
            printf("Case #%d: Broken\n", i);
            continue;
        }

        if(d == 0){
            printf("Case #%d: Possible\n", i);
            continue;
        }

        int tmp = gcd(100, d);
        int min = 100/tmp;
        if(min <= n){
            printf("Case #%d: Possible\n", i);
        } else {
            printf("Case #%d: Broken\n", i);
        }
    }
    return 0;
}

