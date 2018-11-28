#include <iostream>
#include<cstdio>
#include <algorithm>
using namespace std;

int arr[100],n,ntests;
int main()
{
	  int i, t, nTurns, temp, result=-1;
	  int xa, xb, sa, sb, j;
	  scanf("%d",&ntests);;
	  for(t=1;t<=ntests;t++)
	  {
		    result = -1;
		    scanf("%d",&n);
		    for(i=0;i<n;i++)
		    {
			scanf("%d",&arr[i]);
		    }
		    nTurns = 1<<n;
		    
		    for(i=1;i<nTurns-1;i++)
		    {
			      xa=xb=sa=sb=0;
			      temp=i;
			      for(j=0;j<n;j++)
			      {
					if(temp&1)
					{
				  		xa=xa^arr[j];
				  		sa=sa+arr[j];
					}
					else
					{
				  		xb=xb^arr[j];
				  		sb=sb+arr[j];
					}
					temp = temp/2;
			    }
			    if((xa==xb) && (max(sa,sb)>result))
					result = max(sa,sb);
		    }
		    if(result>-1)
		      printf("Case #%d: %d\n",t,result);
		    else
		      printf("Case #%d: NO\n",t);
	  }
}
