#include<stdio.h>
#include<string.h>

int t;
char ss[]="welcome to code jam";
char s[550];
int dp[550][27];

int to(char c)
{
    if(c==' ')return 26;
    return c-'a';
}

void init()
{
    int i,j;
    for(i=0;i<550;i++)
    {
        for(j=0;j<27;j++)
            dp[i][j]=0;
    }
}

int main()
{//freopen("in.txt","r",stdin);
//freopen("out.txt","w",stdout);
    int len=strlen(ss);
    int ca;
    scanf("%d\n",&t);
    for(ca=1;ca<=t;ca++)
    {
        gets(s);
        int i,j,k,n=strlen(s);
        init();
        for(i=n-1;i>=0;i--)
        {
            for(j=0;j<len;j++)
            {
                if(s[i]==ss[j])
                {
                    if(j==len-1)
                        dp[i][j]=1;
                    else
                    {
                        for(k=i+1;k<n;k++)
                        {
                            dp[i][j]+=dp[k][j+1];
                        }
                        dp[i][j]%=10000;
                    }
                }
            }
        }
        int ans=0;
        for(i=0;i<n;i++)
        {
            ans+=dp[i][0];
        }
        printf("Case #%d: %04d\n",ca,ans%10000);
    }

    return 0;
}

