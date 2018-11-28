#include<iostream>
using namespace std;

int t,r,n,k;
long long g[1005],a[1005],b[1005];

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    
    scanf("%d",&t);
    for(int c=1;c<=t;c++)
    {
        printf("Case #%d: ",c);
        scanf("%d%d%d",&r,&k,&n);
        for(int i=0;i<n;i++) scanf("%lld",&g[i]);
        
        for(int i=0;i<n;i++)
        {
             int sum=g[i],j;
             bool f=0;
             for(j=i;sum<=k;)
             {
                 j++;
                 if(j==n) 
                 {
                     j=0;
                     f=1;
                 }
                 sum+=g[j];
                 if(f&&j==i) break;
             }
             a[i]=sum-g[j];
             b[i]=j;
        }
    //    printf("\n"); for(int i=0;i<n;i++) printf("%d %d\n",a[i],b[i]);
        
        long long res=0,st=0;
        for(int i=0;i<r;i++)
        {
             res+=a[st];
             st=b[st];
        }
        printf("%lld\n",res);
     //   cout<<res<<endl;
        
    }
    
    return 0;
} 
