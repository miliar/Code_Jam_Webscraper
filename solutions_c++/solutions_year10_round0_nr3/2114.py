#include<stdio.h>
int n,m,i,j,k,l,t,tt,r;
int g[1001],a[1001],b[1001],c[1001];
long long ans;

int main()
{
    freopen("2.in","r",stdin);
    freopen("2.out","w",stdout);
    scanf("%d",&tt);
    for (t=1;t<=tt;t++)
    {
        scanf("%d%d%d",&r,&k,&n);
        for (i=1;i<=n;i++) {a[i]=b[i]=c[i]=0;scanf("%d",&g[i]);}
        l=2;int sum=g[1];
        for (i=1;i<=n;i++)
        {
            if (l==i) {sum=g[i];l=i+1;if (l>n) {l=1;}}
            while ((l!=i)&&(sum+g[l]<=k)) 
            {
                  sum+=g[l];
                  l++;
                  if (l>n) {l=1;}
            }
            
            a[i]=l;
            b[i]=sum;
            sum-=g[i];
        }
        if (n==1)
        {
                 a[1]=1;
                 b[1]=g[1];
        }
        
        if (r<=2000)
        {
                    ans=0;l=1;
                    for (i=1;i<=r;i++)
                    {
                        long long bb=b[l];
                        ans+=bb;
                        l=a[l];
                    }
        } else
        {
              l=1;i=1;ans=0;
              while (c[l]==0)
              {
                    c[l]=i;
                    i++;
                    l=a[l];
              }
              k=c[l]-1+(r-c[l]+1)%(i-c[l]);
              int h=l;
              for (j=1;j<=k;j++)
              {
                     long long bb=b[l];
                     ans+=bb;
                     l=a[l];
              }
              long long cc,dd;
              cc=i-c[h];
              dd=(r-k)/cc;
              cc=b[h];
              l=a[h];
              while (l!=h) {cc+=b[l];l=a[l];}
              ans+=cc*dd;
              
        }
        
        
        printf("Case #%d: %lld\n",t,ans);
    }
    
    return 0;
}
