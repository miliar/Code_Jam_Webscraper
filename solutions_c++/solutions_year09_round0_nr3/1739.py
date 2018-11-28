#include<stdio.h>
#include<string.h>

char wrd[] = { "welcome to code jam" };

int dp[22];

char in[502];

int main()
{
    freopen("Clarge.in","r",stdin);
    freopen("Clarge.out","w",stdout);
    
    int wlen = strlen(wrd);
    
    int T;
    scanf("%d",&T);
    
    getchar();
    
    for(int t = 1; t <= T; ++t)
    {
        gets(in);
        int len = strlen(in);
            
        memset(dp,0,sizeof(dp));
            
        for(int i = 0; i < len; ++i)
        {
            for(int j = 0; j < wlen; ++j)
            {
                if(in[i]==wrd[j])
                {
                    if(j==0)
                    {
                        dp[j]++;   
                        dp[j] %= 10000;
                    }   
                    else
                    {
                        dp[j] += dp[j-1];
                        dp[j] %= 10000;   
                    }
                }   
            }
        }
        
        printf("Case #%d: ",t);
        
        int a = dp[wlen-1];
        
        printf("%d%d%d%d\n",(a/1000)%10,(a/100)%10,(a/10)%10,a%10);
    }
    
    return 0;    
}
