#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int table[110][110];
double list[110];
double wp[110];
int len[110];

#define eps 1e-9

int main()
{
    char buffer[1000];
    int aa, nn, n, i, j, cnt, win, k;
    double ans, tmp;
    scanf("%d",&nn);
    for ( aa=1; aa<=nn; ++aa ) {
        scanf("%d",&n);
        memset(list,0,sizeof(list));
        memset(len,0,sizeof(len));
        for ( i = 0; i < n; i++ ) {
            scanf("%s",buffer);
            cnt = 0; win = 0;
            for ( j = 0; j < n; j++ ) {
                if ( buffer[j] == '0' ) table[i][j] = 0;
                if ( buffer[j] == '.' ) table[i][j] = -1;
                if ( buffer[j] == '1' ) table[i][j] = 1;
                if ( table[i][j] >= 0 ) cnt++;
                if ( table[i][j] == 1 ) win++;
            }
            wp[i] = 0.25*(win/(double)cnt);
            cnt--;
            for ( j = 0; j < n; j++ ) {
                if ( table[i][j] < 0 ) continue;
                if ( table[i][j] == 1 ) {
                    list[j] += ((win-1)/(double)cnt);
                } else {
                    list[j] += (win/(double)cnt);
                }
                len[j]++;
            }
        }
        printf("Case #%d:\n",aa);
        for ( i = 0; i < n; i++ ) {
            tmp = 0; cnt = 0;
            for ( j = 0; j < n; j++ ) {
                if ( table[i][j] < 0 ) continue;
                cnt++;
                tmp += (list[j]/len[j]); 
            }
            ans = wp[i] + 0.5*(list[i]/len[i]) + 0.25*(tmp/cnt) + eps;
            printf("%.8lf\n",ans);
        }
    }
}
