// gcj.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<cstdio>
#include<string>
#include<vector>
#include<map>
using namespace std;
#define REP(i,n) for(int i=0;i<(int)(n);++i)
typedef __int64 ld; 
 int n;
 ld D;
 ld P[200];
 ld V[200];
 bool check(ld t) {
	 ld pos=-D*ld(4000000);
	 
	 REP(i,n) {
		 ld start = max(P[i]-t,pos+D);
		 ld end = start+D*(V[i]-1);
		 if(end-P[i]>t) return 0;
		 pos=end;
	//	 if(t==2) {
	//		 printf("layd %lld %lld %d\n",start,end,i);
//		 }
		 
	 }
	 return 1;
 }
		
int _tmain(int argc, _TCHAR* argv[])
{
     int t=0;
	 scanf("%d",&t);
	 for(int xx=1;xx<=t;++xx) {
		 scanf("%d %lld",&n,&D);
		 D*=2;
		 ld time=0;
		 REP(i,n)  {
			 ld cnt,w;
			 scanf("%lld %lld",&w,&cnt);
			 P[i]=w*2;
			 V[i]=cnt;
		 }
		 ld low=0, up=ld(4000000)*D;
		 //take care at 0;
        
		 if(!check(0)) while(low+1<up) {
			 ld mid=(low+up)/ld(2);
			 if(check(mid)) {
				 up=mid;
				 time=mid;
			 } else {
				 low=mid;
			 }
		 }
		
		 printf("Case #%d: ",xx);
		 if(time&1) {
			 printf("%lld.5",time/2);
		 } else {
			 printf("%lld",time/2);
		 }
		 printf("\n");

	 }
	return 0;
}

