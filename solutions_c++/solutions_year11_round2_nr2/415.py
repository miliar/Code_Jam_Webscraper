#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int p[210], q[210];

int main() {
    int nt;

    scanf("%d",&nt);
    for (int ct=1; ct<=nt; ct++) {
        int d,c;
        scanf(" %d %d",&c,&d);

        for (int i=0; i<c; i++)
            scanf(" %d %d",&p[i], &q[i]);

        double es=0, di=1E20, me;

        while (di-es>1E-8) {
            bool deu=true;
            double acc=-1E20;
            me=(es+di)/2;

            for (int i=0; i<c; i++) {
                acc=max(acc, p[i]-me-d);
                for (int j=0; j<q[i]; j++) {
                    if (acc+d > p[i]+me) {
                        deu=false;
                        break;
                    }
                    acc+=d;
                }
                
                if (!deu) break;
            }

            if (deu) di=me;
            else es=me;
        }

        printf("Case #%d: %.8lf\n",ct, es);
    }

    return 0;
}
