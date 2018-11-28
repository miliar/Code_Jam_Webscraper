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
  {
    int n, w, l;
    pair<int, int> pr[1000];//<promien, indeks>
    bool zam=false;
    int x[1000], y[1000], skad[1000];
    cin>>n>>w>>l;
    Fori(n)
    {
      cin>>pr[i].first;
      pr[i].second=i;
    }
    sort(pr, pr+n);
    Fori(n)
      skad[pr[i].second]=i;
    if (l>w)
    {
      zam=true;
      swap(l, w);
    }
    int le=-1000000, pra=0, gora=-1000000;
    Fori(n)
    {
      int p=pr[i].first, xx=max(0, le+p), yy=max(0, gora+p);
      if (yy>l)
      {
        le=pra;
        xx=le+p;
        yy=0;
      }
      pra=xx+p;
      gora=yy+p;
      x[i]=xx;
      y[i]=yy;
      if (xx>w || yy>l)
        throw "Blad.";
    }
    cout<<"Case #"<<ca<<": ";
    if (zam) Fori(n) cout<<y[skad[i]]<<' '<<x[skad[i]]<<' ';
    else Fori(n) cout<<x[skad[i]]<<' '<<y[skad[i]]<<' ';
    cout<<endl;
  }

  return 0;
}
