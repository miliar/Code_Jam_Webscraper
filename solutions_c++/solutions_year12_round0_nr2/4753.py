#include <iostream>
#include <stdio.h>

int main()
{
  int nTestCases;
  scanf("%d",&nTestCases);
  for(int i=0;i<nTestCases;++i)
    {
      int nGooglers=0;
      int nSurp=0;
      int nBest=0;
      scanf("%d %d %d",&nGooglers,&nSurp,&nBest);
      int nRisky=0;
      int nCur;
      int more = 0;
      for(int j=0;j<nGooglers;++j)
	{
	  scanf("%d",&nCur);
	  if(nCur > ((nBest-1)*3))
	    {
	      ++more;
	    }
	  else
	    {
	      if(nCur!=0 && nCur > (nBest*3-5))
		{
		  ++nRisky;
		}
	    }
	}
      if(nRisky == nSurp)
	{
	  nRisky=nSurp;
	}
      if(nRisky < nSurp)
	{
	  nRisky=nRisky;
	}
      else
	{
	  nRisky=nSurp;
	}
      printf("Case #%d: %d\n",i+1,more+nRisky);
    }
  return 0;
}

