#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#define PB push_back
#define see(x) //cout<<#x<<" : "<<x<<endl
#define FOR(i,b,c) for(i=(b);i<(c);i++)
using namespace std;
typedef long long LL;
LL sum[1010];
int Sarch(int low,int high,int val,LL lim)
{
   int mid;
   LL TMP;
   while(low<high)
   {
      mid=(low+high)>>1;
      TMP=sum[mid]-lim;
      if(TMP==val)return mid;
      if(TMP>val)high=mid-1;
      else low=mid+1;
   }
   return(sum[low]-lim<=val)?low:low-1;
}
int main()
{
   int T,cas=1;
   freopen("C:\\Documents and Settings\\Administrator\\×ÀÃæ\\data.in","r",stdin);
   freopen("C:\\Documents and Settings\\Administrator\\×ÀÃæ\\data.out","w",stdout);
   scanf("%d",&T);
   while(T--)
   {
      int n,k,i,m,R,ST,idx;
      scanf("%d%d%d",&R,&m,&n);
      LL ans=0;
      for(i=1;i<=n;i++)
      {
         cin>>sum[i];
         sum[i]+=sum[i-1];
      }
      printf("Case #%d: ",cas++);
      if(m>=sum[n])cout<<R*sum[n]<<endl;
      else
      {
         ST=0;
         while(R--)
         {
            if(m>=sum[n]-sum[ST])
            {
               idx=Sarch(0,n,m-sum[n]+sum[ST],0);
               ans+=sum[n]-sum[ST];
               ans+=sum[idx];
               ST=idx%n;
            }
            else
            {
               idx=Sarch(ST,n,m,sum[ST]);
               ans+=sum[idx]-sum[ST];
               ST=idx%n;
            }
            see(ST);
         }
         cout<<ans<<endl;
      }
   }
}
