#include <cstdio>
#define MAXN  120
long double A[MAXN];//tozsame z WP
long double B[MAXN][MAXN];
long double OWP[MAXN];
long double OOWP[MAXN];
//long double C[MAXN][MAXN][MAXN];
char TMP[MAXN][MAXN];

long double f(int a, int b){
    return ((long double)(a))/((long double)(a+b));
}

int main(){
    int z;
    scanf("%d", &z);
    for(int q=1; q<=z; q++){
        int n;
        scanf("%d", &n);
        for(int i=0; i<n; i++){
            scanf("%s", TMP[i]);
            //uzupelaniam A
            int win = 0;
            int lose = 0;
            for(int j=0; j<n; j++){
                if(TMP[i][j]=='1'){
                    win++;
                }else if(TMP[i][j]=='0'){
                    lose++;
                }
            }
            A[i] = f(win, lose);
            //printf("WP: %d, %Lf\n", i, A[i]);

            for(int j=0; j<n; j++){
                if(TMP[i][j]=='1'){
                    B[i][j] = f(win - 1, lose);
                }else if(TMP[i][j]=='0'){
                    B[i][j] = f(win, lose - 1);
                }else{
                    B[i][j] = 0;
                }
                //printf("WPwithout: %d, %d, %Lf\n", i, j, B[i][j]);
            }
        }
        for(int i=0; i<n; i++){
            long double wynik = 0;
            long double ave = 0;
            int ile=0;
            for(int j=0; j<n; j++){
                if(TMP[j][i]!='.'){
                    ile++;
                    ave += B[j][i];
                } 
            }
            //printf("ave: %Lf, ile %d\n", ave, ile);
            OWP[i] = ave/(long double)(ile);
            //printf("OWP: %d, %Lf\n", i, OWP[i]);
        }
        for(int i=0; i<n; i++){
            long double wynik = 0;
            long double ave = 0;
            int ile=0;
            for(int j=0; j<n; j++){
                if(TMP[i][j]!='.'){
                    ile++;
                    ave += OWP[j];
                } 
            }
            OOWP[i]=ave/(long double)ile;
        }
        printf("Case #%d:\n", q);
        for(int i=0; i<n; i++){
            long double ans = (1.0/4.0)*A[i];
            ans += (1.0/2.0)*OWP[i];
            ans += (1.0/4.0)*OOWP[i];
            printf("%.10Lf\n", ans); 
        }
    }
    return 0;
}
