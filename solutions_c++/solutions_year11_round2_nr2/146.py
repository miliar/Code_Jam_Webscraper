#include<stdio.h>
#include<string>
#include<stdlib.h>
#include<iostream>
#include<string.h>
#include<vector>
#include<algorithm>
using namespace std;
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define CLR(s) memset(s,0,sizeof(s))
typedef long long LL;

LL D, p[1000],v[1000];
int n;

int main(){
  int tc; scanf("%d",&tc);
  FOE(ca,1,tc){
    scanf("%d%lld",&n,&D);
    D *= 2;
    FOR(i,0,n){
      scanf("%lld%lld",&p[i],&v[i]);
      p[i] *= 2;
    }
    v[0]--;
    LL lo=0, hi=1ll<<60, ans=1ll<<60;
    while (lo<=hi){
      LL mid = (lo+hi)/2;

      LL now = p[0] - mid;
      bool ok=true;
      FOR(i,0,n){
        FOR(j,0,v[i]){
          now += D;
          if (now < p[i]-mid) now = p[i]-mid;
          if (now > p[i]+mid) ok=false;
        }
      }
      if (ok){ ans=mid; hi=mid-1; }
      else lo=mid+1;
    }
    printf("Case #%d: %lld.%lld\n",ca,ans/2,(ans%2)*5);
  }
  return 0;
}
