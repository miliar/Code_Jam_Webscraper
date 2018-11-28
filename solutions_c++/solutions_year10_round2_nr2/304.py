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
#define N 100
int x[N],v[N];
int n,k,b,t;
bool go(int a)
{
  //cerr<<b-x[a]<<' '<<v[a]*t<<endl;
  if((b-x[a])<=v[a]*t)
    return true;
  return false;
}
int main()         
{
  //#ifdef DEBUG
  /*freopen(taskname".in","r",stdin);                         
  freopen(taskname".out","w",stdout);*/
  //#endif
  int testn;
  scanf("%d",&testn);
  forn(test,testn)
  {
    int ans=0;
    printf("Case #%d: ",test+1);
    scanf("%d %d %d %d",&n,&k,&b,&t);
    forn(i,n)
      scanf("%d",&x[i]);
    forn(i,n)
      scanf("%d",&v[i]);
    for(int i=n-1;i>=0&&k;i--)
    {
      if(go(i))
      {
        //cerr<<i<<endl;
        for(int j=i;j<n-1;j++)
        {
          swap(x[j],x[j]);
          swap(v[j],v[j+1]);
          ans++;
        }
        k--;
        n--;
      }
    }
    if(k)
      printf("IMPOSSIBLE\n");
    else 
      printf("%d\n",ans);  
  }
  return 0;
}

