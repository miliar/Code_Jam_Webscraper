#include <stdio.h>
#include <memory.h>
int n,k,b,t,t0,v[110],sign[110],x[110],ans;
int main()
{
    freopen("b-large.in","r",stdin);
    freopen("b-large.out","w",stdout);
    scanf("%d",&t0);
    for (int t1=1;t1<=t0;t1++)
    {
        scanf("%d%d%d%d",&n,&k,&b,&t);
        for (int i=1;i<=n;i++)
        {
            scanf("%d",&x[i]);
        }
        for (int i=1;i<=n;i++)
          scanf("%d",&v[i]);
        
        memset(sign,0,sizeof(sign));
        for (int i=n;i>0;i--)
        {
            if (x[i]+t*v[i]>=b) 
            {sign[i]=true;
            k--;
            }
            if (k==0) break;
        }
        if (k>0)
        {
            printf("Case #%d: IMPOSSIBLE\n",t1);
            continue;
        }
        

        ans=0;
        for (int i=1;i<=n;i++)  
          for (int j=1;j<i;j++)
          {
                if (sign[j]&&!sign[i]) ans++;
                
          }
          
        printf("Case #%d: %d\n",t1,ans);
    }
    
}
