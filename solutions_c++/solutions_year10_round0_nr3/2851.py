#include<iostream>
int a[1010],sum[1010],opt[1010],optpos[1010];
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int t,r,k,n;
    int x,i;
    scanf("%d",&t);
    for(x=0;x<t;x++)
    {
                    scanf("%d%d%d",&r,&k,&n);
                    for(i=0;i<n;i++)
                    {
                                    scanf("%d",&a[i]);
                                    a[i+n]=a[i];
                                    }
                    a[2*n]=a[0];
                    sum[0]=a[0];
                    for(i=0;i<=2*n;i++)
                    sum[i]=sum[i-1]+a[i];
                    
                    int leftt=0,rightt=0;
                    for(leftt=0;leftt<n;leftt++)
                    {
                                                while(sum[rightt]-sum[leftt]+a[leftt]<=k&&rightt-leftt<n)
                                                rightt++;
                                                opt[leftt]=sum[rightt-1]-sum[leftt]+a[leftt];
                                                optpos[leftt]=rightt;
                                                }
                    /*for(i=0;i<n;i++)
                    printf("%d ",opt[i]);*/
                    
                    int ans=0,start=0;
                    for(i=0;i<r;i++)
                    {
                                    ans+=opt[start];
                                    start=optpos[start]%n;
                                    }
                    
                    printf("Case #%d: %d\n",x+1,ans);
                    }
    scanf(" ");
    return 0;
    }
