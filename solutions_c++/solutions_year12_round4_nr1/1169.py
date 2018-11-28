#include <assert.h>
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

//////////////////////////////////////////////////////////////////////////

void main()
{
  ifstream is("a.in");
  ofstream os("a.out");

  int t;
  is>>t;

  vector<int> d,l;
  vector<int> min_;

  for (int ti=0;ti<t;++ti)
  {
    //solve
    int n;
    is>>n;
    d.clear();
    l.clear();
    d.resize(n+1);
    l.resize(n+1);
    min_.clear();
    min_.resize(n+1,-1);
    d[0]=0;
    l[0]=0;
    for (int i=1;i<=n;++i)
    {
      is>>d[i]>>l[i];
    }

    double D;
    is>>D;
    //int dst = ceil();

    min_[1]=0;
    bool ok=false;
    for (int i=1;i<=n;++i)
    {
      int j=min_[i];
      if(j>=0)
      {
        int len= min(d[i]-d[j],l[i]);
        if (d[i]+len>=D)
        {
          ok=true;
          break;
        }
        for (int i1=i+1;i1<=n;++i1)
          if (d[i]+len>=d[i1])
          {
            if (min_[i1]<0)
              min_[i1]=i;
          }
          else
            break;
      }
    }

    os << "Case #"<<ti+1<<": "<<(ok?"YES":"NO");
    //out
    os<<"\n";
  }
}


//
////void main()
////{
////  ifstream is("a.in");
////  ofstream os("a.out");
////
////  int t;
////  is>>t;
////
////  for (int ti=0;ti<t;++ti)
////  {
////    //solve
////
////    os << "Case #"<<ti+1<<": ";
////    //out
////    os<<"\n";
////  }
////}
////
