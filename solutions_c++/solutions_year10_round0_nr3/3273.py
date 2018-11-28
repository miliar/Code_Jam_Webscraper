#include<cstdio>
#include<algorithm>
#include<iostream>
using namespace std;

typedef long long ll;

ll sum[1001];
ll war[1001];
ll wyn[1000005];
ll wynik;

int main()
{
  int z;
  scanf("%d",&z);
  for(int t=1;t<=z;t++)
  {
    ll N,k,R,pos=0;
    ll curr=0,maxim,szuk;
    scanf("%lld %lld %lld",&R,&k,&N);
    for(int i=0;i<N;i++)scanf("%lld",&war[i]);
    sum[0]=war[0];
    for(int i=1;i<N;i++)sum[i]=sum[i-1]+war[i];
    wynik=0;maxim=sum[N-1];
    if(ll(k)>=maxim){printf("Case #%d: %lld\n",t,ll(R*min(maxim,k)));continue;}
    for(int i=1;i<=R;i++)
    {
      wyn[i]=0;
      if(i!=1 && pos==0 && curr==0)
      {
//        printf("WYNIK: %lld\n",wynik);
        ll e=(i-1);
        ll f=R/e;
        R=int(R%e);
        wynik=ll(f*wynik)+wyn[R];
        break;
      }
      szuk=k;
//      printf("\n1:i:%d curr:%lld maxim:%lld szuk:%lld wynik:%lld pos:%d\n",i,curr,maxim,szuk,wynik,pos);
      if(curr+szuk>=maxim)
      {
        wynik+=maxim-curr;
        szuk-=maxim-curr;
        curr=0;
        pos=0;
      }
      ll newpos=upper_bound(sum+pos,sum+N,curr+szuk)-sum;
      wynik+=sum[newpos-1]-curr;
      curr=sum[newpos-1];
      pos=newpos;
      wyn[i]=wynik;
//      printf("\n2: curr:%lld maxim:%lld szuk:%lld wynik:%lld pos:%d\n",curr,maxim,szuk,wynik,pos);
    }
    printf("Case #%d: %lld\n",t,wynik);
  }
  return 0;
}
