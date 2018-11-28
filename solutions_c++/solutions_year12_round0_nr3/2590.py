#include "stdafx.h"

int main()
{ int tt, a, b, c, d, k, l, q, w, ar[10], p, x, f;
  freopen( "input.txt", "r", stdin );
  freopen( "output.txt", "w", stdout );    
  scanf("%d", &tt);
  for(int t=1; t<=tt; ++t)
  { scanf("%d%d", &a, &b);  
    c=0;
	for(int i=a; i<=b; ++i) 
    { k=1;
	  for(d=i; d>0; d/=10) k*=10; 
	  l=1;
	  q=0;
	  p=0;
	  for(d=i; d>=10; d/=10) 
	   { k/=10;
	     q +=(d % 10)*l;
		 l*=10;
		 w=q*k+d/10;		 
		 if(w>i && w<=b && d%10!=0)
		 {f=0;
		  for(x=0; x<p; ++x)
		   if(ar[x]==w) f=1;
		  if(f==0)
           {ar[p]=w;
		    ++p;
			++c;
		   }
		 }
	   }
	}	
    printf("Case #%d: %d\n", t, c);
  } 
  return 0;
}

