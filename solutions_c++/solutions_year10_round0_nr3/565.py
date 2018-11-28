#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define SIZE 1010

int T, N, K, R, V[SIZE];
long long ans, tb[SIZE], stp[SIZE];

int main()
{
    //freopen("C-large.in","r",stdin);
    //freopen("out.txt","w",stdout);
    
    int i, j, temp, t = 1;
    long long s;
    
    for ( scanf("%d",&T); T; T-- ) {
        for ( scanf("%d%d%d",&R,&K,&N), i = 0; i < N; i++ )
            scanf("%d",&V[i]);
        
        memset(tb,-1,sizeof(tb));
        for ( ans = i = 0, j = 1; j <= R; j++ ) {
            if ( tb[i] != -1 )
                break;
            else {
                stp[i] = j;
                tb[i] = ans; 
            }
            
            temp = i;
            for ( s = 0; 1; i = (i+1)%N ) {
                if ( s + V[i] <= K )
                    s += V[i];
                else
                    break;
                if ( i == (temp-1+N) % N ) {
                    i = temp;
                    break;
                }
            }
            
            ans += s;
        }
        
        if ( j == R + 1 ) {
            printf("Case #%d: %lld\n",t++,ans);
            continue;
        }
        
        s = ans - tb[i];
        ans += s * ( (R-j+1)/(j - stp[i]) );
        
        j = ((R-j+1)%(j - stp[i]));
        for ( ; j; j-- ) {
            temp = i;
            
            for ( s = 0; 1; i = (i+1)%N ) {
                if ( s + V[i] <= K )
                    s += V[i];
                else
                    break;
                if ( i == (temp-1+N) % N ) {
                    i = temp;
                    break;
                }
            }
            
            ans += s;
        }
        
        printf("Case #%d: %lld\n",t++,ans);
    }
    
    return 0;
}
