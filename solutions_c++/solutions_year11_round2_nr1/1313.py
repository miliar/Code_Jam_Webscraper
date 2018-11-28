#include <cstdio>

int main(){
    int T;

    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++){
        int n;
        char a[110][110];
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
            scanf("%s", a + i);
        double wp[110][2], owp[110][2], oowp[110];
        for (int i = 0; i < n; i++){
            double win = 0, sum = 0;
            for (int j = 0; j < n; j++){
                if (a[i][j] == '1') win++;
                if (a[i][j] != '.') sum++;
            }
            wp[i][0] = win;
            wp[i][1] = sum;
        }
        
        for (int i = 0; i < n; i++){
            double opp = 0, sum = 0;
            for (int j = 0; j < n; j++)
                if (a[i][j] != '.') {
                    opp++;
                    if (a[i][j] == '1')
                      sum += wp[j][0]/(wp[j][1]-1);
                    else sum += (wp[j][0]-1)/(wp[j][1]-1);
                }
            owp[i][0] = sum;
            owp[i][1] = opp;
        }
        for (int i = 0; i < n; i++){
            double opp = 0, sum = 0;
            for (int j = 0; j < n; j++)
                if (a[i][j] != '.'){
                    opp++;
                    sum += owp[j][0]/owp[j][1];
                }
            oowp[i] = sum/opp;
        }

        printf("Case #%d:\n", cas);
        for (int i = 0; i < n; i++)
            printf("%.7lf\n", 0.25*wp[i][0]/wp[i][1]
                    + 0.50*owp[i][0]/owp[i][1]
                    + 0.25*oowp[i]);
    }

    return 0;
}