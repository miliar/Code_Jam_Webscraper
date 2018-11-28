#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <math.h>
#include <map>

//#define OMP

#ifdef OMP
#include <omp.h>
#endif

using namespace std;

ifstream fi;
ofstream fo;

class Csolve
{
public:
  int t;
  string txt;
  
  void solve()
  {
    string s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
    string s2 = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";
    char tbl[256] = {0};
    for (int i=0;i<s1.length();i++)
      tbl[s1[i]] = s2[i];
    tbl['y'] = 'a';
    tbl['e'] = 'o';
    tbl['q'] = 'z';
    tbl['z'] = 'q';
    for (int i=0;i<txt.length();i++)
      txt[i] = tbl[ txt[i] ];
  }
  
  void readInput(int _t)
  {
    t = _t;
    char buf[1024];
    fi.getline(buf, 1024);
    txt = buf;
  }
  
  void writeOutput()
  {
    fo << "Case #" << (t+1) << ": ";
    fo << txt;
    fo << endl;
  }
};


int main(int argc, char *argv[])
{
  //fi.open("test.txt");  fo.open("test.out");
  fi.open("A0.in");  fo.open("A0.out");
  //fi.open("A1.in");  fo.open("A1.out");
   
  Csolve solv[8];
  int T;
  fi >> T;
  char empty[64];
  fi.getline(empty, 64);
  
  int si = 0;
  for (int i=0;i<T;i++)
  {
    solv[si++].readInput(i);
    if (si==8)
    {
#ifdef OMP
      #pragma omp parallel num_threads(8)
      {
          int j;
          j = omp_get_thread_num();
#else
      for (int j=0;j<si;j++)
      {
#endif
        solv[j].solve();
      }
      
      for (int j=0;j<si;j++)
        solv[j].writeOutput();
      si = 0;
    }
  }

#ifdef OMP
#pragma omp parallel num_threads(si)
  {
      int j;
      j = omp_get_thread_num();
#else
  for (int j=0;j<si;j++)
  {
#endif
      solv[j].solve();
  }

  for (int j=0;j<si;j++)
    solv[j].writeOutput();
  
  fo.close();
  fi.close();


 return 0;
}
