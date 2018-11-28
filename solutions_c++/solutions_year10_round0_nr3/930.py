#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
const int MAXN=1010;
long long a[MAXN],b[MAXN],c[MAXN],d[MAXN];
int tot,num,n,r,k,sum;


void dfs(int p)
{
     if (p==0)
       {
         for (int i=0;i<n;++i)   c[i]=0;
         return ;
       }
     dfs(p/2);
     for (long long i=0;i<n;++i)
       {
         d[i]=c[i];
         if (p&1)  d[i]+=b[(i+d[i])%n];
         d[i]+=c[(i+d[i])%n];
//         printf("%d %d %d\n",p,i,d[i]);
       }
     for (int i=0;i<n;++i)   c[i]=d[i];
}        

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("ou.txt","w",stdout);
    scanf("%d",&tot);
    num=0;
    while (tot--)
      {
        ++num;
        printf("Case #%d: ",num);
        scanf("%d%d%d",&r,&k,&n);
        for (int i=0;i<n;++i)
          scanf("%d",&a[i]);
        for (int i=0;i<n;++i)
          {
            b[i]=0;
            sum=k; 
            while (b[i]<n && a[(i+b[i])%n]<=sum)
              {
                sum-=a[(i+b[i])%n];
                ++b[i];
              }
  //          printf("%d %d\n",i,b[i]);
          }
        dfs(r);
        long long ans=0;
        for (int i=0;i<n;++i)   ans+=a[i];
        ans*=(c[0]/n);
        c[0]%=n;
        for (int i=0;i<c[0];++i)  ans+=a[i];
        cout<<ans<<endl;
      }
}
