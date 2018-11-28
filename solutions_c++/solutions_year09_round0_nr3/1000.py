#include<stdio.h>
#include<string.h>
const char standard[100]="welcome to code jam";
const int stlen=19;
int f[1100][100];
char str[1100];
void print(int x)
{
    if(x==0) printf("0000");
    else if(x<10) printf("000%d",x);
    else if(x<100) printf("00%d",x);
    else if(x<1000) printf("0%d",x);
    else printf("%d",x);
}
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("c.out","w",stdout);
    int ncase,nc,len,i,j,k,ans;
    scanf("%d",&ncase);
    for(nc=1;nc<=ncase;nc++)
    {

        while(gets(str))
            if(strlen(str)!=0) break;
        len=strlen(str);
        for(i=0;i<len;i++) for(j=0;j<19;j++) f[i][j]=0;
        for(i=len-1;i>=0;i--)
        {
            for(j=0;j<19;j++)
                if(str[i]==standard[j])
                {
                    if(j==18) f[i][j]=1;
                    else
                    {
                        for(k=i+1;k<len;k++)
                            if(str[k]==standard[j+1])
                            {
                                f[i][j]+=f[k][j+1];
                                f[i][j]%=10000;
                            }
                    }
                }
        }
        ans=0;
        for(i=0;i<len;i++)
        {
            if(str[i]==standard[0]) 
            {
                ans+=f[i][0];
                ans%=10000;
            }
        }
        printf("Case #%d: ",nc);
        print(ans);
        printf("\n");
    }
    return 0;
}
