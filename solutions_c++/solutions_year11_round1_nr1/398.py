// gcjr1a.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include <stdio.h>
int main()
{
	freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
  int i,j,k,t,tt,cas,pd,pg,tag;
  long long n;
  double win;
  scanf("%d",&t);
  for(cas=1;cas<=t;cas++)
  {
    scanf("%lld%d%d",&n,&pd,&pg);
	tag=0;
	if(n>=200)
	{
        if(pg!=100&&pg!=0)
			tag=1;
		else if(pg==100&&pd==100)
			tag=1;
		else if(pg==0&&pd==0)
			tag=1;
	}
	else
	{
		for(i=1;i<=n;i++)
		{
			if(i*pd%100==0)
			{
				tag=1;
				break;
			}
		}
       if(pg==100&&pd!=100)
		   tag=0;
	   else if(pg==0&&pd!=0)
			tag=0;
	}
	printf("Case #%d: ",cas);
	if(tag)
      printf("Possible\n");
	else
		printf("Broken\n");
  }
  return 0;
}
