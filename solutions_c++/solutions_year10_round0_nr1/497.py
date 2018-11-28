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

  for (int i=0;i<cases;++i)
    {
      int N,K;
      in >> N >> K;

      /*      std::vector<bool> on;
      on.resize(N);
      for (int k=0;k<K;++k)
	{
	  for (int j=0;j<N;++j)
	    {
	    on[j]=!on[j];
	    if (on[j])
	      break;
	    }
	  //	  for (int j=0;j<=N;++j)
	  //	    std::cout << on[j];
	  //	  std::cout << std::endl;
	}
      
      bool ison=true;
      for (int j=0;j<N;++j)
	if (!on[j])
	  {ison=false;break;}
      */

      std::cout << "Case #" << i+1 << ": ";
      int off=pow(2,N)-1;

      if (K>0 && K%(off+1)==off)
	std::cout << "ON";
      else
	std::cout << "OFF";

      std::cout << std::endl;

    }
  return 0;
}
