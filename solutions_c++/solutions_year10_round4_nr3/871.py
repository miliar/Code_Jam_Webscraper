/* tjhei
   
   g++ main.cc -O3 -Wall && ./a.out
 */

#include <stdio.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

int main()
{
  std::ifstream in("in");
  int cases;
  in >> cases;

  for (int c=0;c<cases;++c)
    {
      std::cout << "Case #" << c+1 << ": ";
      int R;
      in >> R;
      std::vector<std::vector<bool> > field;

      int maxx=1, maxy=1;
      field.resize(maxy);
      for (int y=0;y<maxy;++y)
	field[y].resize(maxx);
	  
      for (int i=0;i<R;++i)
	{
	  int x1,x2,y1,y2;
	  in >> x1 >> y1 >> x2 >> y2;

	  maxx=std::max(x2+1,maxx);
	  maxy=std::max(y2+1,maxy);


					   //  std::cout << maxx << ' ' << maxy << std::endl;
  
	  field.resize(maxy);
	  for (int y=0;y<maxy;++y)
	    field[y].resize(maxx);

	  for (int y=y1;y<=y2;++y)
	    for (int x=x1;x<=x2;++x)
	      field[y][x]=true;
	}

      int steps=0;
      int bacts=0;
      for (int y=0;y<maxy;++y)
	{
	  for (int x=0;x<maxx;++x)
	    if (field[y][x])
	      ++bacts;
	}
      
      while (bacts>0)
	{
	  steps++;
	  
	  for (int y=maxy-1;y>0;--y)
	    for (int x=maxx-1;x>0;--x)
	      {
		if (field[y][x] && !(field[y-1][x] || field[y][x-1]))
		  {
		    field[y][x]=false;
		    --bacts;
		  }
		else
		  if (!field[y][x] && field[y-1][x] && field[y][x-1])
		  {
		    field[y][x]=true;
		    ++bacts;
		  }		    
	      }
	  for (int x=0;x<maxx;++x)
	    if (field[0][x])
	      {
		field[0][x]=false;
		--bacts;
	      }	
	  for (int y=0;y<maxy;++y)
	    if (field[y][0])
	      {
		field[y][0]=false;
		--bacts;
	      }	  
	}
      

				       /*
      for (int y=0;y<maxy;++y)
	    {   for (int x=0;x<maxx;++x)
		{
		    std::cout << ((field[y][x])?'1':'0');
		}
		std::cout << std::endl;
		}*/

      
      std::cout << steps << std::endl;

    }
  return 0;
}
