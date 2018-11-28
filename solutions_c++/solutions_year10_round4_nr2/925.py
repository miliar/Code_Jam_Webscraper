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
      int P;
      in >> P;

      int num_teams=1<<P;
      int num_tic=(1<<P)-1;

				       //     std::cout << "numtic=" << num_tic << std::endl;
      

      std::vector<int> M(num_teams);
      for (int i=0;i<num_teams;++i)
	in >> M[i];

      
      std::vector<int> tp(num_tic);
      int k=0;
      
      for (int i=0;i<P;++i)
	{
	  int anz=std::pow(2,P-1-i);
	  
	  for (int x=0;x<anz;++x)
	    {
	      in >> tp[k];
	      ++k;
	    }
	}

      unsigned int price=std::pow(2,30);

      std::vector<bool> ticket(num_tic);

      for (unsigned int t=0;t<num_teams;++t)
	{
	  int ii=P;
	  while (true)
	    {
	      unsigned int miss=0;
	      unsigned int index=t;
	      unsigned int start=0;
	      unsigned lastind=0;
	      for (int i=0;i<P;++i)
		{
		  index=index/2;
		  unsigned int ind=start+index;
		  start+=1<<(P-1-i);
						   //std::cout << "lookat" << ind << std::endl;
		  
		  if (!(ticket[ind]))
		    {++miss;
		     lastind=ind;
		    }
		  
		}

	      if (miss>M[t])
		{
		  ticket[lastind]=1;
		}
	      else
		break;
	    }
	  
	  

	}
      
      
	  
				       /*
					 std::cout << "ticket:";
	  for (int i=0;i<num_tic;++i)
	    std::cout << ((ticket[i])?"1":"0");
	  std::cout << std::endl;
				       */  
	  
	  bool valid=true;
	  for (unsigned int t=0;t<num_teams;++t)
	    {
	      unsigned int miss=0;
	      unsigned int index=t;
	      unsigned int start=0;
	      for (int i=0;i<P;++i)
		{
		  index=index/2;
		  unsigned int ind=start+index;
		  start+=1<<(P-1-i);
						   //std::cout << "lookat" << ind << std::endl;
	 
		  if (!(ticket[ind]))
		      ++miss;
		}

//	      std::cout << "miss t=" << t << " " << miss << std::endl;
	      
	      if (miss>M[t])
		{
		  valid=false;
		  break;
		}
	    }


					   // std::cout << "valid=" <<valid << std::endl;
	  

	  
	  
	  unsigned int myprice=0;
	  for (int t=0;t<num_tic;++t)
	    {
	      if (ticket[t])
		{
		  myprice+=tp[t];

//		  std::cout << "tp["<< t << " " << tp[t] << std::endl;
				
		}
	      
	    }
//	  std::cout << "valid:" <<" " << myprice<<  std::endl;
	  price=std::min(price,myprice);

					   //}
      
      
      
      


      
      std::cout  << price << std::endl;

    }
  return 0;
}
