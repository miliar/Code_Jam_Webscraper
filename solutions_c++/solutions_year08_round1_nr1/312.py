#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

#define LL long long

class CMP2
{
public:
  bool operator () (const LL &a, const LL &b)
  { return a>b; }
};

int n;
vector<LL> x,y;

int main()
{
  int tt;
  scanf("%d",&tt);
  LL tmp;
  for(int t=1;t<=tt;t++) {
    scanf("%d",&n);
    x.clear(); y.clear();
    for(int i=0;i<n;i++)
      { scanf("%lld",&tmp); x.push_back(tmp); }
    for(int i=0;i<n;i++)
      { scanf("%lld", &tmp); y.push_back(tmp); }

    sort(x.begin(),x.end());
    sort(y.begin(),y.end(),CMP2());

    LL res=0;
    for(int i=0;i<n;i++)
      res+=x[i]*y[i];
    printf("Case #%d: %lld\n", t, res);
  }
  return 0;
}
