#include <stdio.h>
#include <string>
#include <iostream>
#include <math.h>

using namespace std;

int main()
{

	FILE *inFile,*outFile;
	int num_total_cases,num_N,num_K;

	fopen_s(&inFile,"A-large.in","r");
	
	fopen_s(&outFile,"A-large.out","w");
	
	fscanf_s(inFile,"%d",&num_total_cases);

	for(int k=0;k<num_total_cases;k++)
	{
		long double clicks_x_cycle,
			clicks_surpassed;

		fscanf_s(inFile,"%d %d",&num_N,&num_K);
		clicks_x_cycle = pow(long double(2),long double(num_N));
		clicks_surpassed = fmod(long double(num_K + 1),clicks_x_cycle);
		if(clicks_surpassed == 0)
			fprintf(outFile,"Case #%d: ON\n",k+1);
		else
			fprintf(outFile,"Case #%d: OFF\n",k+1);
	}

	fclose(inFile);
	fclose(outFile);
	
	return 1;
}

