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
  string ss;
  getline(cin, ss);
  for (int ca=1; ca<=NNN; ++ca)
  {
    int t[1000][50];
    memset(t, 0, sizeof(t));
    string g="welcome to code jam", s;
    getline(cin, s);
    
    Fori(s.size()+1)
      t[i][0]=1;
    for (int i=1; i<=s.size(); ++i)
      for (int j=1; j<=g.size(); ++j)
      { t[i][j]=t[i-1][j];
        if (s[i-1]==g[j-1]) t[i][j]+=t[i-1][j-1];  
        t[i][j]%=10000;    
      }
    cout<<"Case #"<<ca<<": ";
    for (int wyn=t[s.size()][g.size()], i=1000; i>0; i/=10)
      cout<<(wyn/i)%10;
    cout<<endl;
  }


  return 0;
}
