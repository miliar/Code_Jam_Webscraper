// gcjd.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <algorithm>
using namespace std;
int a[10005];
int main()
{
	freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
  int n,i,j,k,t,cnt;
  scanf("%d",&t);
  cnt=1;
  double cnt1;
  while(t--)
  {
	  cnt1=0.0;
   scanf("%d",&n);
   for(i=1;i<=n;i++)
	   scanf("%d",&a[i]);
   for(i=1;i<=n;i++)
	   if(a[i]!=i)
		   cnt1+=1.0;
   printf("Case #%d: %lf\n",cnt,cnt1);
   cnt++;
  }
  return 0;
}
