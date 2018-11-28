#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <string>
#include <list>
#include <stack>
#include <string.h>
#include <stdlib.h>
#include <vector>
#include <utility>
#include <list>
#define INF 0x3fffffff


typedef long long ll;
#define PII pair<int, int>
#define PLL pair<ll, ll>
#define PDD pair<double, double>
#define PIL pair<int, ll>
#define PLI pair<ll, int>
#define PID pair<int, double>
#define PDI pair<double, int>
#define PLD pair<ll, double>
#define PDL pair<double, ll>

#define PQ(x) priority_queue< x >  //highest first
#define PQR(x) priority_queue< x , vector< x > , greater < x > > //lowest first
#define V(x) vector< x > 
#define L(x) list< x > 
#define MP make_pair
#define PB push_back
#define IT(x) for (typeof((x).begin()) it = (x).begin() ; it != (x).end() ; it++)
#define IT2(x) for (typeof((x).begin()) it2 = (x).begin() ; it2 != (x).end() ; it2++)
#define FOR(i, a, b) for (int i = (a) ; i< (b) ; i++)
//#define DEB(x...) fprintf(stderr,x);
#define DEB

using namespace std;

struct frac{

  ll ob,unt;
  frac(ll o, ll u)
  {
    ob=o;
    unt=u;
  }
  bool operator<(frac o) const
  {
    DEB("[%lli %lli] < [%lli %lli] = %s\n", ob, unt, o.ob, o.unt, (ob*o.unt < o.ob*unt)?"true":"false");
    
    return ob*o.unt < o.ob*unt;
  }
};


bool testc(int nr)
{
  ll l,p,c;
  scanf("%lli %lli %lli ", &l, &p, &c);
  ll cnt=0;
  for (;frac(c,1)<frac(p,l);)
    {
      double f = sqrt((1.*p)/(1.*l));

      ll mid, mid1, mid2;
      mid1=(ll)(f*l);
      mid2=mid1+1;
      
      
      //      if (max(mid1/l, p/mid1) < max(mid2/l, p/mid2))
      if (max(frac(mid1, l), frac(p, mid1)) < max(frac(mid2, l), frac(p, mid2)))
        mid=mid1;
      else
        mid=mid2;

      if ( frac(mid, l) < frac(p, mid))
        l=mid;
      else
        p=mid;

      DEB("ASK %lli\n",mid);

      cnt++;
    }


  printf("Case #%i: %lli\n", nr, cnt);
}


int main()
{
  int t;
  scanf("%i ",&t);
  FOR(i,0,t)
    testc(i+1);

  /*
    while(testc());
  */
  
  return 0;
}
