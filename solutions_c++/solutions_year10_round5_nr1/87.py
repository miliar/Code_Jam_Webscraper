#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <map>
#include <utility>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>

using namespace std;

#define CLEAR(X) memset(X,0,sizeof(X))
#define REP(i,n) for(int i=0;i<(n);i++) 
template <class T> vector<T>parse(string s,const char d=' '){
  vector<T> v; string p; s+=d; int i=0; 
  while(i<(int)s.size())
    if (s[i] == d){stringstream u; u<<p; T t; u>>t; v.push_back(t); p=""; while(i<(int)s.size() && s[i]==d)i++;} else p+=s[i++];   
  return v;
} 

typedef long long ll;
typedef long double ld;

bool z[1000100];
ll p[100000];
ll ps=0;

ll pow(ll a, ll b, ll p){
  if(b==0)return 1;
  if(b==1)return a%p;
  ll x=pow(a,b/2,p);
  x*=x;  x%=p;
  if(b%2)return (x*a)%p;
  return x;
}
ll s[20],k,d,to;

bool match(int a, int b, int p){
  ll v=s[0];
  for(ll i=1;i<k;i++){
    ll nv=(a*v+b)%p;
    if(nv!=s[i])return false;
    v=nv;
  }
  return true;
}

int main(){
  CLEAR(z);
  for(ll i=2;i*i<=1000000;i++)
    if(!z[i])for(ll j=2*i;j<=1000000;j+=i)z[j]=true;
  for(ll i=2;i<=1000000;i++)if(!z[i])p[ps++]=i;
  ll _cases; scanf("%lld",&_cases);
  for(ll _case=1;_case<=_cases;_case++){
    printf("Case #%lld:",_case);
    scanf("%lld%lld",&d,&k);
    to = pow(10,d,1000000000);
    REP(i,k)scanf("%lld",&s[i]);
    if(k==1){
      printf(" I don't know.\n");
      continue;
    }
    if(s[0]==s[1]){
      printf(" %lld\n",s[0]);
      continue;
    }
    if(d<=3){
      ll cnt=0;
      ll fv=-1;
      for(ll i=0;p[i]<=to && cnt<=1;i++){
        for(ll a=0;a<p[i];a++){
          if(s[0]>=p[i])continue;
          ll b=s[1]-a*s[0];
          b%=p[i];b+=p[i];b+=p[i];b%=p[i];
          //for(ll b=1;b<p[i];b++)
           if(match(a,b,p[i])){
        
            ll curv = (a*s[k-1]+b)%p[i];
            if(curv!=fv)cnt++;
            fv=curv;
          }
      }
      }
      if(cnt!=1)printf(" I don't know.\n");
      else printf(" %lld\n", fv);
      continue;
    }
    if(k==2){
      printf(" I don't know.\n");
      continue;
    }
    ll cnt=0;
    ll fv=-1;
    for(ll i=0;p[i]<=to;i++){
      if(s[0]>=p[i])continue;
      ll inv = ((s[1]-s[0])%p[i]+p[i]*3)%p[i];
      inv=pow(inv, p[i]-2,p[i]);
      ll a = ((s[2]-s[1])%p[i])*inv;
      a%=p[i];a+=p[i];a+=p[i];a+=p[i];a%=p[i];
      ll b=s[1]-a*s[0];
      b%=p[i];b+=p[i];b+=p[i];b%=p[i];
      if(match(a,b,p[i])){
        ll curv = (a*s[k-1]+b)%p[i];
        if(curv!=fv)cnt++;
        fv=curv;
      }
    }
    if(cnt!=1)printf(" I don't know.\n");
    else printf(" %lld\n", fv);
  }
  return 0;
}
