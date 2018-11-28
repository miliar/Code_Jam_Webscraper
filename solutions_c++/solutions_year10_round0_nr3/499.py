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
      long R,k,N;
      in >> R >> k >> N;
      std::vector<long> pass(N);
      for (long ii=0;ii<N;++ii)
	in >> pass[ii];

      std::vector<long> new_dest(N);
      std::vector<long> new_money(N);
      for (long r=0;r<N;++r)
	{
	  long in=0;
	  long it=r;
	  while (pass[it]<=(k-in))
	    {
	      in+=pass[it];
	      //inc:
	      ++it;
	      if (it==N)
		it=0;
	      if (it==r)
		break;
	    }
	  new_dest[r]=it;
	  new_money[r]=in;
	}

      long money=0;
      long it=0;
      for (long r=0;r<R;++r)
	{
	  money+=new_money[it];
	  it=new_dest[it];
	}

      /*//naive:
      std::vector<long>::iterator it=pass.begin();
      std::vector<long>::iterator it_start=pass.begin();
      
      long money=0;
      for (long r=0;r<R;++r)
	{
	  long in=0;
	  it_start=it;
	  while (*it<=(k-in))
	    {
	      in+=*it;
	      //inc:
	      ++it;
	      if (it==pass.end())
		it=pass.begin();
	      if (it==it_start)
		break;
	    }

	  money+=in;
	  }*/


      std::cout << "Case #" << i+1 << ": " << money << std::endl;
    }
  return 0;
}
