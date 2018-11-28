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
      int N;      
      in >> N;

      char a[100][100];
      double wp[100];
      double owp[100];
      double oowp[100];

      for (int y=0;y<N;++y)
	{
	  int played=0;
	  int win=0;
	  for (int x=0;x<N;++x)
	    {
	      char c;
	      in >> c;
	      a[y][x]=c;
	      if (c=='0' || c=='1')
		++played;
	      if (c=='1')
		++win;
	    }

	  wp[y]=(double)win/played;
	}

      for (int y=0;y<N;++y)
	{
	  double WP=0;
	  int enem=0;
	  for (int yy=0;yy<N;++yy)
	    {
	      if (yy==y)
		continue;
	      if (a[yy][y]=='.')
		continue;
	      ++enem;
	      
	      int played=0;
	      int win=0;
	       for (int x=0;x<N;++x)
		 {
		   if (x==y)
		     continue;
		   
		   if (a[yy][x]=='1')
		     ++win;
		   if (a[yy][x]=='1' || a[yy][x]=='0')
		     ++played;
		 }
	       WP+=(double)win/played;
//	       if (y==3)
//		 cout << win << " " << played << endl;
	       
	      
	    }
	  owp[y]=WP/enem;
//	  cout << "owp" << owp[y] << endl;
	  
	}

      for (int y=0;y<N;++y)
	{
	  double t=0;
	  int enem=0;
	  for (int yy=0;yy<N;++yy)
	    {
	      if (yy==y)
		continue;
	      if (a[yy][y]=='.')
		continue;

	      ++enem;

/*	      if (y==0)
 		cout << owp[yy] << endl;
*/	      
	      t+=owp[yy];
	    }
	  oowp[y]=t/enem;
	}
      
      
      
      

      std::cout << "Case #" << case_+1 << ":" << endl;

      cout.precision(8);
      
         for (int y=0;y<N;++y)
	{
	  cout //<< wp[y] << " " << owp[y] << " " << oowp[y] << " "
	       << 0.25*wp[y]+0.5*owp[y]+0.25*oowp[y]  << endl;
	}
	 
   
					  //   std::cout << std::endl;

    }
  return 0;
}
