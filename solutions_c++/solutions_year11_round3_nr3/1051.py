#include<cassert>
#include<queue>
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

#define sqr(a) ((a)*(a))
#define mp(a,b) make_pair(a,b) 
#define forn(i,n) for(int i=0;i<(int)n;i++)
#define taskname ""
#ifdef DEBUG
#define deb(x) cerr<<#x<<'='<<x<<endl
#else
#define deb(x) 
#endif
typedef long long ll;

using namespace std;
int n;
int x[10000];
bool check()
{
  forn(j,n)
  {
    //if(x[n]==x[j])
      //return false;
    if(x[n] % x[j] !=0 && x[j]%x[n] !=0)
      return false;
  }
  return true;
}
ll gcd(ll a,ll b)
{
  return b?gcd(b,a%b):a;
}
int main()         
{
//  assert(freopen(taskname"in","r",stdin));
//  assert(freopen(taskname"out","w",stdout));
  int test_n;
  scanf("%d",&test_n);
  forn(test_id,test_n)
  {
    printf("Case #%d: ",test_id+1);
    ll l,r;
    ll k=0;
    cin>>n>>l>>r;
    forn(i,n)
    {
      scanf("%d",&x[i]);
      k=gcd(k,x[i]);
    }
    //x[n]=l+(k-l%k)%k;
    x[n]=l;
    bool fl=true;
    while(x[n]<=r)
    {
      if(check())
      {            
        fl=false;
        printf("%d\n",x[n]);
        break;
      }
      x[n]+=1;
    }  
    if(fl)
      puts("NO");
  }
  return 0;
}

