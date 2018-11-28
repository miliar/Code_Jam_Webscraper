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

int main()
{
  int NNN;
  cin>>NNN;
  for (int ca=1; ca<=NNN; ++ca)
  { int n;
    cin>>n;
    string s[100];
    Fori(n)
      cin>>s[i];
    double wp[100], owp[100], xwp[100];
    cout<<"Case #"<<ca<<":"<<endl;
    for (int d=0; d<n; ++d)
    { Fori(n)
      { wp[i]=0;
        int ile=0;
        for (int j=0; j<n; ++j)
          if (j!=d && s[i][j]!='.')
          { ++ile;
            wp[i]+=s[i][j]-'0';
          }
        wp[i]/=ile;
      }
      xwp[d]=wp[d];
      int ile=0;
      owp[d]=0;
      Fori(n)
        if (s[d][i]!='.')
        { ++ile;
          owp[d]+=wp[i];
        }
      owp[d]/=ile;
    }
    for (int d=0; d<n; ++d)
    {
      int ile=0;
      double oo=0;
      Fori(n)
        if (s[d][i]!='.')
        { ++ile;
          oo+=owp[i];
        }
      oo/=ile;
      cout<<setiosflags(ios::fixed)<<setprecision(8)<<(0.25*xwp[d]+0.5*owp[d]+0.25*oo)<<endl; 
    }
  }


  return 0;
}
