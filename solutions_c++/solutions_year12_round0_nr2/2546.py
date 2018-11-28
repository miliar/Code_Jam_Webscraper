#include "stdafx.h"

int main()
{ int tt, n, s, p, ti, c;
  freopen( "input.txt", "r", stdin );
  freopen( "output.txt", "w", stdout );  
  scanf("%d\n", &tt);  
  for(int t=1; t<=tt; ++t)
  { scanf("%d%d%d", &n, &s, &p);  
    c = 0;
    for(int i=1; i<=n; ++i) 
    { scanf("%d", &ti);
 	  if(ti % 3 == 0)
	  { if(ti/3 >= p) 
	     c++;
	    else
         if((ti/3 == p-1) && (s > 0) && (ti != 0) && (ti != 30))
		 { c++;
	       s--;
		 }
	  }
	  else 
	   if(ti % 3 == 1)
	    { if(ti/3 >= p-1) 
	       c++;	      
	    }
	   else
	    { if(ti/3 >= p-1) 
	       c++;
	      else
           if((ti/3 == p-2) && (s > 0) && (ti != 29))
		  { c++;
	        s--;
		  }
	    }
    }
    printf("Case #%d: %d\n", t, c);
  }  
  return 0;
}