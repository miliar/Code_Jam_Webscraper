#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
long long gcd(long long a,long long b)
{
     long long c;
     while(a%b!=0)
     {
                  c=a%b;
                  a=b;
                  b=c;
     }
     return b;
}

long long t[1000];
int n;
int tt;
int main()
{
    int i,j;
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B.out","w",stdout);
    scanf("%d",&tt);
    for(int ca=1;ca<=tt;ca++)
    {
           // printf("%d\n",ca);
            scanf("%d",&n);
            for(i=0;i<n;i++)
            scanf("%I64d",&t[i]);
            sort(t,t+n);
            n=unique(t,t+n)-t;
            long long ans;
            if(n<2) ans=0;
            else
            {
                long long aa=t[1]-t[0];
            for(i=0;i<n-1;i++)
             for(j=i+1;j<n;j++)
             aa=gcd(aa,t[j]-t[i]);
            
              ans=(aa-t[0]%aa)%aa;
              }
             printf("Case #%d: ",ca);
             printf("%I64d\n",ans);
    }
    return 0;
}
             
            
            
    
    

