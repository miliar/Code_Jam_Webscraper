#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
#define p(x) cout<<#x<<":"<<x<<"\n"

int cs,c,n,m,a,x;
bool f;

int main()
{
  int x1,y1,x2,y2;

  scanf("%d",&cs);
  for(c=0;c<cs;c++)
  {
    scanf("%d %d %d",&n,&m,&a);
	f=0;
	printf("Case #%d: ",c+1);
	for(x1=-n;x1<=n && !f;x1++)
	  for(y1=0;y1<=m && !f;y1++)
	    for(x2=x1;x2<=min(n,x1+n) && !f;x2++)
		  for(y2=0;y2<=m && !f;y2++)
		  {
		    if(!f && abs(x1*y2-x2*y1)==a)
			{
			  f=1;
			  x=min(0,x1);
			  printf("%d %d %d %d %d %d\n",-x,0,x1-x,y1,x2-x,y2);
			}
		  }
    if(!f)
	  printf("IMPOSSIBLE\n");
  }
  return 0;
}
