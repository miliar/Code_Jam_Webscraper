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

struct K
{ int x, y, rozm;
  bool operator<(const K &k) const 
  { if (rozm!=k.rozm) return rozm>k.rozm;
    if (y!=k.y) return y<k.y;
    return x<k.x;
  }
} kb[1000000];

int szer[512][512];
set<K> sk;

int main()
{
  int NNN;
  cin>>NNN;
  for (int ca=1; ca<=NNN; ++ca)
  {
    K k;
    
    int m, n;
    cin>>m>>n;
    bool tab[512][512], wyc[512][512]={};//[y][x]
    Fori(m)
    { string s;
      cin>>s;
      for (int j=0; j<n/4; ++j)
      { int a=s[j]-'0';
        if (a>9) a=s[j]-'A'+10;
        tab[i][j*4]=bool(a&8);
        tab[i][j*4+1]=bool(a&4);
        tab[i][j*4+2]=bool(a&2);
        tab[i][j*4+3]=bool(a&1);
      }
      szer[i][n-1]=1;
      for (int j=n-2; j>=0; --j)
        if (tab[i][j]!=tab[i][j+1]) szer[i][j]=szer[i][j+1]+1;
        else szer[i][j]=1;
    }
    for (int x=0; x<n; ++x)
      for (int y=0; y<m; ++y)
      { int rozm=min(szer[y][x], m-y);
        for (int wys=2; wys<=rozm; ++wys)
        { if (tab[y+wys-2][x]==tab[y+wys-1][x]) rozm=wys-1;
          else rozm=min(rozm, max(wys-1, szer[y+wys-1][x]));
        }
        k.rozm=rozm;
        k.x=x;
        k.y=y;
        sk.insert(k);
      }
    int ile[513]={}, bylo=0;
  
    while (!sk.empty())
    { 
      k=*sk.begin();
      int ro=k.rozm;
      if (k.rozm<1)
      { for (int y=k.y; y<k.y+ro; ++y)
          for (int x=k.x; x<k.x+ro; ++x)
            if (wyc[y][x])
            { ro=max(y-k.y, x-k.x);
            }      
      }
      else
      { 
        for (int j=0; j<bylo; ++j)
          if (kb[j].x<=k.x && kb[j].x+kb[j].rozm>k.x && kb[j].y<=k.y && kb[j].y+kb[j].rozm>k.y)
          { j=bylo;
            ro=0;
          }
          else
          { int sz=kb[j].x-k.x, wy=kb[j].y-k.y;
            if (!(kb[j].x>=k.x+k.rozm || kb[j].y>=k.y+k.rozm || k.x>=kb[j].x+kb[j].rozm || k.y>=kb[j].y+kb[j].rozm)) ro=min(ro, max(sz, wy));
          
          }
      }
      sk.erase(sk.begin());
      if (ro==0)
      { 
        continue;
      }
      if (ro!=k.rozm)
      { k.rozm=ro;
        sk.insert(k);
        continue;
      }
      //cout<<k[i].x<<' '<<k[i].y<<' '<<k[i].rozm<<endl;
      ++ile[k.rozm];
      kb[bylo++]=k;
      for (int y=k.y, yy=k.y+k.rozm, xx=k.x+k.rozm; y<yy; ++y)
        for (int x=k.x; x<xx; ++x)
          wyc[y][x]=true;
    }
  
    int u=0;
    for (int i=512; i>0; --i)
      if (ile[i]) ++u;
    cout<<"Case #"<<ca<<": "<<u<<endl;
    for (int i=512; i>0; --i)
      if (ile[i]) cout<<i<<' '<<ile[i]<<endl;
  }
  return 0;
}
