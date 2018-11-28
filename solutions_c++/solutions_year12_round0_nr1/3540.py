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
  string s="zy qeeejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
  string c="qa zooour language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";
  char z[256]={};
  Fori(s.size()) z[s[i]]=c[i];
 // for (int i='a'; i<='z'; ++i) if (z[i]==0) cout<<(char) i<<' '<<i<<endl;

  int NNN;
  cin>>NNN;
  string ss;
  getline(cin, ss);
  for (int ca=1; ca<=NNN; ++ca)
  {
    getline(cin, ss);
    Fori(ss.size()) ss[i]=z[ss[i]];
    cout<<"Case #"<<ca<<": "<<ss<<endl;
  }
  return 0;
}
