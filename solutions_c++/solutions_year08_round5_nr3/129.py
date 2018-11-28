#include<vector>
#include<string>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<cstdlib>

using namespace std;

int prob[20];
int dp[20][2000];
int m, n;

int main() {
    int teste, t;
    scanf("%d", &teste);
    int i, j, k;
    
    for (t=0; t<teste; t++) {
        scanf("%d %d", &m, &n);
        char leitor[100];
        for (i=0; i<m; i++){
            scanf("%s", leitor);
            int aux = 0;
            for (j=0; j<n; j++){
                aux *= 2;
                if (leitor[j] == 'x')
                   aux++;
            }
            prob[i] = aux;
        }
        /*for (i=0; i<m; i++){
            printf("%d\n", prob[i]);
        }*/
        for (i=0; i<20; i++){
            for (j=0; j<2000; j++){
                dp[i][j] = 0;
            }
        }
        for (k=1; k<=m; k++){
            for (i=0; i<(1<<n); i++){
                if ((i&prob[k-1])!=0) continue;
                //printf("%d %d %d\n", k, i, prob[k-1]);
                for (j=1; j<n; j++){
                    if ((((1<<j)&i)!=0) && (((1<<(j-1))&i)!=0)) break;
                }
                if (j<n) continue;
                int count = 0;
                j = i;
                while(j>0){
                    if (j%2==1) count++;
                    j = j>>1;
                }
                //printf("%d %d\n", i, count);
                for (j=0; j<(1<<n); j++){
                    int a;
                    for (a=1; a<n; a++){
                          if ((((1<<a)&i)!=0) && (((1<<(a-1))&j)!=0)) break;
                    }                    
                    if (a<n) continue;
                    for (a=1; a<n; a++){
                          if ((((1<<a)&j)!=0) && (((1<<(a-1))&i)!=0)) break;
                    }                    
                    if (a<n) continue;
                    dp[k][i] = max(dp[k][i], dp[k-1][j] + count);
                }
            }    
        }
/*        for (i=0; i<=m; i++){
            for (j=0; j<(1<<n); j++){
                printf("%d ", dp[i][j]);
            }
            printf("\n");
        }*/
        int resp = 0;
        for (i=0; i<(1<<n); i++){
            resp = max(resp, dp[m][i]);
        }
        printf("Case #%d: %d\n", t+1, resp);   
    }
    return 0;    
}
