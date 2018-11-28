#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>

int T, m, n, a[1000][1000], q, w, e, r;

int main(){
        scanf("%d", &T);
        for (int tt=1; tt<=T; tt++){
                printf("Case #%d: ", tt);
                for (int i=0; i<105; i++)
                        for (int j=0; j<105; j++)
                                a[i][j] = 0;
                int sum = 0;
                scanf("%d", &m);
                for (int i=0; i<m; i++){
                        scanf("%d%d%d%d", &q, &w, &e, &r);
                        for (int j=w; j<=r; j++)
                                for (int k=q; k<=e; k++)
                                        a[j][k] = 1;
                        }
                for (int i=0; i<=101; i++){
                        for (int j=0; j<=101; j++)
                                if (a[i][j]==1){
//                                      printf("1");
                                        sum++;
                                }
//                              } else printf("0");
//                      puts("");
                }

                int t = 0;
                while (sum!=0){
                        for (int i=101; i>=1; i--){
                                for (int j=101; j>=1; j--)
                                        if (a[i][j]==1){
                                                if (a[i-1][j] == 0 && a[i][j-1] == 0){
                                                        a[i][j] = 0;
                                                        sum--;
                                                }
                                        }
                                        else
                                                if (a[i-1][j] == 1 && a[i][j-1] == 1){
                                                        a[i][j] = 1;
                                                        sum++;
                                                }
                        }
                        t++;
                }
                printf("%d\n", t);
                }
        return 0;
}
