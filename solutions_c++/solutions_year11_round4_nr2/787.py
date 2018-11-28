// gcjr2b.cpp : 定义控制台应用程序的入口点。
//
// gcjr2a.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <stdio.h>
#include <algorithm>
using namespace std;
double zz[20][20];
int main()
{
	freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
	int i,j,k,tt,cas,n,r,c,res,dx,dy,i1,j1,tmp;
	double d,t1,t2,t3,t4,t5,sum,zlx,zly;
    scanf("%d",&tt);
	//double res,t1,x1,sy;
	cas=1;
	while(tt--)
	{
	printf("Case #%d: ",cas);
	cas++;
      scanf("%d%d%lf",&r,&c,&d);
      for(i=0;i<r;i++)
		  for(j=0;j<c;j++)
		  {
			  scanf("%1d",&tmp);
			  zz[i][j]=tmp;
		  }
      res=0;
	  for(i=0;i<r;i++)
		  for(j=0;j<c;j++)
		  {
			  for(k=3;;k++)
			  {
				  if((i+k>r)||(j+k>c))
					  break;
				  dx=i+k-1;
				  dy=j+k-1;
				  sum=0.0;
				  zlx=0.0;
				  zly=0.0;
                for(i1=i;i1<=dx;i1++)
					for(j1=j;j1<=dy;j1++)
					{
						if((i1==i&&j1==j)||(i1==i&&j1==dy)||(i1==dx&&j1==j)||(i1==dx&&j1==dy))
							continue;
						zlx+=(double)(i1)*(d+zz[i1][j1]);
						zly+=(double)(j1)*(d+zz[i1][j1]);
						sum+=(d+zz[i1][j1]);
					}
					zlx/=sum;
					zly/=sum;
					if(zlx==(((double)(i)+(double)(dx))/2.0)&&zly==(((double)(j)+(double)(dy))/2.0))
						if(k>res)
							res=k;
			  }
		  }
  if(res<3)
	  printf("IMPOSSIBLE\n");
  else
	printf("%d\n",res);
	}
	return 0;
}
