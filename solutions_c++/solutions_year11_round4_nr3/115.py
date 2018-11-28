#include <stdio.h>
#include <math.h>
#include <vector>
#define ll long long
using namespace std;
bool isprime[1001003];
vector <ll> primes;
ll findnumpp(ll x)
{
  if(x==1)
    return 1;
  ll ct=1;
  for(ll i=0;primes[i]*primes[i]<=x;i++)
    {
      //printf("%lld\n",primes[i]);
      for(ll j=primes[i];j<=x;j*=primes[i])
	ct++;
    }
  return ct;
}

ll findnump(ll x)
{
  if(x==1)
    return 1;
  ll ct=0;
  for(ll i=0;primes[i]*primes[i]<=x;i++)
    ct++;
  return ct;
}


int main()
{
  for(ll i=2;i<=1000122;i++)
    isprime[i]=true;
  for(ll i=2;i<=1000122;i++)
    for(ll j=i;j<=1000122/i;j++)
      isprime[i*j]=false;
  for(ll i=2;i<=1000122;i++)
    if(isprime[i])
      primes.push_back(i);
  

  ll T;
  scanf("%lld",&T);
  for(ll t=1;t<=T;t++)
    {
      ll N;
      scanf("%lld",&N);
      //int minn=findnump(N);
      printf("Case #%lld: %lld\n",t,findnumpp(N)-findnump(N));



    }
     
}
