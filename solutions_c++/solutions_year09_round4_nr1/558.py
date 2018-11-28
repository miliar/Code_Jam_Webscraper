#include<stdio.h>
#include<string.h>

int t,n;
int a[45];
char c;
int main()
{
    int i,j,k,tt;
    freopen("A-large(1).in","r",stdin);
    freopen("A.small.out","w",stdout);
    scanf("%d",&t);
    for(tt=1;tt<=t;tt++)
    {
                        scanf("%d\n",&n);
                        int ans=0;
                        memset(a,0,sizeof(a));
                        for(i=0;i<n;i++)
                         {
                                        for(j=0;j<n;j++)
                                        {
                                                        scanf("%c",&c);
                                                        if(c=='1')
                                                        a[i]=j;
                                        }
                                        getchar();
                         }
                         for(i=0;i<n-1;i++)
                         {
                                         for(j=i;j<n;j++)
                                         if(a[j]<=i) break;
                                         ans+=j-i;
                                         for(k=j;k>i;k--)
                                         a[k]=a[k-1];
                         }
                         printf("Case #%d: %d\n",tt,ans);
    }
    return 0;
}
                         
    
