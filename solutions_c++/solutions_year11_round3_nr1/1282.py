#include <stdio.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>
using namespace std;




int main()
{
  std::ifstream in("in");
  int cases;
  in >> cases;

  for (int case_=0;case_<cases;++case_)
    {
      int R,C;
      in >> R >> C;

      char a[50][50];
      
      for (int y=0;y<R;++y)
	{
      for (int x=0;x<C;++x)
	{
	  char c;
	  in >> c;
	  a[y][x]=c;
	}
	}
      

      bool poss=true;

      for (int y=0;y<R;++y)
	{
      for (int x=0;x<C;++x)
	{
	  if (a[y][x]=='#')
	    {
	      if ((y==R-1) || (x==C-1))
		{
		  poss=false;
		  goto on;
		}
	      if (a[y][x+1]!='#'
		  || a[y+1][x]!='#'
		  || a[y+1][x+1]!='#')
		{
		  poss=false;
		  goto on;
		}
	      a[y][x]='/';
	      a[y][x+1]='\\';
	      a[y+1][x]='\\';
	      a[y+1][x+1]='/';
	    }
	}
	}
      
	  
	      

	  on:
	  

      std::cout << "Case #" << case_+1 << ":" << endl;

      if (poss)
	{
	  
      
        for (int y=0;y<R;++y)
	{
      for (int x=0;x<C;++x)
	{
	  cout << a[y][x];
	}
      
      
	  cout << endl;
	}
	}
      else
	{
	  cout << "Impossible" << endl;
	  
	}
      
      
      

//      std::cout << std::endl;

    }
  return 0;
}
