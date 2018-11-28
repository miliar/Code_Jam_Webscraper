// candy.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "stdlib.h"

int a[1000];

void sort(int n)
{
	bool gata = false;
	int aux;

	while(!gata)
	{
		gata = true;
		for(int i=0; i<n-1; i++)
			if(a[i] > a[i+1])
			{
				gata = false;
				aux = a[i];
				a[i] = a[i+1];
				a[i+1] = aux;
			}
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	FILE *fi=fopen("input.txt","rt");
	FILE *fo=fopen("output.txt","wt");

	int testNb, up[1000], down[1000];

	fscanf(fi,"%d",&testNb);

	for(int tst=1; tst<=testNb; tst++)
	{
		int n;
		fscanf(fi,"%d",&n);
		for(int i=0; i<n; i++)
			fscanf(fi,"%d",&a[i]);

		sort(n);

		up[0] = a[0];
		for(int i=1; i<n; i++)
			up[i] = (a[i] ^ up[i-1]);

		down[n-1] = a[n-1];
		for(int i=n-2; i>=0; i--)
			down[i] = (a[i] ^ down[i+1]);

		bool sol = false;
		for(int i=0; i<n-1; i++)
			if(up[i] == down[i+1])
			{
				int sum=0;
				for(int j=i+1; j<n; j++)
					sum+=a[j];

				fprintf(fo,"Case #%d: %d\n",tst,sum);
				sol = true;
				break;
			}

		if(!sol) fprintf(fo,"Case #%d: NO\n",tst);

	}

	fclose(fi);
	fclose(fo);
	return 0;
}

