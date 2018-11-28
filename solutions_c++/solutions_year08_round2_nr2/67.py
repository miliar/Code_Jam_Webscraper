#include<algorithm>
#include<cstdlib>
#include<iostream>
#include<map>
#include<sstream>
#include<set>
#include<string>
#include<numeric>
#include<vector>
#include<cmath>

#define PB push_back
#define SZ(x) int((x).size())
#define ALL(a) (a).begin(),(a).end()
#define REP(i,n) for(int i=0;i<(n);i++)

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;

bool isprime(ll a){
  if(a==2)
    return 1;
  if(a%2==0)
    return 0;
  for(ll n=3;n*n<=a;n+=2)
    if(a%n==0)
      return 0;
  return 1;
}

int par[1000005];

int p(int a){
  return par[a]==a?a:par[a]=p(par[a]);
}

int _un(ll a,ll b) {
  int pa=p(a),pb=p(b);
  if(pa!=pb)
    {
      par[pa]=pb;
      return 1;
    }
  return 0;
}

int main()
{
  int T;
  scanf("%d", &T);
  for(int t = 1 ; t <= T ; t++)
    {
      printf("Case #%d: ", t);
      ll A,B,P;
      scanf("%lld%lld%lld", &A, &B, &P);
      int N=B-A+1;
      REP(i,B-A+1)
        par[i]=i;
      for(ll p=P;p<=B-A;p++)
        if(isprime(p))
          {
            ll k=(A/p);
            if(p*k<A)
              k++;
            for(ll u=k+1;p*u<=B;u++)
              N-=_un(p*k-A,p*u-A);
          }
      printf("%d",N);
      puts("");
    }

  return 0;
}
