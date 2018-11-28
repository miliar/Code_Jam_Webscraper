// gcja.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int dp[105];
struct cz
{
	int jqr;
	int bs;
}czs[105];
int main()
{
	freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
  int n,i,j,k,t,wzo,wzb;
  scanf("%d",&t);
  char tc;
  int cnt=1;
  while (t--) 
  {
     scanf("%d",&n);
	 memset(dp,0,sizeof(dp));
     for(i=1;i<=n;i++)
	 {
        scanf(" %c %d",&tc,&czs[i].bs);
		if(tc=='O')
         czs[i].jqr=0;
		else
			czs[i].jqr=1;
	 }
	 int next;
	 int nexti;
	 int res=0;
	 wzo=1;
	 wzb=1;
	 if(czs[1].jqr==0)
	 {
		 next=-1;
		 nexti=-1;
		 for(j=2;j<=n;j++)
		 {
            if(czs[j].jqr==1)
			{
				next=czs[j].bs;
				nexti=j;
				break;
			}
		 }
		 int ts=abs(wzo-czs[1].bs)+1;
		 res+=abs(wzo-czs[1].bs)+1;
		 wzo=czs[1].bs;
		 if(next!=-1)
		 {
			 if(ts>abs(next-wzb))
			 {
				 wzb=next;
			 }
			 else
			 {
				 if(next>=wzb)
					 wzb+=ts;
				 else
					 wzb-=ts;
			 }
		 }
	 }
	 else if(czs[1].jqr==1)
	 {
		 next=-1;
		 nexti=-1;
		 for(j=2;j<=n;j++)
		 {
            if(czs[j].jqr==0)
			{
				next=czs[j].bs;
				nexti=j;
				break;
			}
		 }
		 int ts=abs(wzb-czs[1].bs)+1;
		 res+=abs(wzb-czs[1].bs)+1;
		 wzb=czs[1].bs;
		 if(next!=-1)
		 {
			 if(ts>abs(next-wzo))
			 {
				 wzo=next;
			 }
			 else
			 {
				 if(next>=wzo)
					 wzo+=ts;
				 else
					 wzo-=ts;
			 }
		 }
	 }
  for(i=2;i<=n;i++)
  {
   if(czs[i].jqr==0)
	 {
		 next=-1;
		 nexti=-1;
		 for(j=i+1;j<=n;j++)
		 {
            if(czs[j].jqr==1)
			{
				next=czs[j].bs;
				nexti=j;
				break;
			}
		 }
		 int ts=abs(wzo-czs[i].bs)+1;
		 res+=abs(wzo-czs[i].bs)+1;
		 wzo=czs[i].bs;
		 if(next!=-1)
		 {
			 if(ts>abs(next-wzb))
			 {
				 wzb=next;
			 }
			 else
			 {
				 if(next>=wzb)
					 wzb+=ts;
				 else
					 wzb-=ts;
			 }
		 }
	 }
	  else if(czs[i].jqr==1)
	 {
		 next=-1;
		 nexti=-1;
		 for(j=i+1;j<=n;j++)
		 {
            if(czs[j].jqr==0)
			{
				next=czs[j].bs;
				nexti=j;
				break;
			}
		 }
		 int ts=abs(wzb-czs[i].bs)+1;
		 res+=abs(wzb-czs[i].bs)+1;
		 wzb=czs[i].bs;
		 if(next!=-1)
		 {
			 if(ts>abs(next-wzo))
			 {
				 wzo=next;
			 }
			 else
			 {
				 if(next>=wzo)
					 wzo+=ts;
				 else
					 wzo-=ts;
			 }
		 }
	 }
  }
  printf("Case #%d: %d\n",cnt,res);
  cnt++;
  }
  return 0;
}

