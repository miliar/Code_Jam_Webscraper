#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <queue>

using namespace std;

char tab[128][128];

double WP[128];
double OWP[128];
double OOWP[128];




int main() {
    int T;
    scanf("%d", &T);
    for (int t=1; t<=T; t++) {
        int N;
        scanf("%d", &N);
        for (int i=0; i<N; i++) {
            scanf("%s", tab[i]);
        }
        for (int i=0; i<N; i++) {
            int a=0, w=0;
            for (int j=0; j<N; j++) {
                if (tab[i][j]=='1') w++;
                if (tab[i][j]!='.') a++;
            }
            WP[i]=double(w)/double(a);
            OWP[i]=0;
            for (int j=0; j<N; j++) {
                if (tab[i][j]=='.') continue;
                int a2=0, w2=0;
                for (int k=0; k<N; k++) {
                    if (k==i) continue;
                    if (tab[j][k]=='.') continue;
                    if (tab[j][k]=='1') w2++;
                    if (tab[j][k]!='.') a2++;
                }
                OWP[i]+=double(w2)/double(a2);
            }
            OWP[i]/=double(a);
        }
        
        for (int i=0; i<N; i++) {
            int a=0;
            OOWP[i]=0;
            for (int j=0; j<N; j++) {
                if (tab[i][j]=='.') continue;
                if (tab[i][j]!='.') a++;
                OOWP[i]+=OWP[j];
            }
            OOWP[i]/=double(a);
        }
               
        
        printf("Case #%d:\n", t);
        for (int i=0; i<N; i++) {
//            printf("%lf %lf %lf\n", WP[i], OWP[i], OOWP[i]);
            printf("%.8lf\n", 0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i]);
        }
    }
    return 0;
}
