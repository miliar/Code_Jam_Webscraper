#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<cmath>
#include<vector>
#include<set>
#include<map>
#include<list>
#include<deque>
#include<queue>
#include<stack>
#include<functional>
#include<sstream>
#include<iostream>
#include<ctime>
#include<algorithm>
using namespace std;

#define DEBUG(x...) printf(x)
#define allv(v) (v).begin(),(v).end()
#define rall(v) (v).begin(),(v).rend()
#define _foreach(it,b,e) for(__typeof__(b); it!=(e);++it)
#define foreach(x...) _foreach(x)

typedef long long int huge;

const int inf = 0x3f3f3f3f;
const huge hugeinf = 0x3f3f3f3f3f3f3f3fll;//dois L's
const double eps = 1e-9;
const int maxn = 9999;

int n;
double sum[maxn];
struct xxx{
  int l,p,id;
  double s;
}gaga[maxn];
void calc(int i) {
  double p = gaga[i].p/100.0;
  gaga[i].s=0;
  double at = 1 - p;
  for(int j=1;j<10000;j++){
    gaga[i].s += j*at;
    at *= p;
  }
}

int dc(double a, double b){
  if( fabs(a-b) <eps)return 0;
  else return 1;
}
bool comp (xxx a, xxx b){
  double t = a.s * a.l;
  double r = b.s * b.l;
  //  printf("%d %d %lf %lf\n",a.id,b.id,t +  b.s*(b.l+t),r +  a.s*(a.l+r));
  if( dc(b.s*(b.l+t), a.s*(a.l+r))==0 ) return a.id<b.id;
  return b.s*(b.l+t) < a.s*(a.l+r);
}
int main ()
{
  int tt;
  scanf("%d",&tt);
  for(int pp=1;pp<=tt;pp++)
    {
      scanf("%d",&n);
      for(int i=0;i<n;i++){
        scanf("%d",&gaga[i].l);
        gaga[i].id=i;
      }
      for(int i=0;i<n;i++)
        scanf("%d",&gaga[i].p);
      for(int i=0;i<n;i++){
        calc(i);
      }
      sort(gaga,gaga+n, comp);
      printf("Case #%d:",pp);
      for(int i=0;i<n;i++)
        printf(" %d",gaga[i].id);
      printf("\n");
    }
  return 0;
}
