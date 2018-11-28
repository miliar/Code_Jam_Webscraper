#include "stdafx.h"

int main()
{ int tt, a, b, i, j;
  float p, m, min, c;

  freopen( "input.txt", "r", stdin );
  freopen( "output.txt", "w", stdout );    
  scanf("%d", &tt);
  for(int t=1; t<=tt; ++t)
  { scanf("%d%d", &a, &b);      
	p = 1.0;
    min = b+2;
	for(i=1; i<=a; ++i) 
    {scanf("%f", &m);
	 p = p*m;
	 c = p*(b-a+1+2*(a-i))+(1-p)*(2*b-a+2+2*(a-i));	 	 
	 if (c < min)
	 { min = c;
	 }
	}	
	printf("Case #%d: %f\n", t, min);
  } 
  return 0;
}
