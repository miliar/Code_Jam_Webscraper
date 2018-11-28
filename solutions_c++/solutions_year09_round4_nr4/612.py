#include <algorithm>
#include <limits>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

const int MaxInt=numeric_limits<int>::max();
typedef vector<int> VI;
typedef vector<string> VS;
#define For(i,a,n) for (int i=a; i<n; ++i)
#define Fori(n) For(i,0,n)

int n, x[10], y[10], r[10];

double licz(int a, int b)
{ 
  return (r[a]+r[b]+sqrt(0.0+(x[a]-x[b])*(x[a]-x[b])+(y[a]-y[b])*(y[a]-y[b])))/2.0;
}

int main()
{
  cout<<fixed;
  int NNN;
  cin>>NNN;
  for (int ca=1; ca<=NNN; ++ca)
  { 
    cin>>n;
    Fori(n)
      cin>>x[i]>>y[i]>>r[i];
    for (int i=n; i<3; ++i)
    { x[i]=x[0];
      y[i]=y[0];
      r[i]=r[0];
    }
      
    double wyn=100000000;
    wyn=min(wyn, max(licz(1, 2), licz(0, 0)));
    wyn=min(wyn, max(licz(1, 0), licz(2, 2)));
    wyn=min(wyn, max(licz(0, 2), licz(1, 1)));
    cout<<"Case #"<<ca<<": "<<setprecision(5)<<wyn<<endl;
  }
  return 0;
}
