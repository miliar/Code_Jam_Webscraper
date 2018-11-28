#include<stdio.h>
#include<stdlib.h>
#include<memory.h>
#include<algorithm>
using namespace std;

int x[1000000],y[1000000];
int p[3][3];

long long get3(int n) {
    long long N = n;
    long long res;
    if ( N < 3 ) return 0;
    res = N*(N-1)*(N-2)/6;
    return res;
}

int main(int argc, char *argv[]) {
    int N;
    int n,A,B,C,D,x0,y0,M;
    int nx,ny;
    long long res,xt,yt;
    freopen("A-large.in", "r", stdin);
    freopen("a-L.out", "w", stdout);
    
    scanf("%d", &N);
    for ( int nc = 1 ; nc <= N ; ++nc ) {
        scanf("%d%d%d%d%d%d%d%d", &n, &A, &B, &C, &D, &x0, &y0, &M);
        x[0] = x0;
        y[0] = y0;
        A %= M;
        B %= M;
        for ( int i = 1 ; i < n ; ++i ) {
            x[i] = ((long long)x[i-1]*A+B)%M;
            y[i] = ((long long)y[i-1]*C+D)%M;
        }
        /*
        for ( int i = 0 ; i < n ; ++i ) {
            printf("%d %d\n", x[i],y[i]);
        }
        */
        
        for ( int i = 0 ; i < n ; ++i ) {
            x[i] %= 3;
            y[i] %= 3;
        }
        
        memset(p, 0, sizeof(p));
        
        for ( int i = 0 ; i < n ; ++i ) {
            ++p[x[i]][y[i]];
        }
        
        
        res = 0;
        for ( int i = 0 ; i < 3 ; ++i ) for ( int j = 0 ; j < 3 ; ++j ) {
          //  printf("(%d,%d) %d\n", i,j,p[i][j]);
            res += (long long)get3(p[i][j]);
        }
      //  printf("res = %I64d\n", res);
        for ( int i = 0 ; i < 9 ; ++i ) for ( int j = i+1 ; j < 9 ; ++j ) for ( int k = j+1 ; k < 9 ; ++k ) {
            if ( i==j || j==k || i==k ) continue;
            int ai = i/3, bi = i%3;
            int aj = j/3, bj = j%3;
            int ak = k/3, bk = k%3;
            if ( (ai+aj+ak)%3 == 0 && (bi+bj+bk)%3 == 0 ) {
                res += (long long)p[ai][bi]*p[aj][bj]*p[ak][bk];
               // printf("%d %d %d %I64d\n", i,j,k,res);
            }
        }
        
        printf("Case #%d: ", nc);
        printf("%I64d\n", res);
    }
    fclose(stdout);
    fclose(stdin);
    return 0;
}
