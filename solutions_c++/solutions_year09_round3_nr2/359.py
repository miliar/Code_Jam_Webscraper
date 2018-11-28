#include <iostream>
#include <stdio.h>
#include <string>
#include <math.h>

using namespace std;

string line ;


int main()
{
  int n ;

  scanf("%d\n", &n) ;
  

  for(int i=1;i<=n;i++)
  {
      int m; 
      scanf("%d\n", &m) ;
      double pos[m][3] ;
      double v[m][3] ;
      for(int j=0;j<m;j++)
      {
	  scanf("%lf %lf %lf", &pos[j][0], &pos[j][1], &pos[j][2]) ;
	  scanf("%lf %lf %lf", &v[j][0], &v[j][1], &v[j][2]) ;

      }
      double cpos[3] ={};
      double cv[3] = {}; 
      for(int j=0;j<m;j++)
      {
	    cpos[0] += pos[j][0] ;
	    cpos[1] += pos[j][1] ;
	    cpos[2] += pos[j][2] ;
	    cv[0] += v[j][0] ;
	    cv[1] += v[j][1] ;
	    cv[2] += v[j][2] ;
      }
      cpos[0] /= m ;
      cpos[1] /= m ;
      cpos[2] /= m ;
      cv[0] /= m ;
      cv[1] /= m ;
      cv[2] /= m ;

      double l=0, mian=0 ;
      for(int j=0;j<3;j++)
      {
	    l+= (-1)*cpos[j]*cv[j] ;
	    mian+= cv[j]*cv[j];
      }
      double tmin = 0;
      if(mian !=0)
	tmin = l/mian ;

      if(tmin < 0) tmin = 0 ;
      double d[3] = {};
      for(int j=0;j<3;j++)
	  d[j] = cpos[j] + tmin*cv[j];

      double dmin = 0 ;
      for(int j=0;j<3;j++)
	  dmin += d[j]*d[j] ;

      dmin = sqrt(dmin) ;
      cout.precision(9) ;
      cout << "Case #" << i << ": " << dmin << " " << tmin << endl ;


      
  }

  return 0;
}
