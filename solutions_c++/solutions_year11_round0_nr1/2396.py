#include <vector>
#include <list>
#include <map>
#include <math.h>
#include <set>
#include <string>
#include <sstream>
#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;
#define max(a,b)    (((a) > (b)) ? (a) : (b))
#define min(a,b)    (((a) < (b)) ? (a) : (b))
#define sqr(a)    ((a)*(a))

void main()
{
  ifstream is("a.in");
  ofstream os("a.out");

  int t;
  is>>t;
  for (int ti=0;ti<t;++ti)
  {
    int n;
    is>>n;
    vector<pair<char,int> > s;
    s.resize(n);
    for (int i=0;i<n;++i)
    {
      is>>s[i].first>>s[i].second;
    }

    int pos0=1;
    int pos1=1;
    unsigned int si=0;

    unsigned int s0i=0;
    unsigned int s1i=0;
    int time=0;
    while (si<s.size())
    {
      for (; s0i<si||(s0i<s.size()&&s[s0i].first!='O');++s0i);
      for (; s1i<si||(s1i<s.size()&&s[s1i].first!='B');++s1i);

      if (s0i==si)
      {
        if (pos0==s[si].second)
          ++si;
        else
          pos0+=s[si].second>pos0?+1:-1;

        if (s1i<s.size()&&s[s1i].second!=pos1)
          pos1+=s[s1i].second>pos1?+1:-1;
      }
      else
      {
        if (pos1==s[si].second)
          ++si;
        else
          pos1+=s[si].second>pos1?+1:-1;

        if (s0i<s.size()&&s[s0i].second!=pos0)
          pos0+=s[s0i].second>pos0?+1:-1;
      }

      ++time;
    }

    os << "Case #"<<ti+1<<": "<<time<<"\n";
  }
}