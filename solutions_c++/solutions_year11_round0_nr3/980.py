#include<stdio.h>

int main()
{
  int nTestCase;
  scanf("%d",&nTestCase);
  for(int i=0;i<nTestCase;i++)
    {
      int nCandies;
      scanf("%d",&nCandies);
      unsigned long xorn=0;
      unsigned long long sum=0;
      unsigned long small=10000000;
      for(int j=0;j<nCandies;j++)
	{
	  unsigned long n;
	  scanf("%lu",&n);
	  if(small > n)
	    {
	      small = n;
	    }
	  xorn=xorn^n;
	  sum=sum+n;
	}
      printf("Case #%d: ",i+1);
      if(xorn != 0)
	{
	  printf("NO\n");
	}
      else
	{
	  printf("%llu\n",sum - small);
	}
    }
}
