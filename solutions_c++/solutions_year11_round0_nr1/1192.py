// 2011_1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


int _tmain(int argc, _TCHAR* argv[])
{
	FILE * in	= fopen("large.in","rt");
	FILE * out	= fopen("out_large.txt","wt");

	int n;
	fscanf(in,"%d\n",&n);

	for(int i = 0; i<n; i++)
	{
		int k;
		fscanf(in,"%d ",&k);

		int bp = 1, bt = 0;
		int op = 1, ot = 0;
		for(int j = 0; j<k; j++)
		{
			char c;
			int  p;
			fscanf(in,"%c ",&c);
			fscanf(in,"%d ",&p);
			if(c == 'O')
			{
				ot += abs(p-op)+1;
				if(ot < bt+1) ot = bt+1;
				op = p;
			}
			else if(c == 'B')
			{
				bt += abs(p-bp)+1;
				if(bt < ot+1) bt = ot+1;
				bp = p;
			}

		}
		fprintf(out,"Case #%d: %d\n",i+1, max(ot,bt));
	}
	fclose(in);
	fclose(out);
	return 0;
}

