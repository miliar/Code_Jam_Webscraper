#include <iostream>
#define N 115
using namespace std;
char A[N][N];
int Count[N];
int Won[N];
double wp[N];
int contor;
double owp[N];
double oowp[N];
int k;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("gcj.out","w",stdout);
    int tc;
    scanf("%d",&tc);
    while(tc) {
        scanf("%d",&k);
        for(int i = 1; i <= k; i++) {
          scanf("%s",&A[i][1]);
          Count[i] = 0;
          Won[i] = 0;
        }

        for(int i = 1; i <= k; i++)  {
            for(int j = 1; j <= k; j++) {
                if (A[i][j] != '.') Count[i]++;
                if (A[i][j] == '1') Won[i]++;
            }
            wp[i] = Won[i]/(double) Count[i];
        }
        for(int i = 1; i <= k; i++)  {
            int tot = 0;
            int total = 0;
            double sum = 0;
            for(int j = 1; j <= k; j++) {
                if (A[i][j] != '.') {
                        if (A[i][j] == '0') {
                            tot = Count[j]-1;
                            total++;
                            sum += (double) (Won[j] - 1) / tot;
                        }
                        else {
                            tot = Count[j]-1;
                            total++;
                            sum += ((double)Won[j]) / tot;
                        }
                }
            }
            owp[i] = ((double) sum) / total;
            }
        for(int i = 1; i <= k; i++)  {
            int tot = 0;
            double sum = 0;
             for(int j = 1; j <= k; j++)
              if (A[i][j] != '.') {
                  sum+=owp[j];
                  tot++;
              }
            oowp[i] = sum / (double) tot;
        }
        contor++;
        printf("Case #%d:\n",contor);
        for(int i = 1; i <= k; i++) {
         double now = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
         printf("%.10f\n",now);
        }
        tc--;
    }
    return 0;
}
