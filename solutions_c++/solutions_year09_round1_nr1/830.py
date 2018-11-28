// multi.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

int happy(int n, int base) {
	int x,nn,d;

	if ((base==2)||(base==4)) return 1;

	for(x=0;x<20;x++) {
		nn=0;
		while(n>0) {
			d=n%base;
			n=n/base;
			nn+=d*d;
		}
		n=nn;
		if (n==1) return 1;
	}
	return 0;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int end, i, t, n, nb, tb;
	int bases[10];
	char str[500];

    scanf("%d\n",&t);
	for (i=0;i<t;i++) {
		gets(str);
		nb=sscanf(str,"%d %d %d %d %d %d %d %d %d %d\n",&bases[0],&bases[1],&bases[2],&bases[3],&bases[4],&bases[5],&bases[6],&bases[7],&bases[8],&bases[9]);
		n=1;
		end=0;
		while((n<100000)&(!end)) {
			n++;
			for (tb=0;(tb<nb)&(happy(n,bases[tb]));tb++);
			end=(tb==nb);
		}
		printf("Case #%d: %d\n",i+1,n);
	}
	return 0;
}

