#include<cstdio>
#include<string>
#include<cstring>
#include<memory>
#include<algorithm>
using namespace std;
#define FOR(i,a,b) for(int i = (a); i < (b); ++i)
#define SET(x, v) memset(x, v, sizeof(x))
char dat[128][128];
double ans[128];
double wp[128], owp[128], oowp[128];
int n;
int main() {
    int e = 0, T;
    scanf("%d",&T);
    while(T--) {
        scanf("%d",&n);
        FOR(i,0,n) {
            scanf(" %s",dat[i]);
        }
        FOR(i,0,n) {
            double p1, p2;
            p1 = 0., p2 = 0.;
            FOR(j,0,n)
                if(dat[i][j] == '1') p1++;
                else if(dat[i][j]=='0') p2++;
            wp[i] = p1 / (p1 + p2);
        }
        FOR(i,0,n) {
            double p1, p2;
            p1 = 0., p2 = 0.;
            FOR(j,0,n) {
                if(dat[i][j]=='.') continue;
                double p3 = 0., p4 = 0.;
                FOR(k,0,n) {
                    if(k==i) continue;
                    if(dat[j][k] == '1') p3++;
                    else if(dat[j][k] == '0') p4++;
                }
                double wp = p3 / (p3+p4);
                p1 += wp, p2 += 1.0;
            }
            owp[i] = p1 / p2;
        }
        FOR(i,0,n) {
            double p1, p2;
            p1 = 0., p2 = 0.;
            FOR(j,0,n)
                if(dat[i][j]!='.') p1+= owp[j], p2+=1.;
            oowp[i] = p1 / p2;

        }
        printf("Case #%d:\n", ++e);
        FOR(i,0,n) {
            printf("%.20lf\n", wp[i]*0.25 + 0.5*owp[i] + 0.25*oowp[i]);
        }
    }
    return 0;
}
