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

const int M=20000;
int g[20000], c[20000], ii[20000], v;
bool zm[20000];

int licz(int k)
{ if (ii[k]==v) return 0;
  if (!zm[k]) return M;
  int a=licz(2*k), b=licz(2*k+1);
  if (a>=M && b>=M) return M;
  if (v)
  { int wyn=a+b;
    if (c[k] && g[k]==1) wyn=min(wyn, 1+min(a, b));
    if (g[k]!=1) wyn=min(wyn, min(a, b));
    return wyn;
  }
  int wyn=a+b;
  if (c[k] && g[k]!=1) wyn=min(wyn, 1+min(a, b));
  if (g[k]==1) wyn=min(wyn, min(a, b));
  return wyn;
}

int main()
{
  int n;
  cin>>n;
  for (int ca=1; ca<=n; ++ca)
  { int m;
    cin>>m>>v;
    int wew=(m-1)/2, lis=(m+1)/2;
    for (int i=1; i<=wew; ++i)
      cin>>g[i]>>c[i];
    for (int i=wew+1; i<=m; ++i)
    { cin>>ii[i];
      zm[i]=false;
    }
    for (int i=wew; i>0; --i)
    { if (c[i]) zm[i]=true;
      else zm[i]=zm[i*2] || zm[i*2+1];
      if (g[i]==1) ii[i]=ii[2*i] && ii[2*i+1];
      else ii[i]=ii[2*i] || ii[2*i+1];
    }
    int x=licz(1);
    cout<<endl<<"Case #"<<ca<<": ";
    if (x>=M) cout<<"IMPOSSIBLE";
    else cout<<x;
    cout<<endl;
  }

  char ccccc;
  cin>>ccccc;

  return 0;
}
