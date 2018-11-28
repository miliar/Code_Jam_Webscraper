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
  char comb[40][40];
  int oppose[40][40];
  for (int ti=0;ti<t;++ti)
  {
    memset(comb,0,sizeof(char)*40*40);
    int c;
    is>>c;
    for (int i=0;i<c;++i)
    {
      string s;
      is>>s;
      comb[s[0]-'A'][s[1]-'A']=s[2];
      comb[s[1]-'A'][s[0]-'A']=s[2];
    }

    memset(oppose,0,sizeof(int)*40*40);
    int d;
    is>>d;
    for (int i=0;i<d;++i)
    {
      string s;
      is>>s;

      oppose[s[0]-'A'][s[1]-'A']=1;
      oppose[s[1]-'A'][s[0]-'A']=1;
    }

    int n;
    is>>n;
    string s;
    is>>s;
    
    string res;
    //vector<bool> exists(40,false);
    for (int i=0;i<n;++i)
    {
      char c= s[i];
      res.push_back(c);
      while (res.size()>=2 && comb[res[res.size()-1]-'A'][res[res.size()-2]-'A'])
      {
        res[res.size()-2]=comb[res[res.size()-1]-'A'][res[res.size()-2]-'A'];
        res.resize(res.size()-1);
      }

      for (unsigned int i=0;i<res.size();++i)
        if (oppose[res[i]-'A'][res[res.size()-1]-'A'])
        {
          res.clear();
          break;
        }
    }

    os << "Case #"<<ti+1<<": [";
    for (unsigned int i=0;i<res.size();++i)
    {
      os<<res[i];
      if (i+1<res.size())
        os<<", ";
    }
    //xor==0?os<<s-min_:os<<"NO";
    os<<"]\n";
  }
}

//void main()
//{
//  ifstream is("a.in");
//  ofstream os("a.out");
//
//  int t;
//  is>>t;
//  for (int ti=0;ti<t;++ti)
//  {
//    int n;
//    is>>n;
//    int s=0;
//    int xor=0;
//    int min_=10000000;
//    for (int i=0;i<n;++i)
//    {
//      int c;
//      is>>c;
//      min_=min(min_,c);
//      s+=c;
//      xor^=c;
//    }
//
//    os << "Case #"<<ti+1<<": ";
//    xor==0?os<<s-min_:os<<"NO";
//    os<<"\n";
//  }
//}

//void main()
//{
//  ifstream is("a.in");
//  ofstream os("a.out");
//
//  int t;
//  is>>t;
//  for (int ti=0;ti<t;++ti)
//  {
//    int n;
//    is>>n;
//    vector<pair<char,int> > s;
//    s.resize(n);
//    for (int i=0;i<n;++i)
//    {
//      is>>s[i].first>>s[i].second;
//    }
//
//    int pos0=1;
//    int pos1=1;
//    unsigned int si=0;
//
//    unsigned int s0i=0;
//    unsigned int s1i=0;
//    int time=0;
//    while (si<s.size())
//    {
//      for (; s0i<si||(s0i<s.size()&&s[s0i].first!='O');++s0i);
//      for (; s1i<si||(s1i<s.size()&&s[s1i].first!='B');++s1i);
//
//      if (s0i==si)
//      {
//        if (pos0==s[si].second)
//          ++si;
//        else
//          pos0+=s[si].second>pos0?+1:-1;
//
//        if (s1i<s.size()&&s[s1i].second!=pos1)
//          pos1+=s[s1i].second>pos1?+1:-1;
//      }
//      else
//      {
//        if (pos1==s[si].second)
//          ++si;
//        else
//          pos1+=s[si].second>pos1?+1:-1;
//
//        if (s0i<s.size()&&s[s0i].second!=pos0)
//          pos0+=s[s0i].second>pos0?+1:-1;
//      }
//
//      ++time;
//    }
//
//    os << "Case #"<<ti+1<<": "<<time<<"\n";
//  }
//}