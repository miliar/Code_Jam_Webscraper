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
bool ans[100];
int main()         
{
  /*#ifdef DEBUG
  freopen(taskname".in","r",stdin);                         
  freopen(taskname".out","w",stdout);
  #endif*/
  int t,n,k;
  scanf("%d",&t);
  forn(i,t)
  {
    scanf("%d%d",&n,&k);
    memset(ans,0,sizeof(ans));
    forn(j,k)
    {
      int t=0;
      do
      {  
        ans[t]^=1;
        t++;
      } while(t<n&&!ans[t-1]);
    }
    bool fl=true;
    forn(j,n)
      if(!ans[j])
        fl=false;
    if(n==1)
      if(k%2==1)
        assert(fl);
    printf("Case #%d: %s\n",i+1,(fl)?"ON":"OFF");
  }
  return 0;
}

