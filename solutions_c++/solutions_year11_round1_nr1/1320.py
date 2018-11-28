// 2011_1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"




int _tmain(int argc, _TCHAR* argv[])
{
	FILE * in	= fopen("1.in","rt");
	FILE * out	= fopen("sout.txt","wt");

	int n;
	fscanf(in,"%d\n",&n);
	for(int i = 0; i<n; i++)
	{
		int n,d,g;
		fscanf(in,"%d %d %d\n",&n,&d,&g);
		bool pp = false;

		int pt = 100;
		int wt = d;
		int lt = 100-d;
		

		if(n < 100)
		{
			for(int j = 1; j<=n; j++)
				if(((j*d) % 100) == 0)
				{
					pt = j;
					wt = j*d/100;
					lt = j-j*d/100;
					pp = true;
					break;
				}
		}
		else pp = true;

		if(pp)
		{
			if(g == 100 && lt > 0) pp = false;
			if(g == 0 && wt > 0) pp = false;
		}

		if(pp) fprintf(out,"Case #%d: Possible\n",i+1);
		else  fprintf(out,"Case #%d: Broken\n",i+1);

	}
	fclose(in);
	fclose(out);
	return 0;
}

