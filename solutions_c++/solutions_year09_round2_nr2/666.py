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
  { string s;
    cin>>s;
    cout<<"Case #"<<ca<<": ";
    
  /*  bool ze=true;
    for (int i=1; i<s.size(); ++i)
      if (s[i]!='0') ze=false;
    if (ze)
    { cout<<s<<'0'<<endl;
      continue;
    } */
    
    
    char ma=s[s.size()-1];
    int poz=s.size()-2;
    while (poz>=0 && s[poz]>=ma)
    { ma=max(ma, s[poz]);
      --poz;
    }
    if (poz<0)
    { sort(s.begin(), s.end());
      if (s[0]=='0')
      { Fori(s.size())
          if (s[i]!='0')
          { swap(s[0], s[i]);
            break;
          }
      }
      cout<<s[0]<<'0'<<s.substr(1)<<endl;
    }
    else
    { int poz1=-1;
      for (int i=poz+1; i<s.size(); ++i)
        if (s[i]>s[poz] && (poz1==-1 || s[poz1]>s[i])) poz1=i;
      swap(s[poz], s[poz1]);
      sort(s.begin()+poz+1, s.end());
      cout<<s<<endl;
    }
  }
  return 0;
}
