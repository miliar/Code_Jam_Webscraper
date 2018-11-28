// gcj.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<cstdio>
#include<string>
#include<vector>
#include<map>
using namespace std;
#define REP(i,n) for(int i=0;i<(int)(n);++i)
typedef long double ld; 
int _tmain(int argc, _TCHAR* argv[])
{
     int t=0;
	 scanf("%d",&t);
	 for(int xx=1;xx<=t;++xx) {
		 int n;
		 scanf("%d ",&n);
		 ld play[100],win[100],owp[100],oowp[100];
		 REP(i,n) play[i]=win[i]=owp[i]=oowp[i]=0;
		 char p[100][101];
		 REP(i,n) scanf("%s",p[i]);

		 REP(i,n) {
			 REP(j,n) {
				 if(p[i][j]!='.') play[i]++;
				 if(p[i][j]=='1') win[i]++;
			 }
		 }
		 REP(i,n) {
			 REP(j,n) {
				 if(p[i][j]=='1') {
					 owp[i]+=win[j]/(play[j]-1.0);
				 } else if(p[i][j]=='0') {
					 owp[i]+=(win[j]-1)/(play[j]-1.0);
				 }
			 }
		 }
		 REP(i,n) owp[i]/=play[i];
		 REP(i,n) REP(j,n) {
			 if(p[i][j]!='.') {
				 oowp[i]+=owp[j];
			 }
		 }
		 REP(i,n) oowp[i]/=play[i];
		 printf("Case #%d:\n",xx);
		 REP(i,n)  {
			 printf("%.11Lf\n",((win[i]/play[i]+oowp[i])/2.0+owp[i])/2.0);
		 }
	 }
	return 0;
}

