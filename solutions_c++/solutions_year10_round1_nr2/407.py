//Google1_B

#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;


int D,I,M,N;
int a[1110],dp[1110][256];


int main()
{
    freopen("B-small-attempt3.in","r",stdin);
    freopen("B-small-attempt3.out","w",stdout);

    int t,cs;
    scanf("%d",&t);
    cs=0;
    while(++cs<=t){
        
        int i,j,k;
        scanf("%d%d%d%d",&D,&I,&M,&N);
        
        for(i=1;i<=N;++i)scanf("%d",a+i);
        
        memset(dp,0,sizeof(dp));

        if(M>0){
        
            for(i=1;i<=N;++i){
                for(j=0;j<=255;++j){
                    
                    int cost=1<<29;
                    
                    cost = dp[i-1][j]+D;//delete a[i]
                    
                    //change a[i] and insert some value to make it valid.
                    int tmp=1<<29,dis;
                    
                    dis = a[i] - j ;
                    if(dis<0) dis =-dis;
    
                    for(k=0;k<=255;++k){
                        int ta = k - j;
                        if(ta<0) ta=-ta;
                        
                        int b=0;
                        if(ta==0)b=0;
                        else{
                            b =((ta-1)/M) * I;
                        }
    
                        b += dp[i-1][k];
                        
                        if(tmp > b)tmp = b;
                    }                    
                    
    
                    
                    tmp += dis;
                    
    
                    if( cost > tmp ) cost = tmp; 
    
                    
                    dp[i][j] = cost;
                }
            }
            
            int ans=1<<29;
            for(i=0;i<=255;++i){
                if( dp[N][i] < ans ) ans = dp[N][i];
            }   
            
            
            printf("Case #%d: %d\n",cs,ans);
    
        }
        else{//M==0
        
            int ans=(N-1)*D;
            for(i=1;i<=N;++i){
                int base = a[i];
                int res=0;
                for(j=1;j<=N;++j){
                    int tp =  base - a[j];
                    if(tp<0) tp = -tp;
                    res += tp;
                }
                
                if(ans>res)ans = res;
            }
        
            
            printf("Case #%d: %d\n",cs,ans);
        }
        
        
        
    }
    
    
    
    return 0;    
}
/*
21
6 6 2 3
1 7 5
100 1 5 3
1 50 7


*/
