#include <iostream>
#include <set>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <map>
#include <vector>

using namespace std;

const int N = 1000;
char str[N][N];
double WP[N], OWP[N], OOWP[N], res[N];

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for (int i = 1; i <= t; ++i) {
        printf("Case #%d:\n",i);
        int n;
        scanf("%d",&n);
        for (int j = 0; j < n; ++j) {
            scanf("%s",str[j]);
        }
        memset(WP, 0, sizeof(WP));
        memset(OWP, 0, sizeof(OWP));
        memset(OOWP, 0, sizeof(OOWP));
        
        for (int j = 0; j < n; ++j) {
            int win = 0;
            int tot = 0;
            for (int k = 0; k < n; ++k) {
                if (str[j][k] == '1') win++;
                if (str[j][k] != '.') tot++;
            }
            WP[j] = 1.0 * win / tot;
            //printf("%d : %lf\n",j, WP[j]);
        }
        
        
        for (int j = 0; j < n; ++j) {
            int total = 0;
            double ret = 0;
            
            for (int k = 0; k < n; ++k) {
                if (k != j && (str[j][k] != '.')) {
                   int win = 0;
                   int tot = 0;
                   total++;
                   for (int p = 0; p < n; ++p) {
                       if (p != j) {
                          if (str[k][p] == '1') win++;
                          if (str[k][p] != '.') tot++;
                       }
                   }
                   ret += 1.0 * win / tot;
                }
            }
            ret /= total;
            OWP[j] = ret;
            //printf("%d : %d %lf\n",j, total, OWP[j]);
        }
        
        for (int j = 0; j < n; ++j) {
            double ret = 0;
            int tot = 0;
            for (int k = 0; k < n; ++k) {
                if (str[j][k] != '.') {
                   tot++;
                   ret += OWP[k];
                }
            }
            OOWP[j] = ret / tot;
        }
        
        for (int j = 0; j < n; ++j) {
            res[j] = 0.25 * WP[j] + 0.50 * OWP[j] + 0.25 * OOWP[j];
            printf("%.6lf\n",res[j]);
        }
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
