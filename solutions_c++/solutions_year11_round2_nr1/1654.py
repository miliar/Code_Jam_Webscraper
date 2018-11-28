#include <stdio.h>

char score[100][101];
double wp[100], owp[100], oowp[100], o[100], w[100];
int n;

int main() {
    int casos, i, j, num;

    scanf("%d", &casos);num=casos;
    for(;casos>0;casos--) {
        scanf("%d", &n);
        for(i=0;i<n;i++) {
            scanf("%s", score[i]);
            o[i] = 0;
            w[i] = 0;
            owp[i] = 0;
            oowp[i] = 0;
        }

        for(i=0;i<n;i++)
            for(j=0;j<n;j++) {
                if(score[i][j]=='0')
                    o[i]++;
                else if(score[i][j]=='1') {
                    o[i]++;
                    w[i]++;
                }
            }

        for(i=0;i<n;i++)
            for(j=0;j<n;j++) {
                if(score[i][j]=='0' && o[j]!=1)
                    owp[i] += (w[j]-1) / (o[j]-1);
                else if(score[i][j]=='1' && o[j]!=1)
                    owp[i] += w[j] / (o[j]-1);
            }

        for(i=0;i<n;i++)
            owp[i] = owp[i] / o[i];

        for(i=0;i<n;i++)
            for(j=0;j<n;j++) {
                if(score[i][j]!='.')
                    oowp[i] += owp[j];
            }



        printf("Case #%d:\n", num-casos+1);
        for(i=0;i<n;i++)
            if(o[i]!=0)
                printf("%.7lf\n",0.25*w[i]/o[i]  + 0.5*owp[i] + 0.25*oowp[i]/o[i]);
            else {
                printf("0\n");
            }




    }

    return 0;
}
