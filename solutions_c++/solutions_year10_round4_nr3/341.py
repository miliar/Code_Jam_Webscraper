#include <cstdio>
#include <cstring>

using namespace std;

char dp[105][105], dp2[105][105];

int main(){
    
    freopen("c.in","r",stdin);
    freopen("c.txt","w",stdout);
    
    int cas, c, i, j, k, x1, y1, x2, y2, num, get, maxx, maxy;
    
    scanf("%d", &cas);
    for( c=1; c<=cas; ++c  ){
        
        memset(dp,0,sizeof(dp));
        memset(dp2,0,sizeof(dp2));
        scanf("%d", &num);
        maxx = 0;
        maxy = 0;
        for( i=0; i<num; ++i ){
            scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
            
            if( x2 > maxx ) maxx = x2;
            if( y2 > maxy ) maxy = y2;
            
            for( j=x1; j<=x2; ++j )
                for( k=y1; k<=y2; ++k )
                    dp[j][k] = true;
        }
        
        for( i=1,get=0; i<=100; ++i )
            for( j=1; j<=100; ++j )
                if( dp[i][j] )  ++get;
        
        num = 0;
        while( get!=0 ){
            ++num;
            if( num&1 ){
            for( i=1; i<=maxx; ++i )
                for( j=1; j<=maxy; ++j ){
                    
                    if( dp[i][j] ){
                        if( dp[i-1][j] || dp[i][j-1] )
                            dp2[i][j] = true;
                        else{
                            dp2[i][j] = false;
                            --get;
                        }
                    }
                    else{
                        if( dp[i-1][j] && dp[i][j-1] ){
                            dp2[i][j] = true;
                            ++get;
                        }
                        else
                            dp2[i][j] = false;
                    }
                    
                }
            }
            else{
            for( i=1; i<=maxx; ++i )
                for( j=1; j<=maxy; ++j ){
                    
                    if( dp2[i][j] ){
                        if( dp2[i-1][j] || dp2[i][j-1] )
                            dp[i][j] = true;
                        else{
                            dp[i][j] = false;
                            --get;
                        }
                    }
                    else{
                        if( dp2[i-1][j] && dp2[i][j-1] ){
                            dp[i][j] = true;
                            ++get;
                        }
                        else
                            dp[i][j] = false;
                    }
                }
            }
        }
        
        printf("Case #%d: %d\n", c, num);
        
        
    }
    
    return 0;
}
