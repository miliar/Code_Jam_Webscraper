// Snapper.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define BINARY_MAX_SIZE 7	//Max value is 100 so 7 bits covers it
	
int main(int argc, char* argv[])
{
	int T;				//Number of Inputs
	int N;				//Number of Snapper Devices
	int K;				//Number of Finger Snaps
	int i;

	FILE *input;
	FILE *output;

	input = fopen("A-small-attempt0.in","r");
	output = fopen("A-small-attempt0.out","w");

	printf("%d", sizeof(int));
	if(input != NULL)	//If Input file exists
	{
		fscanf(input,"%d",&T);						//Read Num of Inputs
		printf("%d\n",T);

		for(i=0;i<T;i++)
		{
			fscanf(input,"%d",&N);					//Read Num of Snappers
			fscanf(input,"%d",&K);					//Read Num of Finger snaps

			int bitmask = (pow(2,double(N) ))-1;		//Calculate Value for all Snappers on 
			int ans = K & bitmask;						//AND bitmask and K(num of clicks)

			printf("bitmask = %d\t",bitmask);
			printf("ans = %d\n", ans);

			if(ans == bitmask)							//If num of clicks == bitmask 
				fprintf(output,"Case #%d: %s\n",(i+1),"ON");		//Output Result
			else
				fprintf(output,"Case #%d: %s\n",(i+1),"OFF");		//Output Result
		}
	}
	// Release Files
	fclose(input);
	fclose(output);
	return 0;
}