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

      char lastcol=0;
      int moves=0;
      int lastmoves=0;
      int pos[2]={1,1};

      for (int j=0;j<N;++j)
	{
	  char col;
	  int cpos;
	  in >> col >> cpos;
	  int colindex=(col=='O')?0:1;
	  int tomove = abs(pos[colindex]-cpos);
	  
	  if (col==lastcol)
	    {
	      lastmoves+= tomove + 1;
	    }
	  else
	    {
	      if (lastcol!=0)
		{
		  moves+=lastmoves;
		  lastmoves=max(tomove-lastmoves,0)+1;
		}
	      else
		lastmoves=tomove+1;
	      lastcol=col;
	    }
	  pos[colindex]=cpos;
	}

      moves+=lastmoves;
      std::cout << "Case #" << i+1 << ": ";
      std::cout << moves;

      
      std::cout << std::endl;

      }
  return 0;
}
