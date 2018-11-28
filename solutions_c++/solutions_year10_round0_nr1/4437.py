// snapchain.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "stdio.h"
#include "conio.h"


int _tmain(int argc, _TCHAR* argv[])
{
	FILE* f;
	FILE* f1;
	f= fopen("input.txt","rt");

	f1= fopen("output.txt","wt");

	if (f==NULL)
	{
		printf("ko mo duoc file");
	}

	int t;
	int n,k;
	
	fscanf(f, "%d", &t);
	int *a;

	for (int i=0;i<t;i++)
	{
		fscanf(f, "%d %d",&n, &k );
		a= new int[n+1];
		for (int j=0;j<=n;j++)
			a[j]= 0;

		for (int j=0;j<k;j++)
		{
			int r=0;

			if (a[r]==1)
			{
				while (a[r]&& (r<n))
				{
					a[r]=0;
					r++;
				}
				a[r]=1;

			}
			else
				a[r]=1;
		}
		
		int temp=0;
		a[n]=0;
		while (a[temp]) 
			temp++;
		if (temp==n)
			fprintf(f1,"Case #%d: ON\n",i+1);
		else
			fprintf(f1,"Case #%d: OFF\n",i+1);
		delete a;
	}

	fclose(f);
	fclose(f1);
	

	





	return 0;
}

