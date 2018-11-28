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

int n, m, area;
int x1, y1, x2, y2, x3, y3;

bool solve()
{
  if (area>n*m) return false;
  for (x1=0; x1<=n; x1++)
    for (x2=x1; x2<=n; x2++)
      for (y1=0; y1<=m; y1++)
	for (y2=y1; y2<=m; y2++)
	  {
	    int a = (y1-y2);
	    int b = (-x1+x2);
	    int c = (-x1*y2+x2*y1);
	    // a*x3 + b*y3 = c +-area
	    if (a == 0)
	      {
		if (b == 0) continue;
		x3 = 0;
		y3 = (c+area)/b;
		if ((c+area)%b == 0 && 0<=y3 && y3<=m) return true;
		y3 = (c-area)/b;
		if ((c-area)%b == 0 && 0<=y3 && y3<=m) return true;	       
	      }
	    else
	      {
		for (y3=y2; y3<=m; y3++)
		  {
		    int t = (c+area)-b*y3;
		    x3 = t/a;
		    if (t%a == 0 && 0<=x3 && x3<=n) return true;
		    t = (c-area)-b*y3;
		    x3 = t/a;
		    if (t%a == 0 && 0<=x3 && x3<=n) return true;
		  }
	      }
	  }  
  return false;
}

int main()
{
  ifstream in("b.in");
  ofstream out("b.out");
  int c; in >> c;
  for (int lp=1; lp<=c; lp++)
    {
      in >> n >> m >> area;
      out << "Case #" << lp << ": ";
      if (solve()) 
	out << x1 << ' ' << y1 << ' ' << x2 << ' ' << y2 << ' '
	    << x3 << ' ' << y3 << endl;
      else
	out << "IMPOSSIBLE" << endl;
    }
  in.close();
  out.close();
  return 0;
}
