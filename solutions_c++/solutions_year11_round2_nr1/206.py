#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
#define rep(i, n) for(int i=0; i<(int)(n); i++)

int n, tbl[100][100];
double wp[100], owp[100], oowp[100];

int main() {
    int T;
    scanf("%d", &T);
    rep(_t, T) {
        memset(tbl, -1, sizeof(tbl));
        scanf("%d", &n);
        rep(i, n) rep(j, n) {
            char ch;
            scanf(" %c", &ch);
            if(ch!='.') tbl[i][j] = ch-'0';
        }
        rep(i, n) {
            int s=0, c=0;
            rep(j, n) if(tbl[i][j]!=-1) {
                if(tbl[i][j]) s++;
                c++;
            }
            wp[i] = (double)s/c;
        }
        rep(i, n) {
            int cnt = 0;
            double sum = 0;
            rep(j, n) if(tbl[i][j]!=-1) {
                int s=0, c=0;
                rep(k, n) if(tbl[j][k]!=-1 && k!=i) {
                    if(tbl[j][k]) s++;
                    c++;
                }
                sum += (double)s/c;
                cnt++;
            }
            owp[i] = sum/cnt;
        }
        rep(i, n) {
            int cnt = 0;
            double sum = 0;
            rep(j, n) if(tbl[i][j]!=-1) {
                sum += owp[j];
                cnt++;
            }
            oowp[i] = sum/cnt;
        }
        printf("Case #%d:\n", _t+1);
        rep(i, n) printf("%.8f\n", 0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
    }
    return 0;
}


