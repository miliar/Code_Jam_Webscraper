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

int h, w, wys[100][100]/*[h][w]*/;
char wyn[100][100], nast;

char wynik(int hh, int ww)
{ if (wyn[hh][ww]) return wyn[hh][ww];
  int mi=wys[hh][ww];
  if (hh>0) mi=min(mi, wys[hh-1][ww]);
  if (ww>0) mi=min(mi, wys[hh][ww-1]);
  if (ww<w-1) mi=min(mi, wys[hh][ww+1]);
  if (hh<h-1) mi=min(mi, wys[hh+1][ww]);
  if (mi==wys[hh][ww]) return wyn[hh][ww]=nast++;
  if (hh>0 && mi==wys[hh-1][ww]) return wyn[hh][ww]=wynik(hh-1, ww);
  if (ww>0 && mi==wys[hh][ww-1]) return wyn[hh][ww]=wynik(hh, ww-1);
  if (ww<w-1 && mi==wys[hh][ww+1]) return wyn[hh][ww]=wynik(hh, ww+1);
  return wyn[hh][ww]=wynik(hh+1, ww);
}

int main()
{
  int NNN;
  cin>>NNN;
  for (int ca=1; ca<=NNN; ++ca)
  {
    
    cin>>h>>w;
    for (int hh=0; hh<h; ++hh)
      for (int ww=0; ww<w; ++ww)
        cin>>wys[hh][ww];
        
    memset(wyn, 0, sizeof(wyn));
    nast='a';

    cout<<"Case #"<<ca<<": "<<endl;
    for (int hh=0; hh<h; ++hh)
    { for (int ww=0; ww<w; ++ww)
        cout<<wynik(hh, ww)<<' ';
      cout<<'\n';
    }
    
  }


  return 0;
}
