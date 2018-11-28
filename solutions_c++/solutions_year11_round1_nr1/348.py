#include<stdio.h>
typedef long long ll;
ll n,pd,pg;
int t;
ll mind,maxg;
ll gcd(ll a,ll b){
  if (b==0) return a;
  else return gcd(b,a%b);
}
int main(){
  freopen("a.in","r",stdin);
  freopen("a.out","w",stdout);
  int ca=0;
  scanf("%d",&t);
  while (t--){
    ca++;
    scanf("%lld%lld%lld",&n,&pd,&pg);
    if (pd==0&&pg<100){
      printf("Case #%d: Possible\n",ca);
      continue;
    }
    if (pg==0&&pd>0){
      printf("Case #%d: Broken\n",ca);
      continue;
    }
    if (pg==100&&pd<100){
      printf("Case #%d: Broken\n",ca);
      continue;
    }
    ll d1=gcd(pd,100);
    mind=100/d1;
    if (mind<=n){
      printf("Case #%d: Possible\n",ca);
      continue;
    }
    else{
      printf("Case #%d: Broken\n",ca);
      continue;
    }
  }
  return 0;
}
