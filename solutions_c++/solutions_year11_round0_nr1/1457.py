#include <stdio.h>
#include <string.h>

char who[110][6];
int T, N, bp, op, t = 0, ct, dis[110];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    
    int i, j, k, d, h;
    
    for ( scanf("%d",&T); T; T-- ) {
        for ( scanf("%d",&N), i = 0; i < N; i++ )
            scanf("%s%d",who[i],&dis[i]);
            
            
            
        for ( bp = op = 1, ct = i = 0; i < N; i++ ) {
            if ( who[i][0] == 'O' ) {
                j = op - dis[i];
                if ( j < 0 )
                    j = -j;
                ct += (j+1);
                op = dis[i];
                for ( k = i + 1; k < N; k++ )
                    if ( who[k][0] == 'B' ) 
                        break;
                if ( k < N ) {
                    d = dis[k] - bp;
                    if ( d < 0 )
                        d = -d;
                    if ( d <= j+1 )
                        bp = dis[k];
                    else {
                        if ( bp < dis[k] )
                            bp += (j+1);
                        else
                            bp -= (j+1);
                    }
                }
            }
            else {
                j = bp - dis[i];
                if ( j < 0 )
                    j = -j;
                ct += (j+1);
                bp = dis[i];
                for ( k = i + 1; k < N; k++ )
                    if ( who[k][0] == 'O' ) 
                        break;
                if ( k < N ) {
                    d = dis[k] - op;
                    if ( d < 0 )
                        d = -d;
                    if ( d <= j+1 )
                        op = dis[k];
                    else {
                        if ( op < dis[k] )
                            op += (j+1);
                        else
                            op -= (j+1);
                    }
                }
            }
        }
        
        printf("Case #%d: %d\n",++t,ct);
    }
    
    return 0;
}
