// gcjr2a.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <stdio.h>
#include <algorithm>
using namespace std;
struct cs
{
	double bg;
	double ed;
	double w;
}csd[2005];
int cmp(cs a,cs b)
{
	return a.w<b.w;
}
int main()
{
	freopen("in.txt","r",stdin);
    freopen("out5.txt","w",stdout);
	int i,j,k,tt,cas,n;
	double x,s,r,t,mcsd;
    scanf("%d",&tt);
	double res,t1,x1,sy;
	cas=1;
	while(tt--)
	{
	printf("Case #%d: ",cas);
	cas++;
      scanf("%lf%lf%lf%lf%d",&x,&s,&r,&t,&n);
	  mcsd=x;
      for(i=0;i<n;i++)
	  {
		  scanf("%lf%lf%lf",&csd[i].bg,&csd[i].ed,&csd[i].w);
		  mcsd-=(csd[i].ed-csd[i].bg);
	  }
	  sort(csd,csd+n,cmp);
      res=0.0;
	  t1=t;
	  sy=x;
	  if((mcsd/r)>t)
	  {
		  res+=t;
		  res+=((mcsd-r*t)/s);
		  for(i=0;i<n;i++)
			  res+=((csd[i].ed-csd[i].bg)/(csd[i].w+s));
		  printf("%.9lf\n",res);
		  continue;
	  }
	   res+=(mcsd/r);
		 t1-=(mcsd/r);
	  for(i=0;i<n&&t1>0;i++)
	  {
		  if(((csd[i].ed-csd[i].bg)/(csd[i].w+r))<t1)
		  {
           res+=((csd[i].ed-csd[i].bg)/(csd[i].w+r));
		   t1-=((csd[i].ed-csd[i].bg)/(csd[i].w+r));
		  }
		  else
		  {
			  res+=t1;
			  res+=((csd[i].ed-csd[i].bg)-(csd[i].w+r)*t1)/(csd[i].w+s);
			  t1=0;
		  }
	  }
     for(;i<n;i++)
	 {
          res+=((csd[i].ed-csd[i].bg)/(csd[i].w+s));
	 }
	 printf("%.9lf\n",res);
	}
	return 0;
}

