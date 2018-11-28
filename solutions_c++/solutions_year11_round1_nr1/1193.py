#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <queue>

using namespace std;





int main() {
    int T;
    scanf("%d", &T);
    for (int t=1; t<=T; t++) {
        long long int N, Pd, Pg;
        scanf("%lld%lld%lld", &N, &Pd, &Pg);
        long long int D, G;
        D=100;
        if (Pd%5==0) {if (Pd%25==0) D/=25; else D/=5;}
        if (Pd%2==0) {if (Pd%4==0) D/=4; else D/=2;}
        G=100;
        if (Pg%5==0) {if (Pg%25==0) G/=25; else G/=5;}
        if (Pg%2==0) {if (Pg%4==0) G/=4; else G/=2;}
        long long int D1, G1;
        D1=Pd*(100/D);
        G1=Pg*(100/G);
        int k=1; 
        while (k<10010) {
            if (G*k>=D && G1*k>=D1) break;
            k++;
        }
        bool b=(D<=N && (Pd==100 || Pg!=100) && (Pd==0 || Pg!=0));
        printf("Case #%d: %s\n", t, b?"Possible":"Broken");
    }
    return 0;
}
