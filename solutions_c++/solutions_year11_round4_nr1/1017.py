#include "stdafx.h"

#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <math.h>
#include <map>
#include <iomanip>

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
  int xlen , walkS , runS , runT , N;
  double ans;
  struct SWay
  {
	  int B, E;
	  int spd;
  };
  vector<SWay> way;
  
  void solve()
  {
	  vector<int> dt;
	  for (int i=0;i<N;i++)
	  {
		  dt.push_back(way[i].B);
		  dt.push_back(way[i].E);
	  }
	  sort(dt.begin(), dt.end());
	  dt.push_back(xlen);
	  dt.push_back(xlen);
	  for (int i1=0;i1<N;i1++)
		  for (int i2=0;i2<N-1;i2++)
			  if (way[i2].spd>way[i2+1].spd)
			  {
				  swap(way[i2], way[i2+1]);
			  }
      double rt = runT;
	  ans = 0;
	  double prev = 0;
	  for (int i=0;i<dt.size();i+=2)
	  {
		  if (prev<dt[i])
		  {
			  double dist = dt[i] - prev;
			  double timerun = dist / runS;
			  if (timerun<=rt)
			  {
				  ans += timerun;
				  rt -= timerun;
			  }
			  else
			  {
				  double drun = rt * runS;
				  ans += rt;
				  rt = 0;
				  dist -= drun;
				  double timewalk = dist / walkS;
				  ans += timewalk;
			  }
		  }
		  prev = dt[i+1];
	  }
	  for (int i=0;i<way.size();i++)
	  {
		  double dist = way[i].E - way[i].B;
		  double timerun = dist / (way[i].spd + runS);
		  if (timerun<=rt)
		  {
			  ans += timerun;
			  rt -= timerun;
		  }
		  else
		  {
			  double drun = rt * (way[i].spd + runS);
			  ans += rt;
			  rt = 0;
			  dist -= drun;
			  double timewalk = dist / (way[i].spd + walkS);
			  ans += timewalk;
		  }
	  }

  }
  
  void readInput(int _t)
  {
    t = _t;
	fi >> xlen >> walkS >> runS >> runT >> N;
	way.clear();
	way.resize(N);
	for (int i=0;i<N;i++)
	{
		fi >> way[i].B >> way[i].E >> way[i].spd;
	}
	ans = 0;
  }
  
  void writeOutput()
  {
    fo << "Case #" << (t+1) << ": ";
	//char buf[100

	fo << setprecision(10) << ans;
    fo << endl;
  }
};


int main(int argc, char *argv[])
{
  //fi.open("test.in");  fo.open("test.out");
  //fi.open("A0.in");  fo.open("A0.out");
  fi.open("A1.in");  fo.open("A1.out");
   
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

