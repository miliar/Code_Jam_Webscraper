#include <cstdio>

#define MAX 10001

int m, v;
int tab[MAX];
int G[MAX];
int C[MAX];
int I[MAX];
int M[MAX];

int licz(int nr)
{
    for(int i=(m-1)/2;i>0;i--) {
        int p=i*2;
        int q=p+1;

        if( G[i] != v ) {
            I[i] = -1;
            if( I[q] != -1 )
                I[i] = I[q];
            if( I[p] != -1 && (I[i] == -1 || I[p] < I[i]) )
                I[i] = I[p];
//            printf("      %d\n", I[i] );
        } else {
            if( I[q] == -1 && I[p] == -1 ) {
                I[i] = -1;
            } else {
                if( C[i] == 0 ) {
                    if( I[q] != -1 && I[p] != -1 )
                        I[i] = I[q] + I[p];
                    else
                        I[i] = -1;
                } else {
                    if( I[q] == -1 ) {
                        I[i] = I[p] + 1;

                    } else if( I[p] == -1 ) {
                        I[i] = I[q] + 1;

                    } else {
                        if( I[q] == 0 && I[p] == 0 ) {
                            I[i] = 0;
                        } else {
                            if( I[q] > I[p] )
                                I[i] = I[p] + 1;
                            else
                                I[i] = I[q] + 1;
                        }
                    }
                }
            }
        }
//        printf("  %d\n", I[i] );
    }
    return I[1];
}

int wczytaj()
{
    int val;
    scanf("%d %d", &m, &v );

    
    for(int i=1;i<=(m-1)/2;i++) {
        scanf("%d %d", &G[i], &C[i] );
        I[i] = -1;
    }
    
    for(int i=(m+1)/2;i<=m;i++) {
        scanf("%d", &val);
        if( val == v )
            I[i] = 0;
        else
            I[i] = -1;
    }
    return 0;
}

int main()
{
    int n;
    scanf("%d", &n );
    for( int i=1;i<=n;i++) {
        wczytaj();
        int ret = licz(i);
        if( ret == -1)
            printf("Case #%d: IMPOSSIBLE\n", i );
        else
            printf("Case #%d: %d\n", i, ret );
    }
    return 0;
}
