#include <stdio.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

#include "BigIntegerLibrary.hh"
#include "BigIntegerUtils.hh"

void ggt(BigInteger &res, BigInteger &a, BigInteger &b)
{
  BigInteger a_=a;
  BigInteger b_=b;
  BigInteger h;

  while(b_!=0)
    {
      h=a_%b_;
      a_=b_;
      b_=h;
    }
  res=a_;
}

int main()
{
  BigInteger d;

  std::ifstream in("in");
  int cases;
  in >> cases;

  for (int i=0;i<cases;++i)
    {
      int N;
      in >> N;
      std::vector<BigInteger> t(N);
      std::vector<BigInteger> diffs(N-1);
      std::string s;
      for (int j=0;j<N;++j)
	{
	  in >> s;
	  t[j]=stringToBigInteger(s);
	  if (j>0)
	    {
	    diffs[j-1]=t[j-1]-t[j];
	    if (diffs[j-1].getSign()==BigInteger::negative)
		diffs[j-1].flipSign();
	    }
	}

      BigInteger T(diffs[0]);
      for (int j=1;j<N-1;++j)
	ggt(T,T,diffs[j]);

      //      std::cout << "ggt:" << T << std::endl;
      for (int j=0;j<N;++j)
	{
	  BigInteger val=t[j]%T;
	  val=T-val;
	  //	  std::cout << val << std::endl;

	}

      BigInteger val=t[0]%T;
      if (val>0) val=T-val;
      
      

      std::cout << "Case #" << i+1 << ": " << val << std::endl;

    }
  return 0;
}
