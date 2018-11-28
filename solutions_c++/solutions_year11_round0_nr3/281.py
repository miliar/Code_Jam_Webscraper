// gcjc.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"


#include <stdio.h>
int a[1200];
int main()
{
	freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
  int n,i,j,k,t,sum,yh;
  scanf("%d",&t);
  int cnt=1;
  while (t--) 
  {
    scanf("%d",&n);
	sum=0;
	yh=0;
    for(i=0;i<n;i++)
	{
      scanf("%d",&a[i]);
	  sum+=a[i];
	  yh^=a[i];
	}
	printf("Case #%d: ",cnt);
	cnt++;
	if(yh!=0)
	{
		printf("NO\n");
	}
	else
	{
		int min1=100000000;
		for(i=0;i<n;i++)
			if(a[i]<min1)
				min1=a[i];
		printf("%d\n",sum-min1);
	}
  }
  return 0;
}
