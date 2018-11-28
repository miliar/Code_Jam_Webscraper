#include <algorithm>
#include <limits>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

const int MaxInt=numeric_limits<int>::max();
typedef vector<int> VI;
typedef vector<string> VS;
#define For(i,a,n) for (int i=a; i<n; ++i)
#define Fori(n) For(i,0,n)

int main()
{
  int NNN;
  cin>>NNN;
  for (int ca=1; ca<=NNN; ++ca)
  { VS cc, dd;
    int c, d, n;
    cin>>c;
    Fori(c)
    { string s;
      cin>>s;
      cc.push_back(s);
    }
    cin>>d;
    Fori(d)
    { string s;
      cin>>s;
      dd.push_back(s);
    }
    string wyn, oper;
    cin>>n>>oper;
    Fori(n)
    { bool pol=false;
      if (!wyn.empty())
        for (int c1=0; c1<c; ++c1)
          if ((wyn[wyn.size()-1]==cc[c1][0] && oper[i]==cc[c1][1]) || (wyn[wyn.size()-1]==cc[c1][1] && oper[i]==cc[c1][0]))
          { wyn[wyn.size()-1]=cc[c1][2];
            pol=true;
            break;
          }
      if (pol) continue;
      wyn+=oper[i];
      for (int d1=0; d1<d; ++d1)
        for (int j=0; j<int(wyn.size())-1; ++j)
          if ((wyn[j]==dd[d1][0] && wyn[wyn.size()-1]==dd[d1][1]) || (wyn[j]==dd[d1][1] && wyn[wyn.size()-1]==dd[d1][0]))
            wyn="";
    }
    cout<<"Case #"<<ca<<": [";
    Fori(wyn.size())
      cout<<(i ? ", ":"")<<wyn[i];
    cout<<"]\n";    
  }
  return 0;
}
