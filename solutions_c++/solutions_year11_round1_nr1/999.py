#include <iostream>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <algorithm>
#include <cmath>

using namespace std;

int main(int argc, char** argv)
{
  int T, Pd, Pg;
  long D, G, N, wD, wG;
  bool possD, possG;

  ifstream input("A-large.in");
  ofstream output("A-large.out");

  input >> T;
  for(int i = 0; i < T; i++)
    {
      input >> N;
      input >> Pd;
      input >> Pg;
      
      D = 1;
      possD = false;
      possG = false;

      while(!possD && D <= N)
	{
	  wD = 0;
	  while(!possD && wD <= D)
	    {
	      if(Pd * D == 100 * wD)
		{
		  possD = true;
		  break;
		}
	      wD++;
	    }
	  D++;
	}

      if(possD)
	{
	  D--;
	  G = D;
	  if((Pd > 0 && Pg == 0) || (Pd < 100 && Pg == 100))
	    possG = false;
	  else
	    {
	      while(!possG)
		{
		  wG = wD;
		  while(!possG && wG <= G)
		    {
		      if(Pg * G == 100 * wG)
			{
			  possG = true;
			  break;
			}
		      wG++;
		    }
		  G++;
		}
	    }
	}

      if(possG && possD)
	output<<"Case #"<<i+1<<": "<<"Possible"<<endl;	  
      else
	output<<"Case #"<<i+1<<": "<<"Broken"<<endl;
    }
 
  return 0;
}


