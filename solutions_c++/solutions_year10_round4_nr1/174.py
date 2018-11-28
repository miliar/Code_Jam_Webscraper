#include <cstdio>
#include <cstring>

int N,dia[100][100],test[102][102];

bool Check(int L) {
    int i,j;
    bool yes=1;

    for(i=0; i<L; i++)
        for(j=0; j<L; j++) {
            if(test[i][j] == -1)
                continue;
            if(test[i][j] != test[j][i] && test[j][i] != -1) 
                yes = 0;
            if(test[i][j] != test[L-i-1][L-j-1] && test[L-i-1][L-j-1] != -1)
                yes = 0;
            if(test[i][j] != test[L-j-1][L-i-1] && test[L-j-1][L-i-1] != -1)
                yes = 0;
            if(yes == 0) {
                return yes;
            }
        }
    return yes;
}

int main() {
    int i,j,k,r,c,T,cas=1;

    scanf("%d", &T);
    while(T--) {
        scanf("%d", &N);
        for(i=0; i<N; i++) {
            r = i;
            c = 0;
            for(j=0; j<i+1; j++) {
                scanf("%d", &dia[r][c]);
                r--;
                c++;
            }
        }
        for(; i<N*2-1; i++) {
            r = N - 1;
            c = i - N + 1;
            for(j=0; j<N*2-i-1; j++) {
                scanf("%d", &dia[r][c]);
                r--;
                c++;
            }
        }
        /*for(i=0; i<N; i++) {
            for(j=0; j<N; j++)
                printf("%d", dia[i][j]);
            printf("\n");
        }*/
        bool f=0;
        int ans;
        for(k=N; k<=N*2; k++) {
            for(i=0; i<k-N+1; i++)
                for(j=0; j<k-N+1; j++) {
                    memset(test, 0xff, sizeof(test));
                    for(int r=0; r<N; r++)
                        for(int c=0; c<N; c++)
                            test[r+i][c+j] = dia[r][c];
                    /*for(int r=0; r<k; r++) {
                        for(int c=0; c<k; c++)
                            printf("%d ", test[r][c]);
                        printf("\n");
                    }*/
                    if(Check(k)) {
                        f = 1;
                    }
                }
            if(f)
                break;
        }
        printf("Case #%d: %d\n", cas++, k*k-N*N);
    }
    return 0;
}
