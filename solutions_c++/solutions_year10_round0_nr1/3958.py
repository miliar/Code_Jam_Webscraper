#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int powerof(uint64_t base, uint64_t n)
{
	uint64_t result = 1;
	for (uint64_t i = 0; i < n; ++i)
	{
		result *= base;
	}
	return result;
}

bool snapper(uint64_t snaps, uint64_t snapperCount)
{
	uint64_t bits = powerof(2, snapperCount);
	uint64_t mod = snaps % bits;
	return (mod == bits-1);
}

int main()
{
	FILE *input = fopen("input.txt", "r");
	FILE *output = fopen("output.txt", "w");
	
	char *buffer = new char[4096];
	
	//# of test cases
	fgets(buffer, 4096, input);
	int testCases = atoi(buffer);
	
	//for each test case
	for(int i = 0; i < testCases; ++i)
	{
		fgets(buffer, 4096, input);
		int N = atoi(strtok(buffer, " "));
		int k = atoi(strtok(NULL, " "));
		
		sprintf(buffer, "Case #%d: %s\n", i+1, snapper(k, N) ? "ON" : "OFF");
		fputs(buffer, output);
	}
	
	fclose(input);
	fclose(output);
	delete[] buffer;
}


