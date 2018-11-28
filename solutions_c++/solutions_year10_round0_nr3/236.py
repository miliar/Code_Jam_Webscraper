#include <iostream>
#include <vector>
using namespace std;
typedef unsigned long ul;
typedef unsigned long long ull;

main()
{
  int t; cin >> t;
  for(int count=1;count<=t;count++) 
  {
    int r,k,n; cin >> r >> k >> n;
    ull q=0; vector<ul> g(n); for(int i=0;i<n;i++) { cin >> g[i]; q+=g[i]; }

    ull T=0;

    if (q <= k) T=q*r;
    else
    {
      vector<int> next(n,0); vector<ull> val(n,0);
      for(int i=0;i<n;i++)
      {
        ull v=0; int j; for(j=i;;j=(j+1)%n) { v+=g[j]; if (v>k) break; }
        next[i]=j; val[i]=v-g[j];
      }
      int cur=0, t=0;
      vector<int> first(n,0); vector<ull> acc(n,0);

#ifndef SLOW
      while(r--)
      {
        t++; T+=val[cur];
        if (!first[cur]) { acc[cur]=T; first[cur]=t; cur=next[cur]; }
        else
        {
          int per = t-first[cur]; ull vp = T-acc[cur]; cur=next[cur];
          if (r>=per) { int it = r/per; T += vp*it; r%=per; }
          fprintf(stderr,"Cycle detected of length %d, value %llu\n",per,vp);
          break;
        }
      }
#endif
      while(r-->0)
      {
        T+=val[cur]; cur=next[cur];
      }
    }

    printf("Case #%d: %llu\n",count,T);
  }
}
