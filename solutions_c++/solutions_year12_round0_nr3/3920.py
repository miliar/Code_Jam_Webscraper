#include <fstream>
#include <sstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <math.h>
#include <map>

#define OMP

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
  int A,B;
  int ans;
  
  void solve()
  {
    ans = 0;
    stringstream ss2;
    ss2 << A;
    int sz = ss2.str().length();
    for (int n=A;n<B;n++)
    {
      stringstream ss;
      ss << n;
      string s = ss.str();
      vector<int> am;
      for (int i=1;i<sz;i++)
      {
        string s2 = s.substr(i,sz-i) + s.substr(0,i);
        int m = atoi(s2.c_str());
        if (m>n && m<=B && s2[0]!='0' && s[0]!='0') 
        {
          bool bOk = true;
          for (int j=0;j<am.size();j++)
            if (am[j]==m)
            {
              bOk = false;
              break;
            }
          if (bOk)
          {
            ans++;
            am.push_back(m);
          }
        }
      }
    }
  }
  
  void readInput(int _t)
  {
    t = _t;
    fi >> A >> B;
    
  }
  
  void writeOutput()
  {
    fo << "Case #" << (t+1) << ": ";
    fo << ans;
    fo << endl;
  }
};


int main(int argc, char *argv[])
{
  //fi.open("test.txt");  fo.open("test.out");
  fi.open("C1.in");  fo.open("C1.out");
  //fi.open("B1.in");  fo.open("B1.out");
   
  Csolve solv[8];
  int T;
  fi >> T;
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
