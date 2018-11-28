// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<cstdio>
#include<cmath>
#define REP(i,n) for(int i=0;i<(n);++i)
int abs(int x) {
if(x<0) return -x;
return x;
}

int max(int a,int b) {
	if(a>b) return a;
	return b;
}
int _tmain(int argc, _TCHAR* argv[])
{
	int T;
	scanf("%d ",&T);
	REP(xx,T) {
		int n;
		int p[2],t[2];
		REP(i,2) p[i]=1;
		REP(i,2) t[i]=0;
		int ct = 0;
		scanf("%d ",&n);
		REP(i,n) {
			char c;
			int x,r;
			scanf("%c %d ",&c,&x);
			r=c=='B' ? 1:0;
			t[r]=max(ct+1, t[r]+abs(p[r]-x)+1);
			p[r]=x;
			ct=t[0];
			if(t[1]>ct) ct=t[1];
		}
		printf("Case #%d: %d\n",xx+1,ct);		
	}
	return 0;
}

