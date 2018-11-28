#include <iostream>
#include <math.h>

using namespace std;

const unsigned int n[31] = {0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575, 2097151, 4194303, 8388607, 16777215, 33554431, 67108863, 134217727, 268435455, 536870911, 1073741823};

unsigned int N, k, T;

void main(int argc, char **argv)
{
	FILE *input;
	FILE *output;

	input = fopen(argv[1], "r");
	output = fopen(argv[2], "w");

	fscanf(input, "%u", &T);

	for(int i=1; i<=T; i++)
	{
		fscanf(input, "%u %u", &N, &k);

		if(((k+1) & n[N]) == 0)
			fprintf(output, "Case #%u: ON\n", i);
		else
			fprintf(output, "Case #%u: OFF\n", i);
	}

	fclose(input);
	fclose(output);
}