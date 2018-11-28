#include<stdio.h>
#include<string.h>

int t,n;
int a[45];
char c;
int main()
{
    int I,j,k,Case;
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d",&t);
    for(Case=1;Case<=t;Case++)
    {
    scanf("%d\n",&n);
    int ans=0;
    memset(a,0,sizeof(a));
                        for(I=0;I<n;I++)
                         {
                                        for(j=0;j<n;j++)
                                        {
                                                        scanf("%c",&c);
                                                        if(c=='1')
                                                        a[I]=j;
                                        }
                                        getchar();
                         }
                         for(I=0;I<n-1;I++)
                         {
                                         for(j=I;j<n;j++)
                                         if(a[j]<=I) break;
                                         ans+=j-I;
                                         for(k=j;k>I;k--)
                                         a[k]=a[k-1];
                         }
                         printf("Case #%d: %d\n",Case,ans);
    }
    return 0;
}
                         
    
