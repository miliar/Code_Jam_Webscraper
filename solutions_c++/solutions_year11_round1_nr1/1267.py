#include <cstdio>
#include <cstring>

int main() {
    int nt;

    scanf(" %d",&nt);
    for (int ct=1; ct<=nt; ct++) {
        int d,g, t=100;
        long long n;
        bool res=true;
        scanf(" %lld%d%d",&n,&d,&g);

        if (g==100 && d!=100) res=false;
        else if (g==0 && d) res=false;
        else if (d) {
            for (int i=2; i<d; i++) {
                while (t%i==0 && d%i==0) {
                    d/=i;
                    t/=i;
                }
            }

            if (t>n) res=false;
        }

        printf("Case #%d: ",ct);
        if (res) printf("Possible\n");
        else printf("Broken\n");
    }
    return 0;
}
