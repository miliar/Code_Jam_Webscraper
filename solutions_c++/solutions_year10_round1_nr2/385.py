#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN  =   100+5;
const int MAXR  =   260;

int D,I,N,M;
int array[MAXN];
int f[MAXN][MAXR];

void input(){
    scanf("%d%d%d%d", &D, &I, &M, &N);
    for(int i=1; i<=N; ++i)
        scanf("%d", &array[i]);
}

int app[MAXR];

int solve(){
    int t;

    if(M == 0){
        memset(app, 0, sizeof(app));
        for(int i=1; i<=N; ++i)
            app[array[i]]++;
        t = 0;
        for(int i=0; i<MAXR; ++i)
            t = max(t, app[i]);
        int r1 = D*(N-t);
        
        for(int k=0; k<MAXR; ++k){
            int rs = 0;
            for(int i=1; i<=N; ++i)
                rs += min(D, abs(array[i]-k));
            r1 = min(r1, rs);
        }
        return r1;
    }
    
    if(D == 0)return 0;
    
    memset(f, 0, sizeof(f));
    for(int i=0; i<MAXR; ++i){
        f[1][i] = abs(i - array[1]);
        for(int j=0; j<MAXR; ++j){
            t = abs(j - array[1]) + (abs(i - j)+M-1)/M*I;
            f[1][i] = min(f[1][i], t);
        }
        f[1][i] = min(f[1][i], D+I);
    }
    for(int i=2; i<=N; ++i){
        for(int j=0; j<MAXR; ++j){
            f[i][j] = D + f[i-1][j];

            t = abs(j - array[i]);
            for(int k=0; k<MAXR; ++k)
                t = min(t, abs(array[i] - k) + (abs(k-j)+M-1)/M*I);
            f[i][j] = min(f[i][j], D*(i-1) + t);

            t = f[i-1][j];
            for(int k=max(0, j-M); k<=min(MAXR, j+M); ++k)
                t = min(t, f[i-1][k]);
            f[i][j] = min(f[i][j], t + abs(j - array[i]));

            f[i][j] = min(f[i][j], t + D + I);

            t = f[i-1][array[i]];
            for(int k=max(0, array[i]-M); k<=min(MAXR, array[i]+M); ++k)
                t = min(t, f[i-1][k]);
            f[i][j] = min(f[i][j], t + (abs(j-array[i])+M-1)/M*I);

            for(int nj=0; nj<=MAXR; ++nj){
                t = f[i-1][nj];
                for(int k=max(0, nj-M); k<=min(MAXR, nj+M); ++k)
                    t = min(t, f[i-1][k]);
                f[i][j] = min(f[i][j], t + abs(array[i] - nj) + (abs(j-nj)+M-1)/M*I);
            }
        }
    }

    t = f[N][0];
    for(int i=1; i<MAXR; ++i)
        t = min(t, f[N][i]);
    return t;
}

void debugout(){
    for(int i=1; i<=N; ++i)
        for(int j=0; j<MAXR; ++j)
            printf("f[%d][%d] = %d\n", i, j, f[i][j]);
}

int main(){
    int t;
    scanf("%d", &t);
    for(int i=1; i<=t; ++i){
        input();
        printf("Case #%d: %d\n", i, solve());
        //debugout();
    }
}

