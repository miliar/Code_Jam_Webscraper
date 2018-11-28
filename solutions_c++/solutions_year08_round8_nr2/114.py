#include <algorithm>
#include <limits>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include <iomanip>

using namespace std;

const int MaxInt=numeric_limits<int>::max();
typedef vector<int> VI;
typedef vector<string> VS;
#define For(i,a,n) for (int i=a; i<n; ++i)
#define Fori(n) For(i,0,n)

pair<int, int> p[1000];

int main()
{
//  cout<<fixed;

  int nnn;
  cin>>nnn;
  for (int ca=1; ca<=nnn; ++ca)
  {
    int n, ls=0;
    cin>>n;
    struct S
    { string kol;
      vector<pair<int, int> > odc;
    } s[3000];
    Fori(n)
    { string ss;
      int a, b;
      cin>>ss>>a>>b;
      int j=0;
      while (j<ls && ss!=s[j].kol)
        ++j;
      if (j<ls)
      { s[j].odc.push_back(make_pair(a, b));
      }
      else
      { s[ls].kol=ss;
        s[ls++].odc.push_back(make_pair(a, b));
      }
    }
    int wyn=MaxInt;
    for (int a=0; a<ls; ++a)
    { 
      for (int b=a; b<ls; ++b)
      { 
        for (int c=b; c<ls; ++c)
        { int la=0;
      Fori(s[a].odc.size())
        p[la++]=s[a].odc[i];
        
          int lb=0;
        if (a!=b)
          Fori(s[b].odc.size())
            p[la+lb++]=s[b].odc[i];
            
           int lc=0;
          if (b!=c)
            Fori(s[c].odc.size())
              p[la+lb+lc++]=s[c].odc[i];
          int ll=la+lb+lc;
          sort(p, p+ll);
          int ile=0, ost=0, odc=0;
          while (odc<ll && ost<10000)
          { int nastost=0;
            while (odc<ll && p[odc].first<=ost+1)
            { nastost=max(nastost, p[odc++].second);
            }
            if (!nastost) break;
            ++ile;
            ost=nastost;
          }
        
          if (ost==10000)
            wyn=min(wyn, ile);
        }
      }
    }

    cout<<endl<<"Case #"<<ca<<": ";
    if (wyn==MaxInt) cout<<"IMPOSSIBLE"<<endl;
    else cout<<wyn<<endl;
  }

  { char ccccc;
    cin>>ccccc;
  }
  return 0;
}
