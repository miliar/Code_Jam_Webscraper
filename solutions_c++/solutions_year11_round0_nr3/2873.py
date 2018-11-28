#include <stdio.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>

using namespace std;

int add(int a,int b)
{
  return a^b;
}


int main()
{
  std::ifstream in("in");
  int cases;
  in >> cases;

  for (int i=0;i<cases;++i)
    {
      int N;
      in >> N;

      vector<int> c;

      for (int j=0;j<N;++j)
	{
	  int tt;
	  in >> tt;
	  c.push_back(tt);
	}

      int p=pow(2,N);
      int maxx=-1;
      for (int j=0;j<p;++j)
	{
	  int s1=0;
	  int r1=0;
	  int s2=0;
	  int r2=0;
	  for (int k=0;k<N;++k)
	    {
	      if (j&(1<<k))
		{
		  s1=add(s1,c[k]);
		  r1=r1+c[k];
		}	      
	      else
		{
//		  std::cout << "(" << c[k] << ")";
		  
		  s2=add(s2,c[k]);
		  r2=r2+c[k];
		}	      
	    }

	  if (s1==s2 && r1>0 && r2>0)
	    {
	      maxx=max(maxx,max(r1,r2));
//	      std::cout << j << " " << max(r1,r2) <<":"<< s1 << "," << s2 << std::endl;
	    }
	}
      
      
      std::cout << "Case #" << i+1 << ": ";
      if (maxx==-1) std::cout << "NO";
      else std::cout << maxx;

      
      std::cout << std::endl;

      }
  return 0;
}
