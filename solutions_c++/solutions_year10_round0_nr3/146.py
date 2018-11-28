#include<cstdio>
#include<queue>
using namespace std;

long long a[2000];
long long b[2000];
long long c[2000];
long long d[2000];

int main()
{
    long long t,i,j,r,k,n,temp,temp1,cnt,num,tt,yy,T=1;
    long long sum,ans,res;
    freopen("C-large.in","r",stdin);
    freopen("C.out","w",stdout);
    scanf("%I64d",&t);
    while(t--)
    {
        scanf("%I64d%I64d%I64d",&r,&k,&n);
        for(i=0;i<n;i++) scanf("%I64d",&a[i]);
        
        for(i=0;i<n;i++)
        {
            sum=a[i];
            for(j=(i+1)%n;j!=i;j=(j+1)%n)
            {
                if(sum+a[j]>k) break;
                sum+=a[j];
            }
            
            b[i]=j;
            c[i]=sum;
        }
        memset(d,0,sizeof(long long)*n);
        
        ans=0;
        
        temp=0;
        res=0;
        cnt=1;
        while(d[temp]==0)
        {
            d[temp]=cnt++;
            res+=c[temp];
            temp=b[temp];
        }
        temp1=0;
        for(i=0;i<d[temp]-1;i++)
        {
            ans+=c[temp1];
            temp1=b[temp1];
            r--;
        }
        num=cnt-d[temp];
        tt=res-ans;
        
        yy=r/num;
        
        ans+=yy*tt;

        r%=num;
        for(i=0;i<r;i++)
        {
            ans+=c[temp];
            temp=b[temp];
        }
        
        printf("Case #%I64d: %I64d\n",T++,ans);
    }
}
        
        
