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
#define N 2000
ll x[N];
ll gcd(ll a,ll b)
{
  if(b==0)
    return a;
  return gcd(b,a%b);
}

int main()         
{
  //#ifdef DEBUG
  //freopen(taskname".in","r",stdin);                         
  //freopen(taskname".out","w",stdout);
  //#endif
  int k;
  scanf("%d",&k);
  forn(test,k)
  {  
    int n;
    scanf("%d",&n);
    forn(i,n)
      cin>>x[i];
    sort(x,x+n);
    ll t=0;
    forn(i,n)
      forn(j,i)
        t=gcd(x[i]-x[j],t);
    printf("Case #%d: %I64d\n",test+1,(t-x[0]%t)%t);
  }
  return 0;
}

