#include <stdio.h>
#include <vector>

char ary[110][110];
double wp[110];
double owp[110][110];
double rowp[110];
double oowp[110];
double pri[110];
int win[110];
int lose[110];

int main(int argc, const char *argv[]) {
    int t, n;
    scanf("%d", &t);
    int tt;
    for (tt = 1; tt <= t; tt++) {
        std::vector<int> pk[110];
        // input
        scanf("%d", &n);
        int i;
        for (i = 0; i < n; i++) {
            scanf("%s", ary[i]);
            int w, l;
            w = l = 0;
            int j;
            for (j = 0; j < n; j++) {
                if (ary[i][j] == '.')
                    continue;
                pk[i].push_back(j);
                if (ary[i][j] == '1')
                    w++;
                else
                    l++;
            }
            win[i] = w;
            lose[i] = l;
            wp[i] = (double)w/(w+l);
        }
        for (i = 0; i < n; i++) {
            int j;
            for (j = i; j < n; j++) {
                if (ary[i][j] == '.')
                    continue;
                if (ary[i][j] == '1') {
                    owp[i][j] = (double)(win[i]-1)/(win[i]+lose[i]-1);
                    owp[j][i] = (double)(win[j])/(win[j]+lose[j]-1);
                }
                else {
                    owp[i][j] = (double)(win[i])/(win[i]+lose[i]-1);
                    owp[j][i] = (double)(win[j]-1)/(win[j]+lose[j]-1);
                }
            }
        }
        for (i = 0; i < n; i++) {
            double sum = 0;
            int j;
            for (j = 0; j < pk[i].size(); j++) {
                sum += owp[pk[i][j]][i];
            }
            rowp[i] = sum/pk[i].size();
        }
        for (i = 0; i < n; i++) {
            double sum = 0;
            int j;
            for (j = 0; j < pk[i].size(); j++) {
                sum += rowp[pk[i][j]];
            }
            oowp[i] = sum/pk[i].size();
        }
        printf("Case #%d:\n", tt);
        for (i = 0; i < n; i++) {
            double ans = 0.25*wp[i]+0.5*rowp[i]+0.25*oowp[i];
            printf("%.8lf\n", ans);
        }
    }
    return 0;
}
