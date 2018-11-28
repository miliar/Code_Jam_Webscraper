#include<cstdio>
#include<iostream>
#include<vector>
#include<cstring>
#include<map>

#define S second
#define F first
#define _m make_pair
#define Pll pair<long long,long long>
using namespace std;

Pll kur[1000001];

int main()
{
  int T;
  scanf("%d",&T);
  for(int w=1;w<=T;w++)
  {
    long long n,k,b,t,a1;
    scanf("%lld %lld %lld %lld",&n,&k,&b,&t);
    for(int i=0;i<n;i++){scanf("%lld",&a1);kur[i].F=a1;}
    for(int i=0;i<n;i++){scanf("%lld",&a1);kur[i].S=a1;}
    int licznik=0,swap=0;
    long long swap2=0;
    for(int u=n-1;u>=0 && licznik<k;u--)
    {
      if((b-kur[u].F)<=(t*kur[u].S)){licznik++;swap2+=swap;}
      else swap++;
    }
    printf("Case #%d: ",w);
    if(licznik==k)printf("%lld\n",swap2);
    else printf("IMPOSSIBLE\n");
  }
  return 0;
}
