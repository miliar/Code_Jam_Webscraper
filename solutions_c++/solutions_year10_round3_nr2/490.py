// cjr32.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


int _tmain(int argc, _TCHAR* argv[])
{
	int l,p,c,total;
	FILE *fp=fopen("inp","r");
	FILE *fout=fopen("out","w");
	fscanf(fp,"%d",&total);
	for(int i=0;i<total;i++)
	{
		fscanf(fp,"%d %d %d",&l,&p,&c);
		int mult=l;
		int n=1;
		while(mult<p)
		{
			mult=mult*c;
			n++;
		}
		n=n-2;
//		printf("Value of n: %d ",n);
		int count=0;
		while(n!=0)
		{
			n=n/2;
			count++;
		}
		printf("Case #%d: %d\n",i+1,count);
		fprintf(fout,"Case #%d: %d\n",i+1,count);
	}
	return 0;
}

