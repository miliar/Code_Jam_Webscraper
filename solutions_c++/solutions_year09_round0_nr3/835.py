#include<iostream>
#include<cstring>
#include<set>
#include<memory.h>
using namespace std;
char s[505];
int dp[19];
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("1.txt","w",stdout);
    int t;scanf("%d",&t);for(int hh=1;hh<=t;hh++){
        int i,j;
        while(gets(s)&&!s[0]);memset(dp,0,sizeof(dp));
        for(i=0;i<strlen(s);i++)
        {
             if(s[i]=='w')
             {
                  dp[0]++;      
             }
             else if(s[i]=='e')   
             {
                 dp[1]+=dp[0];
                 dp[6]+=dp[5];
                 dp[14]+=dp[13];
             } 
             else if(s[i]=='l')   
             {
                 dp[2]+=dp[1]; 
             } 
             else if(s[i]=='c')   
             {
                 dp[3]+=dp[2];dp[11]+=dp[10]; 
             } 
             else if(s[i]=='o')   
             {
                  dp[4]+=dp[3];
                  dp[9]+=dp[8];
                  dp[12]+=dp[11];
             } 
             else if(s[i]=='m')   
             {
                  dp[5]+=dp[4];
                  dp[18]+=dp[17];
             } 
             else if(s[i]=='t')   
             {
                  dp[8]+=dp[7];
             } 
             else if(s[i]=='d')   
             {
                  dp[13]+=dp[12];
             } 
             else if(s[i]=='j')   
             {
                  dp[16]+=dp[15];
             } 
             else if(s[i]=='a')   
             {
                  dp[17]+=dp[16];
             } 
             else if(s[i]==' ')   
             {
                  dp[7]+=dp[6];dp[10]+=dp[9];dp[15]+=dp[14];
             } 
             for(j=0;j<19;j++)dp[j]%=10000;               
        }
        printf("Case #%d: %04d\n",hh,dp[18]);
    }
}
