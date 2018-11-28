#include <stdio.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

using namespace std;


int n_factors(int num, int fac)
{
  int r=0;
  if (num==0)
    return 0;
  while (num%fac==0)
    {
      ++r;
      num=num/fac;
    }
  return r;
}


int main()
{
  std::ifstream in("in");
  int cases;
  in >> cases;

  for (int i=0;i<cases;++i)
    {
      bool poss=true;
      int N,PD,PG;
      in >> N >> PD >> PG;

      int f2_ = n_factors(PD,2);
      int f5_ = n_factors(PD,5);

      int D=1;
      if (PD==0)
	D=0;
      else
	D=1;
      if (f2_==0)
	D*=2*2;
      if (f2_==1)
	D*=2;
      if (f5_==0)
	D*=5*5;
      if (f5_==1)
	D*=5;

      if (PG==100 && PD<100)
	poss = false;

      if (PG==0 && PD>0)
	poss = false;

      if (D>N)
	poss= false;
				       //cout << "D: " << D << endl;
      
      
      

      std::cout << "Case #" << i+1 << ": ";

      if (poss)
	std::cout << "Possible";
      else
	std::cout << "Broken";

      std::cout << std::endl;

    }
  return 0;
}
