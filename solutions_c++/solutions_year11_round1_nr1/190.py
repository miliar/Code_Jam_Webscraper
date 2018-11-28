#include<cstdio>

using namespace std;

#define lli long long int

int nwd(int a, int b) {
    if(a < b)
        return nwd(b, a);
    if(b == 0)
        return a;
    return nwd(b, a%b);
}

int main() {
    int zw;
    scanf("%d", &zw);
    for(int zz=1; zz<=zw; zz++) {
        printf("Case #%d: ", zz);
        lli n;
        int d, g;
        scanf("%lld%d%d", &n, &d, &g);
        if(g==100) {
            if(d!=100)
                printf("Broken\n");
            else
                printf("Possible\n");    
            continue;
        }
        if(g==0) {
            if(d!=0)
                printf("Broken\n");
            else
                printf("Possible\n");        
            continue;
        }
        d = 100 / nwd(d, 100);
//        printf("d %d n %lld\n", d, n);
        if(d > n) {
            printf("Broken\n");
            continue;
        }
        else {
            printf("Possible\n");
            continue;
        }         
    }
    return 0;
}
