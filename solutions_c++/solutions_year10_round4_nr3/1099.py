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

struct S
{ int x, y, dl;
  bool operator<(const S &s) const
  { if (y==s.y) return x<s.x;
    return y<s.y;
  }
};

void wstaw(set<S> &odc, S s)
{
        for (;;)
        { S zn;
          zn.x=s.x+s.dl+1;
          zn.y=s.y;
          set<S>::iterator it=odc.lower_bound(zn);
          if (it==odc.begin()) break;
          --it;
          if (it->y<s.y) break;
          if (it->x+it->dl<s.x) break;
          int xx=min(s.x, it->x), dl=max(s.x+s.dl-xx, it->x+it->dl-xx);
          s.x=xx;
          s.dl=dl;
          odc.erase(it);
        }
        odc.insert(s);
}

int main()
{
  int NNN;
  cin>>NNN;
  for (int ca=1; ca<=NNN; ++ca)
  { set<S> odc;
    int r;
    cin>>r;
    for (int i=0; i<r; ++i)
    { int x1, y1, x2, y2;
      cin>>x1>>y1>>x2>>y2;
      for (int y=y1; y<=y2; ++y)
      { S s;
        s.x=x1;
        s.y=y;
        s.dl=x2-x1+1;
        wstaw(odc, s);
      }
    }
    int wyn=0;  
    while (!odc.empty())
    { ++wyn;
   //   for (set<S>::iterator it=odc.begin(); it!=odc.end(); ++it)
     //   cout<<it->x<<' '<<it->y<<' '<<it->dl<<endl;
     // cout<<"++++++++\n";
      set<S> nodc;
      for (set<S>::iterator it=odc.begin(); it!=odc.end(); ++it)
      {
        S s;
        s.y=it->y-1;
        s.x=it->x+1;
        set<S>::iterator po=odc.lower_bound(s);
        bool zm=false;
        if (po==odc.begin())
        { zm=true;
        }
        else
        {
          --po;
          if (po->y!=it->y-1 || po->x+po->dl<=it->x)
          { zm=true;
          }
        }
        s=*it;
        if (zm)
        { if (s.dl>1)
          { --s.dl;
            ++s.x;
            wstaw(nodc, s);
          }
        }
        else wstaw(nodc,s);
        s.y=it->y-1;
        s.x=it->x+it->dl+1;
        po=odc.lower_bound(s);
        if (po==odc.begin()) continue;
        --po;
        if (po->y==it->y-1 && po->x+po->dl>=s.x)
        { s.x=s.x-1;
          s.y=it->y;
          s.dl=1;
          wstaw(nodc, s);
        }  
          
      }
      odc.swap(nodc);
        
    }    
    cout<<"Case #"<<ca<<": "<<wyn<<endl;
  }

  char ccccc;
  cin>>ccccc;

  return 0;
}
