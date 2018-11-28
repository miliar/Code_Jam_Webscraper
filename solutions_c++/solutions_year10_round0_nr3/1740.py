#include<iostream>
using namespace std;
int use[2000],p[2000];
long long Sum[2000];
int main()
{
    int T,t,i,j,l;
    int x,r,k;
    int n,h;
    long long ans,sum,S;
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        cin>>r>>k>>n;
        S=0;
        for(i=0;i<n;i++)
        {scanf("%d",&p[i]);S+=p[i];}
         memset(use,0,sizeof(use));
        j=0;x=0;ans=0;
        memset(Sum,0,sizeof(Sum));
        if(S<=k)
        {
            ans=r*S;
            printf("Case #%d: %lld\n",t,ans);
            continue;
        }
        while(r>0)
        {
            if(use[j]>0) break;
            x++;use[j]=x;
            sum=0;
            for(l=j;;l=(l+1)%n)
            {
                if(sum+p[l]<=k) sum+=p[l];
                else break;
            }
            Sum[x]=Sum[x-1]+sum;
            ans+=sum;r--;
            j=l;
        }
        if(r>0)
        {
            ans+=(int)(r/(x-use[j]+1))*(Sum[x]-Sum[use[j]-1]);
            r%=(x-use[j]+1);
            while(r--)
            {
                sum=0;
                for(l=j;;l=(l+1)%n)  if(sum+p[l]<=k) sum+=p[l]; else break;
                ans+=sum;
                j=l;
            }
        }
        printf("Case #%d: %lld\n",t,ans);
    }
}
