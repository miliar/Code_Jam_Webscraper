// GoogleCodeJamQualifier.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
//using namespace std;

#define null 0

int PowerOf2(int n)
{
	if(n == 0) return 1;
	return 2 * PowerOf2(n-1);
}

int main(int argc, char* argv[])
{
	FILE *fp2 = null, *fp1 = null;
	while(true)
	{
		if(argc != 3)
		{
			std::cout<<"\nPlease enter the input filename\n";
			break;
		}

		fp1 = fopen(argv[1], "r");

		if(fp1 == null)
		{
			std::cout<<"\nInput file could not be opened\n";
			break;
		}

		fp2 = fopen(argv[2], "w");

		if(fp2 == null)
		{
			std::cout<<"\nOutput file could not be opened\n";
			break;
		}

		int iCount = 0;
		int N = 0, K = 0;

		fscanf(fp1,"%d", &iCount);

		for(int i=0; i<iCount; i++)
		{
			fscanf(fp1, "%d %d", &N, &K);
			if(K == 0)
				fprintf(fp2, "Case #%d: OFF\n", i+1);
			else
			{
				int iPowerOf2 = PowerOf2(N);
				if(((K+1)%iPowerOf2) == 0)
				{
					fprintf(fp2, "Case #%d: ON\n", i+1);
				}
				else
					fprintf(fp2, "Case #%d: OFF\n", i+1);
			}
		}
		
		break;
	}

	if(fp1 != null)
		fclose(fp1);

	if(fp2 != null)
		fclose(fp2);

	return 0;
}

