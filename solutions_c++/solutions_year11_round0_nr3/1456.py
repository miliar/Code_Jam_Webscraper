#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int T, N, t = 0, Sum, Max, W[1010], A[1048576], B[1048576];

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    
    int i, j, k;
    
    for ( scanf("%d",&T); T; T-- ) {
        for ( scanf("%d",&N), Max = Sum = i = 0; i < N; i++ ) {
            scanf("%d",&W[i]);
            Sum ^= W[i];
            if ( W[i] > Max )
                Max = W[i];
        }      
        
        if ( Sum )
            printf("Case #%d: NO\n",++t);
        else {
            for ( i = 1; i <= Max; i <<=  1 )
                ;
            k = i-1;
                
            memset(A,-1,sizeof(A));
            A[0] = 0;
            A[W[0]] = W[0];
            for ( i = 1; i < N; i++ ) {
                if ( i&1 ) {
                    memset(B,-1,sizeof(B));
                    for ( j = 0; j <= k; j++ ) {
                        if ( A[j] == -1 )
                            continue; 
                        if ( A[j] > B[j] )
                            B[j] = A[j];
                        if ( A[j] + W[i] > B[j^W[i]] )
                            B[j^W[i]] = A[j] + W[i];
                    }
                }
                else {
                    memset(A,-1,sizeof(A));
                    for ( j = 0; j <= k; j++ ) {
                        if ( B[j] == -1 )
                            continue; 
                        if ( B[j] > A[j] )
                            A[j] = B[j];
                        if ( B[j] + W[i] > A[j^W[i]] )
                            A[j^W[i]] = B[j] + W[i];
                    }
                }
            }
        
            if ( N&1 ) {
                for ( i = 0, j = 1; j <= k; j++ )
                    if ( A[j] > i )
                        i = A[j];
                printf("Case #%d: %d\n",++t,i);
            }
            else {
                for ( i = 0, j = 1; j <= k; j++ )
                    if ( B[j] > i )
                        i = B[j]; 
                printf("Case #%d: %d\n",++t,i);
            }
        }
    }
    
    return 0;
}
