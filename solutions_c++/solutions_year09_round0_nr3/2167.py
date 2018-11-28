#include <iostream>
using namespace std;
char str[] = "$welcome to code jam";
char text[1024];
int DP[512][32];
char s[2];
int N;
int calc_malc()
{
    DP[0][0]=1;
    for(int i=1;text[i]!=0;i++)
    {
                    for(int j=0;j<i;j++)
                            for(int k=0;k<19;k++)
                            {
                                if(text[i]==str[k+1])
                                {
                                                     DP[i][k+1]+=DP[j][k];
                                                     DP[i][k+1]%=10000;
                                }        
                                    
                            }
    }
    int ans=0;
    for(int i=1;text[i]!=0;i++)
    {
              ans+=DP[i][19];      
              ans%=10000;
    }
    return ans%10000;
}


int main()
{
    scanf("%d",&N);
    gets(s);
    
    for(int i=1;i<=N;i++)
    {
            memset(text,0,sizeof(text));
            memset(DP,0,sizeof(DP));
            gets(text+1);
            
            printf("Case #%d: %04d\n",i,calc_malc());
    }    
    
}
