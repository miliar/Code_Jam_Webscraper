#include <stdio.h>
#include <string>
#include <string.h>
#include <algorithm>
using namespace std;
int sum[510],sum1[510];
char s[510];
void work()
{
        memset(sum,0,sizeof(sum));
        int i,j;
        int len = strlen(s);
        char w[20]="welcome to code jam";
        
        if (s[0]=='w') sum[0]=1;
        else sum[0]=0;
        
        for (i=1;i<len;i++) 
        {
                sum[i]=sum[i-1];
                if (s[i]=='w') sum[i]++;
                sum[i]%=10000;
        }
                
        for (i=1;i<=18;i++)
        {
                char c = w[i];
                
                memset(sum1,0,sizeof(sum1));
                for (j=1;j<len;j++)
                {
                        if (s[j]==c) sum1[j] = sum[j-1];
                        sum1[j]+=sum1[j-1];
                        
                        sum1[j]%=10000;
                }
                memcpy(sum,sum1,sizeof(sum1));
        }
        printf("%04d\n",sum[len-1]);
}       
int main()
{
        freopen("c.in","r",stdin);
        freopen("c.out","w",stdout);
        int cs;
        int N;
        scanf("%d",&N);
        gets(s);        
        for (cs=1;cs<=N;cs++)
        {
                printf("Case #%d: ",cs);                
                gets(s);
                work();
        }
        return 0;
}
                
                
                
