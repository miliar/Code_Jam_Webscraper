#include <algorithm>
#include <iostream>
#include <vector>
#include <map>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned long ul;
typedef unsigned short us;
typedef unsigned char uc;

typedef pair<int,int> walk; // boost, len

walk W[100001];

main()
{
  int cases;
  cin >> cases;
  for(int loop=1; loop<=cases; loop++)
  {
    int x, n; double t,s,r;
    cin >> x >> s >> r >> t >> n;

    int rem=x;
    for(int i=1;i<=n;i++)
    {
      int b,e,w; cin>>b>>e>>w; int l=e-b;
      rem-=l; W[i]=make_pair(w,l);
    }
    W[0] = make_pair(0,rem);
    n++; sort(W,W+n);

    double tim=0;
    for(int i=0;i<n;i++)
    {
      int b=W[i].first, l=W[i].second;
      if (t>0)
      {
        double used = min(t,l/(b+r)); t -= used;
        double ran = used*(b+r), still = l-ran;
        tim += used + still/(b+s);
      }
      else tim += l/(b+s);
    }

    printf("Case #%d: ",loop);
    printf("%0.6lf\n",tim);
    // puts("");
  }
}
