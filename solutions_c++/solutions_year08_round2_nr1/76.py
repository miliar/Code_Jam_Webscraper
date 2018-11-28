#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <ctype.h>
#include <map>
#include <set>
#include <algorithm>
#include <utility>
#include <queue>
#include <stack>

#define for_to(i,j,k) for(i=j; i<=k; ++i)
#define for_downto(i,j,k) for(i=j; i>=k; --i)
#define wipe(a,x) memset(a,x,sizeof(a))
#define gcd __gcd
#define huge long long
#define pii pair<int,int>

using namespace std;

huge c[3][3];
huge i,j,k;
huge n_tests,test;
huge n,A,B,C,D,x0,y0,X,Y,M;
huge x1,x2,x3,y1,y2,y3;
huge ans,temp;
pair<int,int> p1,p2,p3;

int main()
{
  scanf("%lld",&n_tests);
 // cout << n_tests << endl;
  for_to(test,1,n_tests)
  {
    scanf("%lld %lld %lld %lld %lld %lld %lld %lld",&n,&A,&B,&C,&D,&x0,&y0,&M); 
    wipe(c,0);
	X=x0;
	Y=y0;
	++c[X % 3][Y % 3];
	for_to(i,1,n-1)
	{
	  X = (A * X + B) % M;
      Y = (C * Y + D) % M;
	  ++c[X % 3][Y % 3];
	}
	
    ans=0;
	for_to(x1,0,2)
	{
	  for_to(y1,0,2)
	  {
	    //cout << x1 << "-" << y1 << " --> " << c[x1][y1] << endl;
	    for_to(x2,0,2)
		{
		  for_to(y2,0,2)
		  {
		    for_to(x3,0,2)
			{
			  for_to(y3,0,2)
			  {
			    
			    p1=pii(x1,y1);
				p2=pii(x2,y2);
				p3=pii(x3,y3);
				if (p1>p2 || p2>p3) continue;
				if ((x1+x2+x3)%3==0 && (y1+y2+y3)%3==0)
				{
				  if (p1!=p2 && p1!=p3 && p2!=p3)
				  {
				    ans+=c[x1][y1]*c[x2][y2]*c[x3][y3];
				  }
				  else if (p1==p2 && p2==p3)
				  {
				    ans+=( c[x1][y1]*(c[x2][y2]-1)*(c[x3][y3]-2) )/6;
				  }
				  else if (p1==p2)
				  {
				    ans+=c[x3][y3]*( ( c[x1][y1]*(c[x2][y2]-1) ) /2 );
				  }
				  else if (p2==p3)
				  {
				    ans+=c[x1][y1]*( ( c[x2][y2]*(c[x3][y3]-1) ) /2 );
				  }
				  
				}
			  }
			}
		  }
		}
	  }
	}	   
	cout << "Case #" << test << ": " << ans << endl;
  }
  
  
  return 0;
}

