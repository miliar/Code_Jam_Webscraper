#include<stdio.h>
#include<stdlib.h>
int t;
int r,k,n;
int a[1005];
long long ans;
int pos,p,temp,num;

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int i,j;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%d%d%d",&r,&k,&n);
        for(j=0;j<n;j++)
            scanf("%d",&a[j]);
        p=0;
        ans=0;
        for(j=0;j<r;j++)
        {
            temp=0;
            num=0;
            while((temp+a[p]<=k)&&(num<n))
            {
                temp=temp+a[p];
                p=(p+1)%n;
                num++;
            }
            ans+=temp;
        }
        printf("Case #%d: %lld\n",i,ans);
    }
    return 0;
}
