#include <iostream>
#include <cmath>
#include <fstream>
using namespace std;

void main()
{   ofstream outfile( "A-small-attempt2.out" );
    ifstream infile( "A-small-attempt2.in" );

	unsigned long T, N, pd, pg, i, j,mind,ming,nd,ng,wd,wg,id,ig,ld,lg;
   infile>>T;
   for (i=1;i<=T;i++)
   {
      infile>>N>>pd>>pg;
	  if ((pd*pg==0)&&(pd+pg!=0))
	  {outfile<<"Case #"<<i<<": Broken"<<endl;}
	  else{
		  if ((pd==0 && pg==0)||(pd==100 &&pg==100))
		  {outfile<<"Case #"<<i<<": Possible"<<endl;}
		 else
	  {
      j=1;
      while (pd%j ==0) j=j*2;
      if (j>4){mind = 1;}else mind =8/j;
      j=1;
      while (pd%j==0) j=j*5;
	  if (j<=25) mind=mind*125/j;
      j=1;
      while (pg%j ==0) j=j*2;
      if (j>4){ming = 1;}else ming =8/j;
      j=1;
      while (pg%j==0) j=j*5;
	  if (j<=25) ming=ming*125/j;

      if (N<mind)
      { outfile<<"Case #"<<i<<": Broken"<<endl;
      }else
      {
          nd=ceil(N/mind);
          wd=mind*pd/100;
          wg=ming*pg/100;
          ld=mind-wd; lg=ming-wg;
          if ((lg>0)&&(wg>0))
          {
             outfile<<"Case #"<<i<<": Possible"<<endl;
          }
          else
          {outfile<<"Case #"<<i<<": Broken"<<endl;
          }
      }
	  };};
   }

}