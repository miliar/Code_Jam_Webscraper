#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <utility>
#include <algorithm>

using namespace std;

int a[10000][2];
int g[10000], c[10000];
int n, m, v;
int unknown = 10000;

int main()
{
  int i, j, k;
  ifstream in("a.in");
  ofstream out("a.out");
  int t; in >> t; 
  for (int lp = 1; lp<=t; lp++)
    {
      in >> m >> v;  
      n = (m-1)/2;
      for (i=0; i<n; i++)
	in >> g[i] >> c[i];	
      for (i=n; i<m; i++)
	{
	  in >> k;
	  a[i][k] = 0;
	  a[i][1-k] = unknown;
	} 
      for (i=n-1; i>=0; i--)
	{
	  int l = i*2+1;
	  int r = i*2+2;
	  int m1, m2, m3, m4;
	  int t_and[2], t_or[2];
	  a[i][0] = unknown; a[i][1] = unknown;
	  m1 = a[l][0]+a[r][0];
	  m2 = a[l][0]+a[r][1];
	  m3 = a[l][1]+a[r][0];
	  m4 = a[l][1]+a[r][1];
	  t_and[0] = min(m1, min(m2, m3));
	  t_and[1] = m4;
	  t_or[0] = m1;
	  t_or[1] = min(m2, min(m3, m4));
	  if (g[i] == 1) 
	    {
	      a[i][0] = min(a[i][0], t_and[0]);
	      a[i][1] = min(a[i][1], t_and[1]);
	      if (c[i] == 1)
		{
		  a[i][0] = min(a[i][0], t_or[0]+1);
		  a[i][1] = min(a[i][1], t_or[1]+1);			    
		}
	    }
	  else
	    {
	      a[i][0] = min(a[i][0], t_or[0]);	     
	      a[i][1] = min(a[i][1], t_or[1]);
	      if (c[i] == 1)
		{
		  a[i][0] = min(a[i][0], t_and[0]+1);
		  a[i][1] = min(a[i][1], t_and[1]+1);
		}
	    }	
	}
      out << "Case #" << lp << ": ";
      if (a[0][v] != unknown)	
	out << a[0][v] << endl;
      else
	out << "IMPOSSIBLE" << endl;
    }
  in.close();
  out.close();
  return 0;
}
