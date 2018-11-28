#include <cstdio>
#include <cstring>

#define min(a,b) (a < b ? a : b)

using namespace std;

int T, pd, pg,C=1;
long long int n;

int main() {

    for(scanf("%d",&T);T--;) {
        scanf("%lld %d %d",&n,&pd,&pg);
        bool blz=false;
        for (int d=1;d<=min(n,30000);d++)
            for (int g=d;g<=30000;g++) {
                //dah?
                if ((pd*d)%100 != 0) continue;
                if ((pg*g)%100 != 0) continue;
                if ((pg*g)/100 < (pd*d)/100) continue;
                int perdihj = d-(pd*d)/100;
                int perditot = g-(pg*g)/100;
                if (perdihj > perditot) continue;
                //printf("%d %d\n",d,g);
                blz = true;
                goto asd;
            }
        asd:;
        printf("Case #%d: %s\n",C++,blz?"Possible":"Broken");
    }

    return 0;
}
