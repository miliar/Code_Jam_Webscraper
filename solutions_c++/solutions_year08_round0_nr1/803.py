#include <stdio.h>
#include <set>
#include <string>
#include <iostream>
#define MAXL 120
using namespace std;

int
main ()
{
  int N,tn;
  scanf ("%d ", &N);
  for (tn=0;tn<N;tn++)
    {
      set <string> dyn, dyn2;
      string ts;
      int S, Q;
      int i;
      int low=0;
      scanf ("%d ", &S);
      for (i=0;i<S;i++)
	{
	  getline (cin, ts);
	  dyn.insert (ts);
	}
      scanf ("%d ", &Q);      
      for (i=0;i<Q;i++)
	{
	  getline (cin, ts);
	  if (dyn.find (ts)!=dyn.end ())
	    {
	      dyn.erase (ts);
	      if (dyn.empty ())
		{
		  low++;
		  dyn.swap (dyn2);
		}
	      dyn2.insert (ts);
	      continue;
	    }
	  if (dyn.empty ())
	    {
	      low++;
	      dyn.swap (dyn2);
	      dyn.erase (ts);
	      dyn2.insert (ts);
	    }
	}
      printf ("Case #%d: %d\n",tn+1,dyn.empty()?low+1:low);
    }
  return 0;
}
