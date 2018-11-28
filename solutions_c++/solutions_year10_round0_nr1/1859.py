#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INPUT_FILE "A-large.in"


int main()
{
	char line[32], *line_error;
	unsigned int K,N,T, tc, mask;
	
	//read input file
	FILE* fp = fopen(INPUT_FILE, "r");
	if(!fp)
		return -1;

	//read first line to determine T
	line_error = fgets(line, 32, fp);
	if(!line_error)
		return -2;
	sscanf(line, "%d", &T);

	//do all T test cases
	for(tc=1; tc<=T; tc++)
	{
		//find N (snappers) and K (finger snappings)
		line_error = fgets(line, 32, fp);
		if(!line_error)
			return -3;
		sscanf(line, "%d %d", &N, &K);

		mask = (1<<N) - 1;
		if((K&mask) == mask)
			printf("Case #%u: ON\n", tc);
		else
			printf("Case #%u: OFF\n", tc);
	}

	return 0;
}

