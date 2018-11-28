#include <stdio.h>

int wp[110][2];
double owp[110];
double oowp[110];

char str[110][110];

int main () {
    int kase, h = 1;
    freopen("A-large.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d", &kase);
    while ( kase-- ) {
          int n, i, j;
          scanf("%d", &n);
          for (i = 0; i < n; i++) {
              scanf("%s", str[i]);
          }
          printf("Case #%d:\n", h++);
          for (i = 0; i < n; i++) {
              wp[i][0] = 0; wp[i][1] = 0;
              for (j = 0; j < n; j++) {
                  if (str[i][j] == '0' ) {
                     wp[i][0]++;
                  }    
                  else if (str[i][j] == '1' ) {
                       wp[i][1]++;
                  }
              }
          }
          for (i = 0; i < n; i++) {
              double sum = 0;
              int m = 0;
              for (j = 0; j < n; j++) {
                  if (str[i][j] != '.') {
                     if (str[j][i] == '1')
                        sum += (wp[j][1]-1)*1.0/(wp[j][1]+wp[j][0]-1);
                     else 
                          sum += wp[j][1]*1.0/(wp[j][1]+wp[j][0]-1);
                     m++;
                  }
              }
              owp[i] = sum/m;
          }
          for (i = 0; i < n; i++) {
              double sum = 0;
              int m = 0;
              for (j = 0; j < n; j++) {
                  if (str[i][j] != '.') {
                     sum += owp[j];
                     m++;
                  }
              }
              oowp[i] = sum/m;
          }
          for (i = 0;i < n; i++) {
              printf("%.12f\n",0.25*wp[i][1]/(wp[i][0]+wp[i][1])+0.5*owp[i]+0.25*oowp[i]);
          }
    }
    return 0;
}
