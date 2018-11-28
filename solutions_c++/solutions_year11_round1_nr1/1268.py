// gcj.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<cstdio>
int solve(int n,int d,int g) {
	if(g==100 && d!=100) return 0;
	if(g==0 && d!=0) return 0;
	int gcd=1;
	for(int i=1;i<=100;++i) if((100 % i) ==0 && (d % i)==0) gcd=i;
	if(100/gcd <=n) return 1;
	return 0;
}
int _tmain(int argc, _TCHAR* argv[])
{
     int t=0;
	 scanf("%d",&t);
	 for(int xx=1;xx<=t;++xx) {
		 int n,d,g;
		 scanf("%d %d %d",&n,&d,&g);
		 printf("Case #%d: %s\n",xx,solve(n,d,g)?"Possible":"Broken");

	 }
	return 0;
}

