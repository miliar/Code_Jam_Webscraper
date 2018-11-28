#include<stdio.h>
#include<string.h>
char data[110][110];
int right[110];
int main()
{
    int t;
    freopen("A-large.in","r",stdin);
    freopen("out","w",stdout);
    scanf("%d",&t);
    for (int tt=1;tt<=t;tt++)
    {
        int n,ans=0;
        scanf("%d",&n);
        for (int i=1;i<=n;i++)
        {
            scanf("%s",data+i);
            right[i]=0;
            for (int j=0;j<n;j++)
                if (data[i][j]=='1') right[i]=j+1;
            //printf("%d\n",right[i]);
        }
        for (int i=1;i<=n;i++)
            if (right[i]>i)
            {
                int k;
                int temp=right[i];
                for (int j=i+1;j<=n;j++)
                    if (right[j]<=i)
                    {
                        k=j;
                        break;
                    }
                for (int j=k;j>i;j--)
                {
                    right[j]^=right[j-1]^=right[j]^=right[j-1];
                    ans++;
                }
                //right[k]=temp;
            }
        printf("Case #%d: %d\n",tt,ans);
    }
}