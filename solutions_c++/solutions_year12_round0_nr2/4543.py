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

  for (int ti=0;ti<t;++ti)
  {
    int n,s,p;

    int res=0;

    //input
    is >> n>> s>> p;
    for (int i=0;i<n;++i)
    {
      int k;
      is>>k;
      if (k>=p+2*max(p-1,0))
        ++res;
      else if (s>0 && k>=p+2*max(p-2,0))
      {
        ++res;
        --s;
      }
    }

    //solve

    //out
    os << "Case #"<<ti+1<<": ";
    os<<res;
    os<<"\n";
  }
}


//void main()
//{
//  ifstream is("a.in");
//  ofstream os("a.out");
//
//  int t;
//  is>>t;
//
//  for (int ti=0;ti<t;++ti)
//  {
//    //solve
//
//    os << "Case #"<<ti+1<<": ";
//    //out
//    os<<"\n";
//  }
//}

//a
//const string src_ ("ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvq");
//const string dst_ ("our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upz");
//void main()
//{
//  ifstream is("a.in");
//  ofstream os("a.out");
//
//  map<char,char> m;
//  set<char> d;
//  for (unsigned int i=0;i<src_.size();++i)
//  {
//    m[src_[i]]=dst_[i];
//    d.insert(dst_[i]);
//  }
//
//  char src_miss=0;
//  char dst_miss=0;
//  for (char c = 'a';c<='z';++c)
//  {
//    if (m.find(c)==m.end())
//    {
//      assert(!src_miss);
//      src_miss=c;
//    }
//    if (d.find(c)==d.end())
//    {
//      assert(!dst_miss);
//      dst_miss=c;
//    }
//  }
//  m[src_miss]=dst_miss;
//
//  int t;
//  is>>t;
//
//  char src[1000];
//  is.getline(src,1000);//для перехода
//
//  for (int ti=0;ti<t;++ti)
//  {
//    //string src;
//    //is >> src; до первого пробела
//
//    is.getline(src,1000);
//
//    os << "Case #"<<ti+1<<": ";
//    for (unsigned int i=0;src[i];++i)
//    {
//      os<<m[src[i]];
//    }
//    os<<"\n";
//  }
//}

