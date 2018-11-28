#include<stdio.h>
#include<string>
#include<stdlib.h>
#include<iostream>
#include<string.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
typedef long long LL;
const double EPS = 1e-8;
const int INF = (1<<29);

long long a[1000];

long long pow(long long a,long long b,long long p){
  if (b==0) return 1;
  if (b==1) return a;
  long long y = pow(a,b/2,p);
  if (b%2==0) return y*y%p;
  return y*y%p*a%p;
}

long long inv(long long a,long long p){ 
  return pow(a,p-2,p); 
}

int d,n;
bool prime[1000010];

int main(){
  memset(prime,1,sizeof(prime));
  for (LL i=2; i<=1000000; i++){
    if (!prime[i]) continue;
    for (LL j=i*i; j<=1000000; j+=i) prime[j]=false;
  }
  int ca; scanf("%d",&ca);
  for (int tt=1; tt<=ca; tt++){
    printf("Case #%d: ",tt);
    scanf("%d%d",&d,&n);
    LL mx=0;
    for (int i=0; i<n; i++){
      scanf("%lld",&a[i]);
      if (a[i]>mx) mx=a[i];
    }
    int m=1;
    for (int t=d, i=0; i<t; i++) m*=10;
    if (n==1){ printf("I don't know.\n"); continue; }
    if (n==2){ 
      if (a[0]==a[1]) printf("%lld\n",a[0]);
      else printf("I don't know.\n"); 
      continue; 
    }
    if (a[0]==a[1]){
      bool ok=true;
      for (int i=2; i<n; i++){
        if (a[i]!=a[0]) ok=false;
      }
      if (ok) printf("%lld\n",a[0]);
      else printf("I don't know.\n");
      continue;
    }
    LL ans=-1;
    for (LL i=mx+1; i<=m; i++){
      if (!prime[i]) continue;
      LL A=((a[2]-a[1])*inv(a[1]-a[0]+i*10000ll,i)+i*1000000ll)%i;
      LL B=(a[1]-a[0]*A+i*10000000ll)%i;

      LL S=a[0];
      bool ok=true;
      for (int j=1; j<n; j++){
        S=(S*A+B)%i;
        if (S!=a[j]) ok=false;
      }
      if (ok){
        if (ans==-1) ans = (a[n-1]*A+B)%i;
        else if ((a[n-1]*A+B)%i != ans){ ans=-1; break; }
      }
    }
    if (ans!=-1){
      printf("%lld\n",ans);
    }else{
      printf("I don't know.\n");
    }
  }
  return 0;
}
