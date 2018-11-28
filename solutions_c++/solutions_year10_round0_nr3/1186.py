#include<cassert>
#include<cstring>
#include<cstdio>
#include<vector>
#include<string>
#include<set>
#include<map>
#include<cmath>
#include<iostream>
#include<algorithm>
#define eps 1e-12
#define sqr(a) (a)*(a)
#define forn(i,n) for(int i=0;i<(int)n;i++)
#define taskname ""
typedef long long ll;
using namespace std;
#define N int(2e5)
ll x[N];
ll get[N];
int mv[N];
int t,r,k,n;
int main()         
{
  //#ifdef DEBUG
  //freopen(taskname"in","r",stdin);                         
//  freopen(taskname".out","w",stdout);
  //#endif
  scanf("%d",&t);
  forn(test,t)
  {
    ll ans=0;
    memset(mv,-1,sizeof(mv));
    memset(get,0,sizeof(get));
    cin>>r>>k>>n;
    forn(i,n)
      scanf("%I64d",&x[i]);
    int i=0,j=0,take=0;
    ll s=0;
    while(r)
    {
      if(take==0)
      {
        if(mv[i]==-1)
        {
          take=1;
          s+=x[i];
          i=(i+1)%n;
        }
        else
        {
          ans+=get[i];
          i=mv[i];
          r--;
        }
      }
      else if(take==n||s+x[i]>k)
      {      
   //     printf("r=%d i=%d take=%d s=%I64d\n",r,i,take,s);    
        mv[j]=i;
        get[j]=s;
        r--;
        j=i;
        ans+=s;
        s=0;
        take=0;
      }
      else
      {
        s+=x[i];
        take++;
        i=(i+1)%n;
      }
    }
    printf("Case #%d: %I64d\n",test+1,ans);
  }
  return 0;
}

