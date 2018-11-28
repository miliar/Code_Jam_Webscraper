/*
TASK: Code Jam '09 - Problem C
LANG: C++
*/

//welcome to code jam

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

    char str[600];
    int dp[600][20];
    char cj[]="welcome to code jam";

int main()
{
    int n,i,cc,cases,j,k,ans;
    
//    printf("Strlen %d\n", strlen(cj));
    
    scanf("%d\n", &cases);
    
    for(cc=0;cc<cases;cc++)
    {
        ans=0;
        
        gets(str);
        
        n = strlen(str);
        
        for(i=0;i<n;i++)
        {
            for(j=0;j<19;j++)
                dp[i][j]=0;
            
            for(j=0;j<19;j++)
            {
                if(str[i]==cj[j])
                {
                    if(j==0)
                    {
                        dp[i][j]++;
                    }
                    else
                    {
                        for(k=0;k<i;k++)
                        {
                            dp[i][j]=(dp[i][j]+dp[k][j-1])%10000;
//                            printf("dp %d %d = %d\n",i,j, dp[i][j]);
                        }
                    }
                }
            }
            
            ans=(ans+dp[i][18])%10000;
        }
        
        
        
        printf("Case #%d: %04d\n",cc+1,ans);
    }
    
    return 0;
}
