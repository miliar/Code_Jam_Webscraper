// gcjb.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include <stdio.h>
#include <string.h>
#include <stack>
#include <map>
using namespace std;
char zh[200][200];
char pc[200][200];
int dz[200];
int main()
{
  int n,i,j,k,t,c,d;
  char t1,t2,t3;
  freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
  scanf("%d",&t);
  int top;
  int cnt=1;
  while (t--) 
  {
    top=0;
    memset(zh,0,sizeof(zh));
	memset(pc,0,sizeof(pc));
	scanf("%d ",&c);
	while(c--)
	{
		scanf(" %c %c %c",&t1,&t2,&t3);
		zh[t1][t2]=zh[t2][t1]=t3;
	}
    scanf("%d ",&d);
	while(d--)
	{
		scanf(" %c %c",&t1,&t2);
		pc[t1][t2]=pc[t2][t1]=1;
	}
    scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		scanf(" %c",&t1);
		if(top==0)
			dz[top++]=t1;
		else
		{
			if(zh[dz[top-1]][t1])
				dz[top-1]=zh[dz[top-1]][t1];
			else
			{
				int tag=0;
				for(j=0;j<top;j++)
					if(pc[dz[j]][t1])
					{
						tag=1;
						top=0;
						break;
					}
				if(tag)
					continue;
				else
					dz[top++]=t1;
			}
		}
	}
   printf("Case #%d: [",cnt);
   for(i=0;i<top-1;i++)
	   printf("%c, ",dz[i]);
   if(top-1>=0)
	   printf("%c",dz[top-1]);
   printf("]\n");
   cnt++;
  }
  return 0;
}
